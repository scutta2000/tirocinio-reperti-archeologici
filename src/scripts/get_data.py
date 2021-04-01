import pandas as pd
from pathlib import Path


def ceramiche_DB():
    path = Path(__file__).parent.parent / 'dati_ceramiche_classi.xlsx'
    tarquina = pd.read_excel(path, index_col=0, usecols=[
                             0, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    non_tarquina = pd.read_excel(path, index_col=0, usecols=[
                                 0, 2, 3, 4, 5, 6, 7, 8, 9, 10], sheet_name=1)

    X = pd.concat([tarquina, non_tarquina])
    y = [1]*len(tarquina) + [0]*len(non_tarquina)

    return X, y


def da_classificare_DB():
    path = Path(__file__).parent.parent / 'dati_ceramiche_da_classificare.xlsx'
    db = pd.read_excel(path, index_col=0, usecols=[
        0, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    return db
