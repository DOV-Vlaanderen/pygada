from loguru import logger
import matplotlib as plt
import seaborn as sns

def boxplots(inputdf, save=False):
    """Create a box plot per parameter that is in the dataset. The y-scale contains the concentrations in log.
    The plot can be saved as a png file.

    Parameters
    ----------
    inputdf : dataframe
        The input dataframe.

    Returns
    -------
    None
    """

    plt.figure(figsize=(20, 10))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plot = sns.boxplot(x="parameter", y="meetwaarde", data=inputdf, color="lightblue")
    plot.set(ylim=0.01)
    plot.set(yscale="log")
    plot.set_xlabel("Parameter", fontsize=20)
    plt.xticks(rotation=90)
    plt.tight_layout()
    if save:
        plt.savefig(f"{outputpath}/boxplots/boxplot_parameters_{parameter}.png")
    plt.clf()

    logger.info(f"Plotting the box plot per parameter.")

def plot_dataset(self, inputdf=pd.DataFrame, outputpath=str, parameter=str, source=str, max_value=float):
    """Create a box plot per parameter that is in the dataset. The y-scale with the concentrations is in log.
    The plot is saved as a png file.

    :param inputdf: The input dataframe.
    :param outputpath: Part of the path where the user want to store the result png.
    :param parameter: The chosen parameter(s), it/they are part of the path to the result png.
    :param source: The source from where the data comes from.
    :param max_value: The maximum value of the concentration of the parameters in the dataset.
    :return: None.
    """

    logger.info(f"Start plotting the box plot per parameter.")

    df = inputdf
    if source == "VMM":
        parameters = ['Temperatuur (veldmeting)', 'Geleidingsvermogen 20°C', 'Geleidingsvermogen 20Â°C',
                      'Zuurgraad pH (veldmeting)']
        for i in parameters:
            df = df[df["parameter"] != i]
    if source == 'pydov':
        df = df.rename(columns={"waarde": "meetwaarde"})

    plt.figure(figsize=(20, 10))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plot = sns.boxplot(
        x="parameter", y="meetwaarde", data=df, color="lightblue"
    )
    plot.set(ylim=(0.01, max_value))
    plot.set(yscale="log")
    #todo: change ylabel to unit from input data.
    if source == "pydov":
        plot.set_xlabel("Parameter", fontsize=20)
        plot.set_ylabel("Concentration", fontsize=20)
    if (source == "VMM") | (source == "gw_OVAM"):
        plot.set_xlabel("Parameter", fontsize=20)
        plot.set_ylabel("Concentration (ng/l)", fontsize=20)
    if source == "soil_OVAM":
        plot.set_xlabel("Parameter", fontsize=20)
        plot.set_ylabel("Concentration (ng/kg ds)", fontsize=20)

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f"{outputpath}/boxplots/boxplot_parameters_{parameter}.png")
    plt.clf()
