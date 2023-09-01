import numpy as np
import pandas as pd


class DetectionCondition:
    """Class to handle the detection condition."""

    def __init__(self, dataset):
        """
        Initialize the class.

        Parameters
        ----------
        dataset: dataframe
            The input dataset.
        """

        self.df = dataset

    def lower_bound(self):
        """
        Change the values to zero if the detection condition is '<'. The lower-bound principle.

        Returns
        -------
        df: dataframe
            The dataset with adapted values to the lower-bound principle for the detection condition.
        """

        self.df['value'] = np.where(self.df['detection_condition'] == '<', 0, self.df['value'])

        return self.df

    def middle_bound(self):
        """
        Change the values to the detection limit divided by two if the detection condition is '<'. The middle-bound principle.

        Returns
        -------
        df: dataframe
            The dataset with adapted values to the middle-bound principle for the detection condition.
        """

        self.df['value'] = np.where(self.df['detection_condition'] == '<', self.df.value.astype(float).div(2), self.df['value'])

        return self.df

    def upper_bound(self):
        """
        Change the values to the detection limit if the detection condition is '<'. The upper-bound principle.

        Returns
        -------
        df: dataframe
            The dataset with adapted values to the upper-bound principle for the detection condition.
        """

        self.df['value'] = np.where(self.df['detection_condition'] == '<', self.df['value'], self.df['value'])

        return self.df


if __name__ == '__main__':
    df = pd.read_csv('../../datasets/PFAS/test_dataset.txt')
    print(df[['detection_condition', 'value']].head(1))

    df_lower = df.copy()
    dc = DetectionCondition(df_lower)
    df_lower = dc.lower_bound()
    print(df_lower[['detection_condition', 'value']].head(1))

    df_middle = df.copy()
    dc = DetectionCondition(df_middle)
    df_middle = dc.middle_bound()
    print(df_middle[['detection_condition', 'value']].head(1))

    df_upper = df.copy()
    dc = DetectionCondition(df_upper)
    df_upper = dc.upper_bound()
    print(df_upper[['detection_condition', 'value']].head(1))