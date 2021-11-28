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


def ceramiche_no_ripetizioni_DB(ripetizioni=False):
    # ripetizioni:
    #   False -> X, y solo una copia
    #   True -> X_singolo, X_ripetuto, y_singolo, y_ripetuto

    path = Path(__file__).parent.parent / \
        'dati_ceramiche_classi_no_ripetizioni.xlsx'
    tarquina = pd.read_excel(path, index_col=0, usecols=[
                             0, 2, 3, 4, 5, 6, 7, 8, 9, 10], engine="openpyxl")

    non_tarquina = pd.read_excel(path, index_col=0, usecols=[
                                 0, 2, 3, 4, 5, 6, 7, 8, 9, 10], sheet_name=1, engine="openpyxl")
    if not ripetizioni:
        X = pd.concat([tarquina, non_tarquina])
        y = [1]*len(tarquina) + [0]*len(non_tarquina)

        return X, y
    else:
        tarquina_ripetuto = pd.read_excel(path, index_col=0, usecols=[
            0, 2, 3, 4, 5, 6, 7, 8, 9, 10], sheet_name=2)

        non_tarquina_ripetuto = pd.read_excel(path, index_col=0, usecols=[
            0, 2, 3, 4, 5, 6, 7, 8, 9, 10], sheet_name=3)

        X_singolo = pd.concat([tarquina, non_tarquina])
        y_singolo = [1]*len(tarquina) + [0]*len(non_tarquina)

        X_ripetuto = pd.concat([tarquina_ripetuto, non_tarquina_ripetuto])
        y_ripetuto = [1]*len(tarquina_ripetuto) + \
            [0] * len(non_tarquina_ripetuto)

        return X_singolo, X_ripetuto, y_singolo, y_ripetuto


def da_classificare_DB():
    path = Path(__file__).parent.parent / 'dati_ceramiche_da_classificare.xlsx'
    db = pd.read_excel(path, index_col=0, usecols=[
        0, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    return db


def unified_DB():
    # Ritorna le X del database classificato + database non classificat
    x1, _ = ceramiche_DB()
    x2 = da_classificare_DB()
    return pd.concat([x1, x2])
