import numpy as np
import pandas as pd
from loguru import logger
from matplotlib import pyplot as plt
import seaborn as sns
# Import classes using precise module indications. For example:
from pygada.explorative_data_analysis.interactive_plots.highcharts import Highcharts


class CorrelationSD:

    def __init__(self, inputdf, type=None):

        self.inputdf = inputdf
        self.type = type

    def heatmap(self):
        """Create a correlation heatmap with every parameter that is in the dataset.
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

        logger.info(f"Start the correlation matrix of the dataset.")

        df = self.inputdf[['index', 'parameter', 'value']]  # todo: check if index is correct
        df = df.pivot(index='index', columns='parameter', values='value')
        df = df[['PFOS', 'PFHxS', 'PFNA', 'PFOA']]
        df = np.log(df[:]).replace(np.NINF, np.nan)  # todo: check if necessary

        df1_correlation = df.corr().round(2)

        if self.type == 'static':
            plt.figure(figsize=(10, 10))

            heatmap = sns.heatmap(df1_correlation, vmin=0, vmax=1, annot=True)
            heatmap.set_title(f"correlation heatmap")
            sns.set(font_scale=3)
            plt.tight_layout()
            plt.show()
            #if save:
            #    plt.savefig(f"{outputpath}/{parameter}_{transformation}_correlation_heatmap.png")
            plt.clf()

        elif self.type == 'dynamic':
            df1_correlation = df1_correlation.loc[:, df1_correlation.columns.notna()]  # todo: check if necessary
            highcharts = Highcharts(df1_correlation)
            highcharts.correlation_heatmap()

df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')

correlation_analysis = CorrelationSD(df, type='dynamic')
correlation_analysis.heatmap()
