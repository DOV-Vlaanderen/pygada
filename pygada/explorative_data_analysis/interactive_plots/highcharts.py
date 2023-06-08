from highcharts_core.chart import Chart
from matplotlib.cbook import boxplot_stats
import pandas as pd


class Highcharts:

    def __init__(self, input_df, unit):

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
                "pointFormat": 'Concentration: {point.y} ' f'{self.unit}'
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
                    'text': f'Concentration in log {self.unit}'
                }
            }
        }
        chart = Chart(options=options_kwargs, container='boxplot')
        chart.add_series(*data)

        as_js_literal = chart.to_js_literal('./interactive_plots/rendering/boxplot.js')

        return as_js_literal


if __name__ == '__main__':

    input_df = pd.read_csv('from-pandas.csv')
    highcharts = Highcharts(input_df)

    highcharts.boxplot()
