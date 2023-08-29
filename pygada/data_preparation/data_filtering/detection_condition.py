import numpy as np
import pandas as pd


class DetectionCondition:

    def __init__(self, dataset):
        """Initialize the class"""

        self.df = dataset

    def lower_bound(self):

        self.df['value'] = np.where(self.df['detection_condition'] == '<', 0, self.df['value'])

        return self.df

    def middle_bound(self):

        self.df['value'] = np.where(self.df['detection_condition'] == '<', self.df.value.astype(float).div(2), self.df['value'])

        return self.df

    def upper_bound(self):

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