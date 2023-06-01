import pandas as pd
from loguru import logger
from matplotlib import pyplot as plt
import seaborn as sns

def boxplots(inputdf, outputpath=None, save=False):
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

    unit = inputdf['unit'].unique()[0]

    plt.figure(figsize=(20, 10))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plot = sns.boxplot(x="parameter", y="value", data=inputdf, color="lightblue")
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

    logger.info(f"Plotting the box plot per parameter.")

df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')
boxplots(df)
