import pandas as pd
from pydov.search.bodemobservatie import BodemobservatieSearch
from pydov.util.location import Within, Box
from loguru import logger
from owslib.fes2 import PropertyIsEqualTo, Or


def soil_request(parameter, bounding_box):
    """Download the soil observations data for the chosen parameter(s).

        Parameters
        ----------
        parameter : list[str]
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
        bblist = bounding_box.split('-')
        lowerleftx = int(bblist[0])
        lowerlefty = int(bblist[1])
        upperrightx = int(bblist[2])
        upperrighty = int(bblist[3])
    bbox = Box(lowerleftx, lowerlefty, upperrightx, upperrighty)

    bodemobservatie = BodemobservatieSearch()
    logger.info(f"Downloading the soil observations data.")

    if len(parameter) > 1:
        query = []
        for i in parameter:
            query.append(PropertyIsEqualTo(propertyname='parameter', literal=i))
        query = Or(query)
    else:
        query = PropertyIsEqualTo(propertyname='parameter', literal=parameter[0])
    df = bodemobservatie.search(location=Within(bbox), query=query)
    data = pd.DataFrame(df)

    return data

# data = soil_request(['Anorganische C - percentage', 'Organische C - percentage'], 'flanders')
