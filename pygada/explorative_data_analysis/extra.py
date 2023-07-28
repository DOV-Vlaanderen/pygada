def count(self):
    """Create a correlation heatmap of the count of datapoints used do determine the correlation value.
    The plot can be saved as a png file.

    Returns
    -------
    None
    """

    df_cor_nb = pd.DataFrame(np.nan, index=self.parameters, columns=self.parameters)
    for i in range(len(self.parameters)):
        for j in range(len(self.parameters)):
            df_count = self.df.dropna(subset=[self.parameters[i], self.parameters[j]])
            df_cor_nb.loc[self.parameters[i], self.parameters[j]] = int(len(df_count))

    if self.type == 'static':


    elif self.type == 'dynamic':
        df_cor_nb = df_cor_nb.loc[:, df_cor_nb.columns.notna()]  # todo: check if necessary
        highcharts = Highcharts(df_cor_nb)
        highcharts.correlation_heatmap(container='correlation_heatmap_count', data_info='count matrix',
                                       max_df=max(df_cor_nb.max()))


def correlation_scatterplot(self, max_conc):

    data_highcharts = []
    columns = list(self.df.columns)
    count = -1
    for i in range(len(columns) - 1):

        for k in range(1, len(columns) - i):
            count += 1
            scatter_data = []
            for j in range(len(self.df)):
                scatter_data.append([self.df[columns[i]][j], self.df[columns[i + k]][j]])
            data_highcharts.append(
                {"boostThreshold": 0, "name": f'{columns[i]}-{columns[i + k]}', "data": scatter_data, "type": 'scatter', "color": self.color[count]})
    options_kwargs = {

        'title': {
            'text': 'Scatterplot of parameters'
        },

        'legend': {
            'enabled': True
        },

        'xAxis': {
            'min': 0,
            'max': max_conc,
            'title': {
                'text': f'Concentrations ({self.unit})'
            }
        },

        'yAxis': {
            'min': 0,
            'max': max_conc,
            'tickInterval': 1,
            'title': {
                'text': f'Concentrations ({self.unit})'
            }
        },
        'chart': {
            'type': 'scatter',
        },
    }
    chart = Chart(options=options_kwargs, container='correlation_scatterplot')
    chart.add_series(*data_highcharts)

    as_js_literal = chart.to_js_literal('./interactive_plots/rendering/correlation_scatterplot.js')

    return as_js_literal