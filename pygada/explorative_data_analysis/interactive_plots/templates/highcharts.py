from highcharts_core.chart import Chart
from matplotlib.cbook import boxplot_stats
import pandas as pd


def boxplot(df):

    boxplot = boxplot_stats(df)
    boxplot = pd.DataFrame(boxplot).drop(['mean', 'iqr', 'cilo', 'cihi', 'fliers'], axis=1)
    whishi = boxplot.pop('whishi')
    boxplot.insert(4, 'whishi', whishi)
    boxplot = boxplot.transpose().set_axis(list(df.columns.values), axis=1)

    columns = list(boxplot.columns)
    data = list(boxplot[x].values.tolist() for x in columns)
    series = [{
        "name": "Observations",
        "data": data,
        "type": 'boxplot'}]

    options_kwargs = {
        'title': {
            'text': 'Highcharts Box Plot Example'
        },

        'legend': {
            'enabled': True
        },

        'xAxis': {
            'categories': columns,
            'title': {
                'text': 'Experiment No.'
            }
        },

        'yAxis': {
            'title': {
                'text': 'Observations'
            }
        }
    }

    chart = Chart(options=options_kwargs)
    chart.add_series(*series)

    as_js_literal = chart.to_js_literal('test2.js')

    return as_js_literal

