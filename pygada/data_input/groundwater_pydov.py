import os

import pandas as pd
from pydov.search.grondwatermonster import GrondwaterMonsterSearch
from pydov.search.grondwaterfilter import GrondwaterFilterSearch
from pydov.util.location import Within, Box
from pydov.util.query import Join
from loguru import logger
from owslib.fes2 import PropertyIsEqualTo, Or


def parameter_group(parameter):
    """ Define the parameter group based on the parameter. The parameter group will then be used to query on.
    This will significantly reduce the download time.

    Parameters
    ----------
    parameter : list
        A list with the user-defined parameters.

    Returns
    -------
    param_group : list[str]
        A list with the occurring parameter groups, based on the parameters.

    """

    param_group = []

    kationen = ['K', 'NH4', 'Fe', 'Mn', 'Ca', 'Mg', 'Fe2+', 'Na', 'SomKAT', 'Fe(Tot.)', 'Sr', 'Fe3+']
    anionen = ['HCO3', 'F', 'PO4', 'Cl', 'NO3', 'CO3', 'NO2', 'SO4', 'Br', 'SomAN', 'PO4(Tot.)', 'OH']
    zware_metalen = ['Pb', 'Al', 'Hg', 'Cd', 'Cu', 'Co', 'Ni', 'Cr', 'As', 'Zn', 'B', 'Ba', 'Ti', 'Sn', 'Sb']
    pesticiden_actieve_stoffen = ['metola-S', 'Simaz', 'Chlortol', 'Isoprot', 'Glyfos', 'Atraz', 'Linur', 'Bentaz',
                                  'Diur', 'Terbu', 'Chloridaz', 'fluopicolide', 'flufe', 'Imida', 'Mesotri',
                                  'trichlorpyr', 'Triflox', 'Fluroxypyr', 'Metox', 'Hexaz', 'Metobro', '245t',
                                  'Propaz', 'Prometr', 'Sebu', 'mcpa', 'Dichlorpr', 'Metaza', 'Carben', 'PropaCl',
                                  'Mecopr', 'mcpb', 'Linur_mono', 'Metami', 'Methabenz', 'Terbutryn', 'Cyana',
                                  'Ethofum', 'Clproph', 'Carbet', '24db', '24d', 'Fenoprop', '5ClFenol', 'Propan',
                                  'Ala', 'Dicam', 'brom']
    pesticiden_relevante_metabolieten = ['atr_des', 'DMS', 'chazr', 'meta11', 'meta9', 'Atr_desisoprop', 'Terbu_des']
    niet_relevante_metabolieten_van_pesticiden = ['AMPA', 'VIS', 'BAM', 'meta8', 'Metola-S-ESA', 'Dchdzn', 'meta4']
    fysico_chemische_parameters = ['EC(Lab.)', 'T', 'EC', 'pH', 'TOC', 'O2', 'Eh°', 'pH(Lab.)', 'TDS', 'Temp.',
                                   'EC(Veld)', 'pH(Veld)', 'droogrest', 'H(tot)', 'TAP', 'TAM', 'DOC']
    organische_verbindingen = ['Tri', 'Per', 'CN']
    chemisch_PFAS = ['PFOSA', 'PFECHS', '8:2 FTS', 'ADONA', 'PFOAbranched', 'EtPFOSA', 'PFTrDS', 'PFPeA', 'PFHxA',
                     '8:2 FTUCA', 'PFTeDA', 'MePFOSA', 'PFDA', '8:2 diPAP', '6:2 FTS', 'PFOAtotal', 'PFNS', 'PFDoDS',
                     'PFOSbranched', 'MePFOSAA', 'HFPO-DA', 'PFDoDA', 'PFBA', 'PFHxDA', '6:2 diPAP', 'PFOS', 'PFUnDA',
                     'PFHpS', 'PFHxS', '6:2/8:2 diPAP', 'PFOA', 'P37DMOA', '9Cl-PF3ONS', '4:2 FTS', 'HPFHpA', 'PFHpA',
                     'PFNA', '10:2 FTS', '4H-PFUnDA', 'PFUnDS', 'PFBS', 'PFODA', 'PFTrDA', 'PFDS', 'PFOStotal', 'PFPeS',
                     'PFBSA', 'EtPFOSAA']
    andere_parameters = ['%AfwijkBalans', 'P2O5', 'Si']

    parameter_groups = [kationen, anionen, zware_metalen, pesticiden_actieve_stoffen, pesticiden_relevante_metabolieten,
                  niet_relevante_metabolieten_van_pesticiden, fysico_chemische_parameters, organische_verbindingen,
                  chemisch_PFAS, andere_parameters]

    parameter_groups_str = ['kationen', 'anionen', 'zware_metalen', 'pesticiden_actieve_stoffen',
                            'pesticiden_relevante_metabolieten', 'niet_relevante_metabolieten_van_pesticiden',
                            'fysico_chemische_parameters', 'organische_verbindingen', 'chemisch_PFAS',
                            'andere_parameters']

    for i in parameter:
        for j in parameter_groups:
            if i in j:
                param_group.append(parameter_groups_str[parameter_groups.index(j)])
    param_group = list(set(param_group))

    return param_group


def groundwater_request(parameter, bounding_box):
    """Download the groundwater monsters and filter data for the chosen parameter(s).

    Parameters
    ----------
    parameter : list
        A list with the user-defined parameters.
    bounding_box : str
        The coordinates of a bounding box.

    Returns
    -------
    data : dataframe
        The groundwater data.
    """

    if bounding_box == 'flanders':
        lowerleftx = 15000
        lowerlefty = 150000
        upperrightx = 270000
        upperrighty = 250000
    else:
        bblist = bounding_box.split(',')
        lowerleftx = int(bblist[0])
        lowerlefty = int(bblist[1])
        upperrightx = int(bblist[2])
        upperrighty = int(bblist[3])
    bbox = Box(lowerleftx, lowerlefty, upperrightx, upperrighty)

    gwmonster = GrondwaterMonsterSearch()
    logger.info(f"Downloading the groundwater monsters data.")
    param_group = parameter_group(parameter)
    if len(param_group) > 1:
        query = []
        for i in param_group:
            query.append(PropertyIsEqualTo(propertyname=i, literal='true'))
        query = Or(query)
    else:
        query = PropertyIsEqualTo(propertyname=param_group[0], literal='true')
    df = gwmonster.search(location=Within(bbox), query=query)
    data = df[df.parameter.isin(parameter)]
    data["datum_monstername"] = pd.to_datetime(data["datum_monstername"])

    gwfilter = GrondwaterFilterSearch()
    logger.info(f"Downloading the corresponding groundwater filter data.")
    filter_elements = gwfilter.search(query=Join(data, "pkey_filter"), return_fields=["pkey_filter", "aquifer_code",
        "diepte_onderkant_filter", "lengte_filter"])

    data = pd.merge(data, filter_elements)

    return data


# df = groundwater_request(['As', 'Tri'], 'flanders')
# path = os.getcwd()
# df.to_csv(path+'/gw_data.csv', header=True, index=True, sep="\t", mode="a")
# print(df)

# todo, add extra filtering on query? f.e. specific years?
