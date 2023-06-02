import numpy as np
import pandas as pd
from highcharts_core.options.series.boxplot import BoxPlotSeries
from loguru import logger
from matplotlib import pyplot as plt
import seaborn as sns
# Import classes using precise module indications. For example:
from highcharts_core import highcharts
from interactive_plots.templates.highcharts import boxplot


def boxplots(inputdf, type=None, outputpath=None, save=False):
    """Create a box plot per parameter that is in the dataset. The y-scale contains the concentrations in log.
    The plot can be saved as a png file.

    Parameters
    ----------
    inputdf : dataframe
        The input dataframe.
    outputpath : str
        The folder where the results will be saved.
    save : Boolean
        The option to save the result.

    Returns
    -------
    None
    """

    logger.info(f"Plotting the box plot per parameter.")

    unit = inputdf['unit'].unique()[0]
    df = inputdf[['parameter', 'value']]

    if type == 'matplotlib':
        plt.figure(figsize=(20, 10))
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plot = sns.boxplot(x="parameter", y="value", data=df, color="lightblue")
        plot.set(ylim=0.01)
        plot.set(yscale="log")
        plot.set_xlabel("Parameter", fontsize=20)
        plot.set_ylabel(f"Value in log {unit}", fontsize=20)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
        # if save:
            # plt.savefig(f"{outputpath}/boxplot_parameters.png")
        plt.clf()

    elif type == 'highcharts':
        df = df.pivot(columns='parameter', values='value')
        df = df.loc[:, df.columns.notna()]
        boxplot(df)


df2 = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')
boxplots(df2, 'highcharts')


