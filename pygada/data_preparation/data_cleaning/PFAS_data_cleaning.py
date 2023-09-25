import os
import numpy as np
from pygada.data_preparation.data_cleaning.general_data_cleaning import DataCleaning
import pandas as pd


def soil(inputfile, source, save=True):
    """
    Clean the soil dataset and report the overview in a metadata file.
    Each type of error is added as a new attribute to the error dataframe. \n
    Check for:\n
    - date
    - sum parameter
    - detection condition
    - unit
    - top
    - basis
    Perform some extra manipulations: \n
    - Some parameters are replaced by their synonym.
    - The date is transformed to the datetime type
    Ultimately, the clean and error result can be saved as separate text files.

    Parameters
    ----------
    inputfile: text file
        The input dataset.
    source: str
        The data source.
    save: Boolean
        The option to save the cleaned and error dataset as separate text files.

    Returns
    -------
    df_error: dataframe
        The dataframe containing the errors.
    df_result: dataframe
        The cleaned dataframe without the errors.
    metadata: json
        A json object containing the amount of each error (# and %).
    """

    df = pd.read_csv(inputfile, sep=';')

    df = df.rename(columns={'datum': 'date', 'detectieconditie': 'detection_condition', 'meetwaarde': 'value', 'meeteenheid': 'unit', 'bron': 'source', 'top_in_m': 'top_m_mv', 'basis_in_m': 'basis_m_mv'})
    original_columns = df.columns.values.tolist()
    df_error = pd.DataFrame(columns=original_columns)

    data_cleaning = DataCleaning(df)
    df_error_date = data_cleaning.date('date')
    df_error = df_error.merge(df_error_date, how='outer', on=original_columns)
    #df_error_sum_parameters = data_cleaning.sum_parameter('parameter', ['totaal PFAS indicatief', 'totaal PFAS', 'totaal PFAS kwantitatief', 'PFAS Som kwantitatief', 'PFAS Som indicatief', 'PFAS totaal (Kwantitatief en indicatief)', 'EFSA-4'])
    #df_error = df_error.merge(df_error_sum_parameters, how='outer', on=original_columns)
    df_error_dc = data_cleaning.detection_condition('detection_condition', ['=', '<'])
    df_error = df_error.merge(df_error_dc, how='outer', on=original_columns)
    df_error_unit = data_cleaning.unit('unit', ['mg/kg ds', 'µg/kg ds'])
    df_error = df_error.merge(df_error_unit, how='outer', on=original_columns)
    df_error_top = data_cleaning.top('top_m_mv')
    df_error = df_error.merge(df_error_top, how='outer', on=original_columns)
    df_error_basis = data_cleaning.basis('basis_m_mv')
    df_error = df_error.merge(df_error_basis, how='outer', on=original_columns)
    metadata = data_cleaning.meta(len(df_error), source, 'soil', save)

    df_error_2 = df_error[original_columns]
    df_result = pd.concat([df, df_error_2]).drop_duplicates(keep=False)

    df_result['parameter'] = df_result['parameter'].replace({'som PFOA': 'PFOAtotal', 'som PFOS': 'PFOStotal', 'ADONA': 'DONA'})
    df_result['date'] = pd.to_datetime(df_result['date'])

    if save:
        path = os.getcwd()
        path1 = f"{path}/results"
        if not os.path.exists(path1):
            os.mkdir(f"{path}/results")
        df_error.to_csv(f'results/PFAS_{source}_soil_error.txt', encoding='utf-8-sig')
        df_result.to_csv(f'results/PFAS_{source}_soil_result.txt', encoding='utf-8-sig')

    return df_error, df_result, metadata


def groundwater(inputfile, source, save=True):
    """
    Clean the groundwater dataset and report the overview in a metadata file.
    Add each type of error as a new attribute to the error dataframe. \n
    Check for:\n
    - date
    - sum parameter
    - detection condition
    - unit
    - top
    - basis
    Perform some extra manipulations: \n
    - Empty detection conditions are replaced by '='
    - Some parameters are replaced by their synonym.
    - The date is transformed to the datetime type
    Ultimately, the clean and error result can be saved as separate text files.

    Parameters
    ----------
    inputfile: text file
        The input dataset.
    source: str
        The data source.
    save: Boolean
        The option to save the cleaned and error dataset as separate text files.

    Returns
    -------
    df_error: dataframe
        The dataframe containing the errors.
    df_result: dataframe
        The cleaned dataframe without the errors.
    metadata: json
        A json object containing the amount of each error (# and %).
    """

    df = pd.read_csv(inputfile, sep=';')

    df = df.rename(columns={'datum': 'date', 'detectieconditie': 'detection_condition', 'meetwaarde': 'value', 'meeteenheid': 'unit', 'bron': 'source', 'top_in_m': 'top_m_mv', 'basis_in_m': 'basis_m_mv'})
    original_columns = df.columns.values.tolist()
    df_error = pd.DataFrame(columns=original_columns)

    data_cleaning = DataCleaning(df)
    df_error_date = data_cleaning.date('date')
    df_error = df_error.merge(df_error_date, how='outer', on=original_columns)
    #df_error_sum_parameters = data_cleaning.sum_parameter('parameter', ['EU DWRL-20', 'EFSA-4', 'PFAS Som kwantitatief', 'PFAS Som indicatief', 'PFAS totaal (Kwantitatief en indicatief)', 'som PFAS kwantitatief', 'som PFAS indicatief', 'totaal PFAS'])
    #df_error = df_error.merge(df_error_sum_parameters, how='outer', on=original_columns)
    df_error_dc = data_cleaning.detection_condition('detection_condition', ['=', '<', np.nan])
    df_error = df_error.merge(df_error_dc, how='outer', on=original_columns)
    df_error_unit = data_cleaning.unit('unit', ['ng/l', 'µg/l'])
    df_error = df_error.merge(df_error_unit, how='outer', on=original_columns)
    df_error_top = data_cleaning.top('top_m_mv')
    df_error = df_error.merge(df_error_top, how='outer', on=original_columns)
    df_error_basis = data_cleaning.basis('basis_m_mv')
    df_error = df_error.merge(df_error_basis, how='outer', on=original_columns)
    metadata = data_cleaning.meta(len(df_error), source, 'groundwater', save)

    df_error_2 = df_error[original_columns]
    df_result = pd.concat([df, df_error_2]).drop_duplicates(keep=False)

    df_result['detection_condition'] = df_result['detection_condition'].replace(np.nan, '=')
    df_result['parameter'] = df_result['parameter'].replace({'som PFOA': 'PFOAtotal',
                                                             'som PFOS': 'PFOStotal',
                                                             'ADONA': 'DONA',
                                                             'PFOA vertakt': 'PFOAbranched',
                                                             'PFOS vertakt': 'PFOSbranched',
                                                             'PFOS lineair': 'PFOS',
                                                             'PFOA lineair': 'PFOA'})
    df_result['date'] = pd.to_datetime(df_result['date'])

    if save:
        path = os.getcwd()
        path1 = f"{path}/results"
        if not os.path.exists(path1):
            os.mkdir(f"{path}/results")
        df_error.to_csv(f'results/PFAS_{source}_groundwater_error.txt', encoding='utf-8-sig')
        df_result.to_csv(f'results/PFAS_{source}_groundwater_result.txt', encoding='utf-8-sig')

    return df_error, df_result, metadata


if __name__ == '__main__':
    soil('../../datasets/PFAS/PFAS_data_OVAM_bodem.csv', 'OVAM', save=True)
    groundwater('../../datasets/PFAS/PFAS_data_OVAM_grondwater.csv', 'OVAM', save=True)

