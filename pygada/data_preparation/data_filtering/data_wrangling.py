import pandas as pd


class FilterTransformData:
    """Class to filter and transform the data."""

    def __init__(self, dataset):
        """Initialize the class."""

        self.df = dataset

    """def top_filter(self, df):

        df['diepte_bovenkant_filter'] = df['diepte_onderkant_filter'].replace(',', '.', regex=True).astype(float)-df['lengte_filter'].replace(',', '.', regex=True).astype(float)

        return df

    def change_df_col_names(self, df):

        df = df.rename(
                columns={'pkey_grondwatermonster': 'id',
                         'datum_monstername': 'date',
                         'datum': 'date',
                         'waarde': 'value',
                         'eenheid': 'unit',
                         'diepte_onderkant_filter': 'basis_m_mv',
                         'diepte_bovenkant_filter': 'top_m_mv',
                         'veld_labo': 'field_lab',
                         'pkey_bodemobservatie': 'id',
                         'observatie': 'date',
                         'diepte_tot_cm': 'basis_m_mv',
                         'diepte_van_cm': 'top_m_mv',
                         })
        return df

    def change_depth_units(self, df, medium):

        if medium == 'soil':
            df['top'] = df['top']/100
            df['bottom'] = df['bottom']/100

        return df"""

    def filter_on_attribute(self):

        self.df = self.df[['id', 'date', 'x_m_L72', 'y_m_L72', 'top_m_mv', 'basis_m_mv', 'parameter', 'detection_condition', 'value', 'unit', 'source', 'matrix']]

        return self.df

    def transform_to_float(self):

        self.df[['x_m_L72', 'y_m_L72', 'top_m_mv', 'basis_m_mv', 'value']] = self.df[['x_m_L72', 'y_m_L72', 'top_m_mv', 'basis_m_mv', 'value']].replace(',', '.', regex=True).astype(float)

        return self.df

    def check_units(self):

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

    """def check_date(self):
        self.df['date'] = pd.to_datetime(self.df['date'])

        return self.df"""


if __name__ =='__main__':

    dataset = pd.read_csv('../../datasets/PFAS/demo_dataset.txt')
    ftd = FilterTransformData(dataset)
    df = ftd.check_units()
    print(df)
