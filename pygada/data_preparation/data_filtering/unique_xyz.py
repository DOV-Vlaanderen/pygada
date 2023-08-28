import pandas as pd

from pygada.data_preparation.data_filtering.data_wrangling import FilterTransformData


def filter_to_3d(df):
    df_len_start = len(df)
    df2 = df[df.duplicated(subset=['field_lab', 'parameter', 'x', 'y', 'top', 'bottom', 'source'])]
    df2 = df2.reset_index()
    df_copy = df.copy()
    for i in range(len(df2)):
        df3 = df_copy[(df_copy['field_lab'] == df2['field_lab'][i]) &
                      (df_copy['parameter'] == df2['parameter'][i]) &
                      (df_copy['x'] == df2['x'][i]) &
                      (df_copy['y'] == df2['y'][i]) &
                      (df_copy['top'] == df2['top'][i]) &
                      (df_copy['bottom'] == df2['bottom'][i]) &
                      (df_copy['source'] == df2['source'][i])]
        df = df.drop(df3.index)
        df3 = df3.sort_values('date', ascending=False)
        unique_recent_date = df3.loc[df3['date'] == df3['date'].iloc[0]]
        len_unique_recent_date = len(df3.loc[df3['date'] == df3['date'].iloc[0]])
        if len_unique_recent_date == 1:
            df = pd.concat([df, unique_recent_date])
        elif len_unique_recent_date > 1:
            df3 = unique_recent_date
            mean_value = df3['value'].mean()
            df3['value'].iloc[0] = mean_value
            df = pd.concat([df, df3.head(1)])
    df_len_end = len(df)
    print(f'Filtered {df_len_start-df_len_end} datapoints.')
    return df


if __name__ == '__main__':

    pd.set_option('display.max_columns', None)
    df_gw = pd.read_csv('C:/Users/vandekgu/PycharmProjects/pygada/pygada/test_data/results/gw_test_data_adapted.csv')
    #print(df_gw)
    ftd = FilterTransformData()
    df_gw = ftd.top_filter(df_gw)
    df_gw = ftd.change_df_col_names(df_gw, 'groundwater')


    df = filter_to_3d(df_gw)
