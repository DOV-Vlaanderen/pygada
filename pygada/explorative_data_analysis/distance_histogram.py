import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.spatial import distance
from collections import Counter

# Import classes using precise module indications. For example:
from pygada.explorative_data_analysis.interactive_plots.highcharts import Highcharts

def distance_histogram(df, type):

    coords_array, x2, y2, distances = [], [], [], []

    for i in df["x"].values.tolist():
        x2.append(i.replace(",", "."))
    for i in df["y"].values.tolist():
        y2.append(i.replace(",", "."))

    for i in range(len(df)):
        coords_array.append([float(x2[i]), float(y2[i])])

    distance1 = distance.cdist(coords_array, coords_array, "euclidean")
    for i in range(len(df)):
        for j in range(len(df)):
            if j > i:
                distances.append(distance1[i][j])
    distances = sorted(distances)

    if type == 'static':
        histogram = sns.histplot(data=distances, bins=100)
        histogram.set_xlabel("Distance (m)")
        histogram.set_ylabel("Count")
        plt.show()
        plt.clf()

    if type == 'dynamic':

        # Histogram function of Highcharts does not work for a large number of data
        hist, bin_edges = np.histogram(distances, bins=100)
        bin_edges_mean = []
        bin_edges_label = []
        for i in range(len(bin_edges) - 1):
            bin_edges_mean.append((bin_edges[i] + bin_edges[i + 1]) / 2)
            bin_edges_label.append(f'{round(bin_edges[i])}m - {round(bin_edges[i + 1])}m')
        df = pd.DataFrame({'count': hist, 'bin_mean': bin_edges_mean, 'bin_edges': bin_edges_label})

        highcharts = Highcharts(df)
        highcharts.column_plot()

df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')
distance_histogram(df, type='static')