import pandas as pd


class FilterTransformData:
    """Class to filter and transform the data."""

    def __init__(self):
        """Initialize the class."""

    def top_filter(self, df):

        df['diepte_bovenkant_filter'] = df['diepte_onderkant_filter']-df['lengte_filter']

        return df

    def change_df_col_names(self, df, medium):

        if medium == 'groundwater':
            df = df.rename(
                columns={'pkey_grondwatermonster': 'index', 'datum_monstername': 'date', 'waarde': 'value', 'eenheid': 'unit',
                         'diepte_onderkant_filter': 'bottom', 'diepte_bovenkant_filter': 'top'})
        elif medium == 'soil':
            df = df.rename(
                columns={'pkey_bodemobservatie': 'index', 'observatie': 'date', 'waarde': 'value', 'eenheid': 'unit',
                         'diepte_tot_cm': 'bottom', 'diepte_van_cm': 'top'})

        return df

    def check_units(self, df, medium):

        unique_units = df['unit'].tolist()

        def most_frequent(list):
            return max(set(list), key=list.count)

        unit = most_frequent(unique_units)

        if medium == 'groundwater':
            df_conv = pd.DataFrame({'kg/l': [1, 0.001, 0.000001, 0.000000001, 0.000000000001],
                                    'g/l': [1000, 1, 0.001, 0.000001, 0.000000001],
                                    'mg/l': [1000000, 1000, 1, 0.001, 0.000001],
                                    'µg/l': [1000000000, 1000000, 1000, 1, 0.001],
                                    'ng/l': [1000000000000, 1000000000, 1000000, 1000, 1]},
                                   index=['kg/l', 'g/l', 'mg/l', 'µg/l', 'ng/l'])
        #elif medium == 'soil':

        for i, j in [('value', unit)]:
            df[i] = df[i]*df['unit'].map(df_conv[j])
            df['unit'] = j

        return df


if __name__ == '__main__':
    df = pd.read_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/data_as_fe_0100.csv')

    ftd = FilterTransformData()

    df = ftd.top_filter(df)
    df = ftd.change_df_col_names(df, 'groundwater')
    df = ftd.check_units(df, 'groundwater')

    df.to_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/data_as_fe_0100_2.csv')
