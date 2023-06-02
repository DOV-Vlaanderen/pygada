from highcharts_core.chart import Chart
from highcharts_core.options.series.area import LineSeries
from highcharts_core.options.series.boxplot import BoxPlotSeries

# Create a new LineSeries instance from the CSV file "some-csv-file.csv".
my_series = LineSeries.from_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv',
                                property_column_map = {
                                    'x': 0,
                                    'y': 3,
                                    'id': 'id'
                                })