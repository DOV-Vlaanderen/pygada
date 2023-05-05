from enum import Enum
import pandas as pd
import pydov
from pydov.search.grondwaterfilter import GrondwaterFilterSearch
from pydov.types.grondwatermonster import GrondwaterMonster
from pydov.util.location import Within, Box
from pydov.util.net import LocalSessionThreadPool, SessionFactory
from pydov.search.grondwatermonster import GrondwaterMonsterSearch
from owslib.fes2 import OgcExpression, Or, PropertyIsEqualTo, And

from pydov.util.query import Join

bbox_flanders = Box(15000, 150000, 270000, 250000)


class ParameterGroup(object):

    class Type(Enum):
        SOIL = 'B'
        GROUND = 'G'
        WATER = 'W'

    _parameter_groups = dict()

    def __init__(self, grouptype):
        """Initialise a ParameterGroup object for a given group type.

        Parameters
        ----------
        parametergrouptype : ParameterGroup.Type
        """
        self.grouptype = grouptype
        self._update_parameter_groups(self.grouptype)

    @classmethod
    def _update_parameter_groups(cls, grouptype):
        if grouptype in cls._parameter_groups:
            return

        parametergroups = pydov.session.get(
            'https://services.dov.vlaanderen.be/dovkernserver/monster/'
            'codetabellen/parametergroep'
        ).json()

        parameters = []

        def get_parameters(parametergroup, session=None):
            if session is None:
                session = SessionFactory()

            return session.get(
                f'https://services.dov.vlaanderen.be/dovkernserver/monster/'
                f'codetabellen/groep/{parametergroup}/parameters'
            ).json()

        pool = LocalSessionThreadPool()

        for parametergroup in parametergroups:
            if parametergroup['groepType'] == grouptype.value:
                pool.execute(get_parameters, (parametergroup['code'],))

        for r in pool.join():
            if r.get_error():
                raise r.get_error()

            worker_result = r.get_result()
            if worker_result is not None:
                parameters.extend(worker_result)

        cls._parameter_groups[grouptype] = [
            {'parameter': p['korteNaam'],
             'description': p['beschrijving'],
             'group': p['parametergroep']['beschrijving'],
             'groupcode': p['parametergroep']['code']}
            for p in parameters
        ]

    def get_parametergroups(self, parameters):
        """Get a list of parametergroups based on a list of given parameters.

        Parameters
        ----------
        parameters : list of str
            List of parameter names.

        Returns
        -------
        list of str
            List of unique parametergroups for the given parameters.
        """
        return list(set(
            p['group'] for p in self._parameter_groups[self.grouptype]
            if p['parameter'] in parameters
        ))

    def get_parametergroups_codes(self, parameters):
        """Get a list of parametergroup codes based on a list of given
        parameters.

        Parameters
        ----------
        parameters : list of str
            List of parameter names.

        Returns
        -------
        list of str
            List of unique parametergroup codes for the given parameters.
        """
        return list(set(
            p['groupcode'] for p in self._parameter_groups[self.grouptype]
            if p['parameter'] in parameters
        ))

    def get_parameters(self, parametergroups):
        """Get a list of parameter names based on a list of given
        parametergroups.

        Parameters
        ----------
        parametergroups : list of str
            List of parameter groups.

        Returns
        -------
        list of str
            List of unique parameter names for the given parameter groups.
        """
        return list(set(
            p['parameter'] for p in self._parameter_groups[self.grouptype]
            if p['group'] in parametergroups
        ))


class GrondwaterMonsterParameterGroupFilter(OgcExpression):
    def __init__(self, parameters):
        """Initialisation.

        Creates a new filter on parameter groups based on the given parameter
        names. It will allow a first filtering of matching groundwater
        samples, which then will need to be further filtered down on the client.

        Parameters
        ----------
        parameters : list of str
            List of parameter names to include in the query.
        """
        super(GrondwaterMonsterParameterGroupFilter, self).__init__()

        self.parameters = parameters
        self.parameter_group = ParameterGroup(ParameterGroup.Type.WATER)

        self.parametergroup_field_mapping = {
            '1': 'kationen',
            '2': 'anionen',
            '3': 'zware_metalen',
            '4': 'pesticiden_actieve_stoffen',
            '12': 'pesticiden_relevante_metabolieten',
            '13': 'niet_relevante_metabolieten_van_pesticiden',
            '5': 'fysico_chemische_parameters',
            '7': 'organische_verbindingen',
            'GW_CHEM_PFAS': 'chemisch_PFAS'
        }

        self.parametergroup_field_default = 'andere_parameters'

        fields = self._map_to_fields()
        if len(fields) == 1:
            self.query = PropertyIsEqualTo(fields[0], 'true')
        else:
            self.query = Or(
                [PropertyIsEqualTo(field, 'true') for field in fields]
            )

    def _map_to_fields(self):
        parametergroups = self.parameter_group.get_parametergroups_codes(
            self.parameters)

        return list(set(
            self.parametergroup_field_mapping.get(
                pg, self.parametergroup_field_default)
            for pg in parametergroups
        ))

    def toXML(self):
        """Return the XML representation of the
        GrondwaterMonsterParameterGroupFilter query.

        Returns
        -------
        xml : etree.ElementTree
            XML representation of the PropertyInList

        """
        return self.query.toXML()


class GroundwaterRequest(GrondwaterMonsterSearch):
    def __init__(self, parameters):
        super().__init__(GrondwaterMonster)

        self.parameters = parameters
        self.return_fields = None

    def search(self, location=None, query=None, sort_by=None, max_features=None):
        if query is not None:
            query = And(
                [GrondwaterMonsterParameterGroupFilter(parameters), query])
        else:
            query = GrondwaterMonsterParameterGroupFilter(parameters)

        data = super().search(
            location, query, sort_by, self.return_fields, max_features
        )

        data = data[data.parameter.isin(self.parameters)]
        data["datum_monstername"] = pd.to_datetime(data["datum_monstername"])

        gwfilter = GrondwaterFilterSearch()
        filter_elements = gwfilter.search(
            query=Join(data, "pkey_filter"),
            return_fields=["pkey_filter", "aquifer_code",
                           "diepte_onderkant_filter", "lengte_filter"]
        )

        data = pd.merge(data, filter_elements)
        return data


if __name__ == '__main__':
    parameters = ['Fe', 'CO3']

    gw_request = GroundwaterRequest(parameters)

    data = gw_request.search(
        location=Within(bbox_flanders),
        max_features=10
    )

    print(data)
