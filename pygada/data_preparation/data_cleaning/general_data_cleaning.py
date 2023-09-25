import json
import os
import pandas as pd
from loguru import logger


class DataCleaning:
    """Class to clean up a dataset."""

    def __init__(self, dataset):
        """Initialize the class.

        Parameters
        ----------
        dataset : dataframe
            The input dataset as a dataframe.

        Returns
        -------
        None"""

        logger.info('Initialize the script to clean up the data.')

        self.df = dataset
        self.metadata = {"# records": len(dataset),
                         "Records with at least 1 error": {},
                         }

    def date(self, column):
        """ Check for missing and unrealistic date records.

        Parameters
        ----------
        column : str
            The column name of the date attribute.

        Return
        ------
        df_error_date : dataframe
            A dataframe containing the records that have no date value."""

        logger.info('Check for missing date.')

        # Check for empty dates
        df_error_date = self.df[(self.df[column].isna())]
        df_error_date['error_date'] = 'empty date'

        # Check for unrealistic dates
        df_result_date = self.df[(~self.df[column].isna())]
        df_result_date['new_date'] = pd.to_datetime(df_result_date['date'], errors='coerce')
        df_error_date_2 = df_result_date.loc[df_result_date['new_date'].isnull()]
        df_error_date_2 = df_error_date_2.drop(['new_date'], axis=1)
        df_error_date_2['error_date'] = 'Unrealistic date'
        df_error_date = df_error_date.append(df_error_date_2)

        self.metadata.update({"Date errors": {"#": len(df_error_date), "%": round(len(df_error_date)/len(self.df)*100, 2)}})

        return df_error_date

    def sum_parameter(self, column, sum_parameters):
        """Check for PFAS sum parameters.
        These parameters already containing some interpretation.
        The lower bound principle, a value lower than the detection limit is equal to zero.

        Parameters
        ----------
        column : str
            The column name of the sum parameter attribute.
        sum_parameters : list
            Possible PFAS sum parameters.

        Return
        ------
        df_error_sp : dataframe
            A dataframe containing sum parameter records.
        """

        logger.info('Check for sum parameters.')

        df_error_sum = self.df[(self.df[column].isin(sum_parameters))]
        df_error_sum['error_sum_parameter'] = 'Sum parameter'

        self.metadata.update({"Sum parameter errors": {"#": len(df_error_sum), "%": round(len(df_error_sum)/len(self.df)*100, 2)}})

        return df_error_sum

    def detection_condition(self, column, detection_conditions):
        """Check for incorrect detection condition.

        Parameters
        ----------
        column : str
            The column name of the detection condition attribute.
        detection_conditions : list
            Allowed detection conditions.

        Return
        ------
        df_error_dc : dataframe
            A dataframe containing the records that have the detection condition equal to '>'."""

        logger.info('Check for incorrect detection condition.')

        df_error_dc = self.df[~(self.df[column].isin(detection_conditions))]
        df_error_dc['error_detection_condition'] = 'incorrect detection condition'

        self.metadata.update({"Detection condition errors": {"#": len(df_error_dc), "%": round(len(df_error_dc) / len(self.df) * 100, 2)}})

        return df_error_dc

    def unit(self, column, units):
        """Check for incorrect unit.

        Parameters
        ----------
        column : str
            The column name of the detection condition attribute.
        units : list
            Allowed units.

        Return
        ------
        df_error_unit : dataframe
            A dataframe containing the records that have an incorrect unit."""

        logger.info('Check for incorrect unit.')

        df_error_unit = self.df[~(self.df[column].isin(units))]
        df_error_unit['error_unit'] = 'incorrect unit'

        self.metadata.update({"Unit errors": {"#": len(df_error_unit), "%": round(len(df_error_unit)/len(self.df)*100, 2)}})

        return df_error_unit

    def top(self, column):
        """Check for missing top.

        Parameters
        ----------
        column : str
            The column name of the top attribute.

        Return
        ------
        df_error_top : dataframe
            A dataframe containing the records that have no top."""

        logger.info('Check for missing top.')

        df_error_top = self.df[(self.df[column].isna())]
        df_error_top['error_top'] = 'No top m mv'

        self.metadata.update({"Top errors": {"#": len(df_error_top), "%": round(len(df_error_top) / len(self.df) * 100, 2)}})

        return df_error_top

    def basis(self, column):
        """Check for missing basis.

        Parameters
        ----------
        column : str
            The column name of the basis attribute.

        Return
        ------
        df_error_basis : dataframe
            A dataframe containing the records that have no basis."""

        logger.info('Check for missing basis.')

        df_error_basis = self.df[(self.df[column].isna())]
        df_error_basis['error_basis'] = 'No basis m mv'

        self.metadata.update({"Basis errors": {"#": len(df_error_basis), "%": round(len(df_error_basis) / len(self.df) * 100, 2)}})

        return df_error_basis

    def meta(self, len_result_df, source, matrix,  save=True):
        """Create a metadata file, containing information about the type and amount of errors (# and %).

        Parameters
        ----------
        len_result_df: int
            The length of the dataframe containing the error data records.
        save: Boolean
            The option to save the metadata file.

        Return
        ------
        metadata : json
            A json object containing the amount of each error."""

        self.metadata.update({"Records with at least 1 error": {"#": len_result_df, "%": round(len_result_df / len(self.df) * 100, 2)}})

        metadata = json.dumps(self.metadata, indent=3)

        if save:
            path = os.getcwd()
            path1 = f"{path}/results"
            if not os.path.exists(path1):
                os.mkdir(f"{path}/results")
            path2 = f"{path}/results/metadata_{source}_{matrix}.json"
            with open(path2, "w") as outfile:
                outfile.write(metadata)

        return metadata
