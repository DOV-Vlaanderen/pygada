# UTF-8
# date as yyyy-mm-dd
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pygada.explorative_data_analysis.interactive_plots.highcharts import Highcharts
from datetime import date

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


def count_datapoints_timeseries_extended():
    df = pd.read_csv('demo_dataset_filtered_3D.txt')
    colors = ["#f8902d", "#8b6ea6", "#6ebe43", "#9c7848", "#e0592a", "#c28942", "#41796c"]
    min_date = min(df.date)

    def count_date(inputdata, matrix):
        datelist = pd.date_range(start=min_date, end=date.today(), freq='1d')
        dateframe = pd.DataFrame(datelist, columns=['date'])
        df2 = inputdata[inputdata['matrix'] == matrix]
        df2["date"] = df2["date"].astype("datetime64")
        df2 = df2[["date"]].groupby(df2.date.dt.to_period("D")).agg('count')
        df2 = df2.to_timestamp()
        df2 = pd.DataFrame(df2)
        df2 = df2.rename(columns={"date": "count"})
        idx = pd.date_range(df2.index.values[0], df2.index.values[-1])
        df2 = df2.reindex(idx)
        df2 = df2.reset_index()
        df2 = df2.rename(columns={"index": "date"})
        # df2['date'] = df2["date"].astype(str)
        df2 = df2.fillna(0)
        date_count = dateframe.merge(df2, how='left', on='date')
        date_count = date_count.fillna(0)
        date_count['date'] = date_count["date"].astype(str)

        return date_count

    series = []
    count = 0
    for i in df.matrix.unique():
        data = []
        data_1 = count_date(df, i)
        for j in range(len(data_1)):
            data_2 = {'name': f'{i}', 'x': data_1.iloc[j]['date'], 'y': data_1.iloc[j]['count'], 'drilldown': 'true'}
            data.append(data_2)
        series.append({'name': i, 'data': data, 'type': 'line', 'color': colors[count]})
        count+=1

    def count_date2(inputdata, matrix, source):
        datelist = pd.date_range(start=min_date, end=date.today(), freq='1d')
        dateframe = pd.DataFrame(datelist, columns=['date'])
        df2 = inputdata[(inputdata['matrix'] == matrix) & (inputdata['source'] == source)]
        if len(df2) != 0:
            df2["date"] = df2["date"].astype("datetime64")
            df2 = df2[["date"]].groupby(df2.date.dt.to_period("D")).agg('count')
            df2 = df2.to_timestamp()
            df2 = pd.DataFrame(df2)
            df2 = df2.rename(columns={"date": "count"})
            idx = pd.date_range(df2.index.values[0], df2.index.values[-1])
            df2 = df2.reindex(idx)
            df2 = df2.reset_index()
            df2 = df2.rename(columns={"index": "date"})
            # df2['date'] = df2["date"].astype(str)
            df2 = df2.fillna(0)
            date_count = dateframe.merge(df2, how='left', on='date')
            date_count = date_count.fillna(0)
            date_count['date'] = date_count["date"].astype(str)

            return date_count

    drilldown_series = ''
    series1 = ''
    series2 = ''
    count = 0
    for i in df.matrix.unique():
        colorcount = 0
        for j in df.source.unique():
            data_1 = count_date2(df, i, j)
            drilldown_data = []
            if type(data_1) is not type(None):
                for k in range(len(data_1)):
                    drilldown_data.append([data_1.iloc[k]['date'], data_1.iloc[k]['count']])
                if count == 0:
                    drilldown1 = f'"{i} {j}": ' + '{' + f'name: "{j}", color:"{colors[colorcount]}", id:0, data: {drilldown_data}' + '}'
                    serie1 = 'drilldowns[e.point.name +' + f'" {j}"]'
                    serie2 = f'chart.addSingleSeriesAsDrilldown(e.point,series[{count}])'
                else:
                    drilldown1 = f',"{i} {j}": ' + '{' + f'name: "{j}", color:"{colors[colorcount]}", data: {drilldown_data}' + '}'
                    serie1 = ',drilldowns[e.point.name +' + f'" {j}"]'
                    serie2 = f';chart.addSingleSeriesAsDrilldown(e.point,series[{count}])'
                drilldown_series += drilldown1
                if serie1.replace(',', '') not in series1:
                    series1 += serie1
                if serie2.replace(';', '') not in series2:
                    series2 += serie2
                count += 1
                colorcount += 1
    drilldown = 'function(e) {if(!e.seriesOptions){var chart=this,drilldowns = {' + drilldown_series + '}, series = [' + series1 + ']; ' + series2 + ';chart.applyDrilldown()' + '}}'
    drilldown = drilldown.replace("'", '"')

    highcharts = Highcharts(df)
    highcharts.count_datapoints_timeseries_extended(series, drilldown)

#df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')
#count_datapoints_timeseries(df, type='dynamic', datetype='D')
count_datapoints_timeseries_extended()

