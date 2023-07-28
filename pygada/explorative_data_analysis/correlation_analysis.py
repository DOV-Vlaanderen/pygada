import math

import numpy as np
import pandas as pd
from loguru import logger
from matplotlib import pyplot as plt
import seaborn as sns
# Import classes using precise module indications. For example:
from pygada.explorative_data_analysis.interactive_plots.highcharts import Highcharts


class CorrelationSD:

    def __init__(self, inputdf, parameters, type=None):
        """Initialize the class.

        Parameters
        ----------
        inputdf : dataframe
            The input dataframe.
        parameters : list
            The chosen variables.
        type : str
            The chosen output for figures. Static or dynamic.

        Returns
        -------
        None"""

        self.type = type


        df = inputdf[['index', 'parameter', 'value']]  # todo: check if index is correct

        df = df.pivot(index='index', columns='parameter', values='value')
        df = df[parameters]
        df = np.log(df[:]).replace(np.NINF, np.nan)  # todo: check if necessary

        unit = inputdf['unit'].unique()[0]

        self.df = df
        self.unit = unit
        self.parameters = parameters

    def heatmap(self):
        """Create a correlation heatmap with every parameter that is in the dataset.
        The plot can be saved as a png file.

        Returns
        -------
        None
        """

        logger.info(f"Start the correlation matrix of the dataset.")

        df1_correlation = self.df.corr().round(2)

        df_cor_nb = pd.DataFrame(np.nan, index=self.parameters, columns=self.parameters)
        for i in range(len(self.parameters)):
            for j in range(len(self.parameters)):
                df_count = self.df.dropna(subset=[self.parameters[i], self.parameters[j]])
                df_cor_nb.loc[self.parameters[i], self.parameters[j]] = int(len(df_count))

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

            heatmap = sns.heatmap(df_cor_nb, annot=True, fmt='g', vmin=0, vmax=max(df_cor_nb.max()))
            sns.set(font_scale=1)
            plt.tight_layout()
            plt.show()
            #if save:
            #    plt.savefig(f"{outputpath}/{parameter}_{transformation}_count_heatmap.png")
            plt.clf()

        elif self.type == 'dynamic':
            df1_correlation = df1_correlation.loc[:, df1_correlation.columns.notna()]  # todo: check if necessary
            highcharts = Highcharts(df1_correlation)
            highcharts.correlation_heatmap(container='correlation_heatmap', data_info='matrix', count=df_cor_nb)

    def scatterplot(self):
        """Create a scatter plot from every parameter that is in the dataset.
        The plot can be saved as a png file.

        Returns
        -------
        None
        """

        if self.type == 'static':
            scatter_matrix = pd.plotting.scatter_matrix(self.df, alpha=1, figsize=(10, 10))
            plt.tight_layout()
            plt.show()
            #if save:
            #    plt.savefig(f"{outputpath}/{parameter}_{transformation}_correlation_scatterplot_matrix.png")
            plt.clf()

        elif self.type == 'dynamic':
            df = self.df.dropna()
            #df = self.df.head(50)  # todo: plot not rendering with large amount of data.
            highcharts = Highcharts(df, self.unit)
            print(self.df.values.tolist())
            highcharts.correlation_scatterplot_matrix()


df = pd.read_csv('C:/Users/vandekgu/OneDrive - Vlaamse overheid - Office 365/Documenten/PycharmProjects/pygada/pygada/test_data/results/PFAS_gw_VMM.csv')

correlation_analysis = CorrelationSD(df, ['PFOS', 'PFHxS', 'PFNA', 'PFOA'], type='dynamic')
correlation_analysis.scatterplot()
