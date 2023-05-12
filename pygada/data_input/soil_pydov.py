from pydov.types.bodemobservatie import Bodemobservatie
from pydov.util.location import Within, Box
from pydov.util.query import PropertyInList
from pydov.search.bodemobservatie import BodemobservatieSearch
from owslib.fes2 import And

bbox_flanders = Box(15000, 150000, 270000, 250000)


class ParameterInList(PropertyInList):
    def __init__(self, parameters):
        """Initialisation.

        Parameters
        ----------
        parameters : list of str
            List of parameter names to include in the query.
        """
        super().__init__('parameter', parameters)


class SoilRequest(BodemobservatieSearch):
    def __init__(self, parameters):
        super().__init__(Bodemobservatie)

        self.parameters = parameters
        self.return_fields = None

    def search(self, location=None, query=None, sort_by=None,
               max_features=None):
        if query is not None:
            query = And(
                [ParameterInList(self.parameters), query])
        else:
            query = ParameterInList(self.parameters)

        return super().search(
            location, query, sort_by, self.return_fields, max_features
        )


if __name__ == '__main__':

    params = ['Mineralen - glauconiet']

    soil_request = SoilRequest(params)

    data = soil_request.search(
        location=Within(bbox_flanders),
        max_features=10
    )

    #print(data)
    data.to_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/soil_test_data.csv')