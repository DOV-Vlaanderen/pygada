# UTF-8
# date as yyyy-mm-dd
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pygada.explorative_data_analysis.interactive_plots.highcharts import Highcharts


def count_datapoints_timeseries(df, type, datetype=None):
    # todo: remove to filtering_transforming
    df["date"] = df["date"].astype("datetime64")

    df = df["date"].groupby(df.date.dt.to_period("M")).agg('count') if datetype == 'M' \
        else df["date"].groupby(df.date.dt.to_period("Y")).agg('count') if datetype == 'Y' \
        else df["date"].groupby(df.date.dt.to_period("D")).agg('count')
    df = df.resample("Y").count() if datetype == 'Y' \
        else df.resample("M").count() if datetype == 'M' \
        else df.to_timestamp()
    df = pd.DataFrame(df)
    df = df.rename(columns={"date": "count"})
    if datetype == 'D':
        idx = pd.date_range(df.index.values[0], df.index.values[-1])
        df = df.reindex(idx)
        df = df.reset_index()
        df = df.rename(columns={"index": "date"})
    else:
        df = df.reset_index()
    df['date'] = df["date"].astype(str)
    df = df.fillna(0)

    if type == 'static':
        if len(df)>30:
            plt.figure(figsize=(len(df)/3, 10))
        elif len(df)<5:
            plt.figure(figsize=(5, 8))
        else:
            plt.figure(figsize=(15, 10))
        sns.lineplot(data=df, x='date', y='count',  color='blue')
        plt.xticks(rotation=90)
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.ylim(ymin=0)
        plt.xlim(xmin=df['date'].values[0], xmax=df['date'].values[-1])
        plt.tight_layout()
        plt.show()
        plt.clf()

    if type == 'dynamic':
        highcharts = Highcharts(df)
        highcharts.count_datapoints_timeseries()


df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')
count_datapoints_timeseries(df, type='dynamic', datetype='D')

