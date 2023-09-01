import pandas as pd


class FilterTransformData:
    """Class to filter and transform the data."""

    def __init__(self, dataset):
        """
        Initialize the class.

        Parameters
        ----------
        dataset: dataframe
            The input data.
        """

        self.df = dataset

    def filter_on_attribute(self):
        """
        Filter a dataframe on the necessary attributes.\n
        - id
        - date
        - x_m_L72
        - y_m_L72
        - top_m_mv
        - basis_m_mv
        - parameter
        - detection_condition
        - value
        - unit
        - source
        - matrix

        Returns
        -------
        df: dataframe
            The filtered dataset, containing only the necessary attributes.
        """

        self.df = self.df[['id', 'date', 'x_m_L72', 'y_m_L72', 'top_m_mv', 'basis_m_mv', 'parameter', 'detection_condition', 'value', 'unit', 'source', 'matrix']]

        return self.df

    def transform_to_float(self):
        """
        Transform the type of the values of some attributes to float.\n
        - x_m_L72
        - y_m_L72
        - top_m_mv
        - basis_m_mv
        - value

        Returns
        -------
        df: dataframe
            The dataset with certain attribute's values as float type.
        """

        self.df[['x_m_L72', 'y_m_L72', 'top_m_mv', 'basis_m_mv', 'value']] = self.df[['x_m_L72', 'y_m_L72', 'top_m_mv', 'basis_m_mv', 'value']].replace(',', '.', regex=True).astype(float)

        return self.df

    def check_units(self):
        """
        Change the unit of soil and groundwater data to the most common unit per matrix.

        Returns
        -------
        df: dataframe
            A dataset with all the records of the same matrix in the same unit.

        """

        result_df = pd.DataFrame()

        for k in self.df['matrix'].unique():
            df_k = self.df[self.df['matrix']==k]
            unique_units = df_k['unit'].tolist()

            def most_frequent(list):
                return max(set(list), key=list.count)

            unit = most_frequent(unique_units)

            if k == 'Groundwater':
                df_conv = pd.DataFrame({'mg/l': [1, 0.001, 0.000001],
                                        'µg/l': [1000, 1, 0.001],
                                        'ng/l': [1000000, 1000, 1]},
                                       index=['mg/l', 'µg/l', 'ng/l'])

            if k == 'Soil':
                df_conv = pd.DataFrame({'mg/kg ds': [1, 0.001, 0.000001],
                                        'µg/kg ds': [1000, 1, 0.001],
                                        'ng/kg ds': [1000000, 1000, 1]},
                                       index=['mg/kg ds', 'µg/kg ds', 'ng/kg ds'])

            for i, j in [('value', unit)]:
                df_k[i] = df_k[i]*df_k['unit'].map(df_conv[j])
                df_k['unit'] = j

            result_df = result_df.append(df_k)
        self.df = result_df

        return self.df


if __name__ =='__main__':

    dataset = pd.read_csv('../../datasets/PFAS/demo_dataset.txt')
    ftd = FilterTransformData(dataset)
    df = ftd.check_units()
    print(df)
