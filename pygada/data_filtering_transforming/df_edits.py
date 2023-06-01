import pandas as pd


class FilterTransformData:
    """Class to filter and transform the data."""

    def __init__(self):
        """Initialize the class."""

    def top_filter(self, df):

        df['diepte_bovenkant_filter'] = df['diepte_onderkant_filter'].replace(',', '.', regex=True).astype(float)-df['lengte_filter'].replace(',', '.', regex=True).astype(float)

        return df

    def change_df_col_names(self, df, medium):

        if medium == 'groundwater':
            df = df.rename(
                columns={'pkey_grondwatermonster': 'index', 'datum_monstername': 'date', 'datum': 'date', 'waarde': 'value', 'eenheid': 'unit',
                         'diepte_onderkant_filter': 'bottom', 'diepte_bovenkant_filter': 'top', 'veld_labo': 'field_lab'})
        elif medium == 'soil':
            df = df.rename(
                columns={'pkey_bodemobservatie': 'index', 'observatie': 'date', 'waarde': 'value', 'eenheid': 'unit',
                         'diepte_tot_cm': 'bottom', 'diepte_van_cm': 'top', 'veld_labo': 'field_lab'})

        return df

    def change_depth_units(self, df, medium):

        if medium == 'soil':
            df['top'] = df['top']/100
            df['bottom'] = df['bottom'] / 100

        return df

    def check_units(self, df, medium):

        unique_units = df['unit'].tolist()

        def most_frequent(list):
            return max(set(list), key=list.count)

        unit = most_frequent(unique_units)

        if medium == 'groundwater':
            df_conv = pd.DataFrame({'mg/l': [1, 0.001, 0.000001],
                                    'µg/l': [1000, 1, 0.001],
                                    'ng/l': [1000000, 1000, 1]},
                                   index=['mg/l', 'µg/l', 'ng/l'])

        for i, j in [('value', unit)]:
            df[i] = df[i]*df['unit'].map(df_conv[j])
            df['unit'] = j

        return df

    def check_date(self, df):
        df['date'] = pd.to_datetime(df['date'])

        return df

#
#df_gw = pd.read_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/gw_test_data.csv')
#df_soil = pd.read_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/soil_test_data.csv')

"""
if __name__ == '__main__':
    df = pd.read_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/data_as_fe_0100.csv')

    ftd = FilterTransformData()

    df = ftd.top_filter(df)
    df = ftd.change_df_col_names(df, 'groundwater')
    df = ftd.check_units(df, 'groundwater')

    df.to_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/data_as_fe_0100_2.csv')
"""
"""
if __name__ == '__main__':
    ftd = FilterTransformData()
    df_gw = ftd.change_df_col_names(df_gw, 'groundwater')
    df_soil = ftd.change_df_col_names(df_soil, 'soil')
    print(df_gw['date'])
    df_gw = ftd.check_date(df_gw)

    print(df_gw['date'])
"""
"""
if __name__ == '__main__':
    ftd = FilterTransformData()
    df_soil = ftd.change_df_col_names(df_soil, 'soil')
    print(df_soil['top'])
    df_gw = ftd.change_depth_units(df_soil, 'soil')
    print(df_soil['top'])
"""

"""
if __name__ == '__main__':
    df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/PFAS/groundwater_VMM.csv', sep=';')

    ftd = FilterTransformData()

    df = ftd.top_filter(df)
    df = ftd.change_df_col_names(df, 'groundwater')
    df = ftd.check_units(df, 'groundwater')
    df = ftd.check_date(df)

    df.to_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')"""