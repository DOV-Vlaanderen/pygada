import pandas as pd
from loguru import logger
from matplotlib import pyplot as plt
import seaborn as sns
# Import classes using precise module indications. For example:
from pygada.explorative_data_analysis.interactive_plots.highcharts import Highcharts


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
    df = inputdf[['index', 'parameter', 'value']]  # todo: check if index is correct

    if type == 'static':
        plt.figure(figsize=(20, 10))
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plot = sns.boxplot(x="parameter", y="value", data=df, color="lightblue")
        plot.set(ylim=0.01)
        plot.set(yscale="log")
        plot.set_xlabel("Parameter", fontsize=20)
        plot.set_ylabel(f"Concentrations in log {unit}", fontsize=20)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
        # if save:
            # plt.savefig(f"{outputpath}/boxplot_parameters.png")
        plt.clf()

    elif type == 'dynamic':
        df = df.pivot(index='index', columns='parameter', values='value')
        df = df.loc[:, df.columns.notna()]
        highcharts = Highcharts(df, unit)
        highcharts.boxplot()


df2 = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')
boxplots(df2, 'dynamic')
