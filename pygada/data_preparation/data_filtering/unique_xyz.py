import pandas as pd


def filter_to_3d(df):
    """
    Filter the dataset to a 3D dataset containing unique values, considering the most recent data for the combination of following attributes:\n
    - parameter
    - x_m_L72
    - y_m_L72
    - top_m_mv
    - basis_m_mv
    - source
    - matrix

    If multiple records have these unique combination, the mean of the values is considered.

    Parameters
    ----------
    df: dataframe
        The input dataset.

    Returns
    -------
    df: dataframe
        The transformed dataset containing 'unique xyz-coordinates'.
    """

    df_len_start = len(df)
    df2 = df[df.duplicated()]
    df2 = df2.reset_index()
    df_copy = df.copy()
    for i in range(len(df2)):
        df3 = df_copy[(df_copy['parameter'] == df2['parameter'][i]) &
                      (df_copy['x_m_L72'] == df2['x_m_L72'][i]) &
                      (df_copy['y_m_L72'] == df2['y_m_L72'][i]) &
                      (df_copy['top_m_mv'] == df2['top_m_mv'][i]) &
                      (df_copy['basis_m_mv'] == df2['basis_m_mv'][i]) &
                      (df_copy['source'] == df2['source'][i]) &
                      (df_copy['matrix'] == df2['matrix'][i])]
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
