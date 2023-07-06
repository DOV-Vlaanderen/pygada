from highcharts_core.chart import Chart
from highcharts_core.options.series.area import LineSeries
from matplotlib.cbook import boxplot_stats
import pandas as pd
import numpy as np


class Highcharts:

    def __init__(self, input_df, unit=None):

        self.df = input_df
        self.unit = unit

    def boxplot(self):
        df_boxplot_stats = pd.DataFrame({'whislo': [], 'q1': [], 'med': [], 'q3': [], 'whishi': []})
        df_boxplot_outliers = pd.DataFrame({'parameter': [], 'value': []})

        for i in list(self.df.columns):
            boxplot = boxplot_stats(self.df[i].dropna())
            boxplot = pd.DataFrame(boxplot)
            boxplot = boxplot.drop(['mean', 'iqr', 'cilo', 'cihi', 'fliers'], axis=1)
            whishi = boxplot.pop('whishi')
            boxplot.insert(4, 'whishi', whishi)
            df_boxplot_stats = pd.concat([df_boxplot_stats, boxplot])
            outliers = self.df[i][(self.df[i] < boxplot['whislo'].values[0]) | (self.df[i] > boxplot['whishi'].values[0])]
            df_boxplot_outliers = pd.concat(
                [df_boxplot_outliers, pd.DataFrame({'parameter': i, 'value': outliers.values})])

        df_boxplot_stats = df_boxplot_stats.transpose().set_axis(list(self.df.columns.values), axis=1)

        columns = list(df_boxplot_stats.columns)
        data = list(df_boxplot_stats[x].values.tolist() for x in columns)

        index_list = []
        outliers_list = []
        for i in df_boxplot_outliers['parameter'].values.tolist():
            index_list.append(columns.index(i))
        df_boxplot_outliers['index'] = index_list

        for i in range(len(df_boxplot_outliers)):
            outliers_list.append(
                [df_boxplot_outliers['index'].values.tolist()[i], df_boxplot_outliers['value'].values.tolist()[i]])

        data = [{
            "name": "Boxplots",
            "data": data,
            "tooltip": {
                "headerFormat": '<em>Parameter {point.key}</em><br/>'
            },
            "type": 'boxplot'}, {
            "name": "Outliers",
            "data": outliers_list,
            "type": 'scatter',
            "marker": {
                "fillColor": 'white',
                "lineWidth": 0.5,
                "lineColor": "lightblue"
            },
            "tooltip": {
                "headerFormat": '<em>Parameter {point.key}</em><br/>',
                "pointFormat": '<b>Outliers</b> <br/> Concentration: {point.y} ' f'{self.unit}'
            }}
        ]

        options_kwargs = {
            'title': {
                'text': 'Box Plot per Parameter'
            },

            'legend': {
                'enabled': True
            },

            'xAxis': {
                'categories': columns,
                'title': {
                    'text': 'Parameter'
                }
            },

            'yAxis': {
                'type': 'logarithmic',
                'minorTickInterval': 0.1,
                'title': {
                    'text': f'Concentration (log {self.unit})'
                }
            }
        }
        chart = Chart(options=options_kwargs, container='boxplot')
        chart.add_series(*data)

        as_js_literal = chart.to_js_literal('./interactive_plots/rendering/boxplot.js')

        return as_js_literal

    def correlation_heatmap(self, container, data_info, max_df=None):

        data_highcharts = []

        columns = list(self.df.columns)
        data = list(self.df[x].values.tolist() for x in columns)
        for i in range(len(data)):
            for j in range(len(data)):
                data_highcharts.append([i, j, data[i][j]])

        data = [{
                "name": "Correlation",
                "borderWidth": 1,
                "data": data_highcharts,
                "type": 'heatmap',
                "dataLabels": {
                    "enabled": True,
                }}
        ]

        max = max_df if max_df else 1

        options_kwargs = {
            'title': {
                'text': f'Correlation {data_info}'
            },
            'legend': {
                'align': 'right',
                'layout': 'vertical',
                'margin': 0,
                'verticalAlign': 'top',
                'y': 25,
                'symbolHeight': 280,
            },
            'xAxis': {
                'categories': columns,
                'title': {
                    'text': 'Parameter'
                }
            },
            'yAxis': {
                'categories': columns,
                'title': {
                    'text': f'Parameter'
                },
                'reversed': True
            },
            'colorAxis': {
                'reversed': False,
                'min': 0,
                'max': max,
                'minColor': '#FFFFFF',
                'maxColor': '#00C1FF',
            },
            'chart': {
                'type': 'heatmap',
                'marginTop': 40,
                'marginBottom': 80,
            },
        }

        chart = Chart(options=options_kwargs, container=container)
        chart.add_series(*data)

        as_js_literal = chart.to_js_literal(f'./interactive_plots/rendering/{container}.js')

        return as_js_literal

    def correlation_scatterplot(self, max_conc):

        data_highcharts = []
        columns = list(self.df.columns)

        for i in range(len(columns) - 1):
            for k in range(1, len(columns) - i):
                scatter_data = []
                for j in range(len(self.df)):
                    scatter_data.append([self.df[columns[i]][j], self.df[columns[i + k]][j]])
                data_highcharts.append(
                    {"boostThreshold": 0, "name": f'{columns[i]}-{columns[i + k]}', "data": scatter_data, "type": 'scatter'})
        options_kwargs = {

            'title': {
                'text': 'Scatterplot of parameters'
            },

            'legend': {
                'enabled': True
            },

            'xAxis': {
                'min': 0,
                'max': max_conc,
                'title': {
                    'text': f'Concentrations ({self.unit})'
                }
            },

            'yAxis': {
                'min': 0,
                'max': max_conc,
                'tickInterval': 1,
                'title': {
                    'text': f'Concentrations ({self.unit})'
                }
            },
            'chart': {
                'type': 'scatter',
            },
        }
        chart = Chart(options=options_kwargs, container='correlation_scatterplot')
        chart.add_series(*data_highcharts)

        as_js_literal = chart.to_js_literal('./interactive_plots/rendering/correlation_scatterplot.js')

        return as_js_literal

    def count_datapoints_timeseries(self):

        series = [LineSeries.from_pandas(self.df, property_map={'y': 'count', 'x': 'date'}, series_kwargs={'name': 'VMM groundwater'})]

        options_kwargs = {
            'chart': {
                'zooming': {
                    'key': 'shift',
                    'type': 'x'
                },
              },
            'title': {
                'text': 'Count of datapoints'
            },

            'legend': {
                'enabled': True
            },

            'xAxis': {
                'type': 'datetime',
                'title': {
                    'text': 'Date'
                }
            },

            'yAxis': {
                'title': {
                    'text': 'Count'
                }
            }
        }

        chart = Chart(options=options_kwargs, container='count_datapoints_timeseries')
        chart.add_series(*series)

        as_js_literal = chart.to_js_literal('./interactive_plots/rendering/count_datapoints_timeseries.js')

        return as_js_literal


if __name__ == '__main__':

    input_df = pd.read_csv('from-pandas.csv')
    highcharts = Highcharts(input_df)

    highcharts.boxplot()
