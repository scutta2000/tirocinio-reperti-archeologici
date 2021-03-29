# # Obbiettivo
#
# Primo test per verificare se un NN può essere efficace per risolvere il problema.
#
# # Risultati
#
# Ottenuti buoni risultati ~95% accuratezza, i NN sono una strada plausibile

from numpy.random import seed
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
from pathlib import Path
from pylatex import Document, Section
import numpy

seed(42)

doc = Document()

with doc.create(Section('Test iniziale neural networks')):
    pass

path = Path(__file__).parent.parent / 'dati_ceramiche_classi.xlsx'

tarquina = pd.read_excel(path, index_col=0, usecols=[
                         0, 2, 3, 4, 5, 6, 7, 8, 9, 10])

non_tarquina = pd.read_excel(path, index_col=0, usecols=[
                             0, 2, 3, 4, 5, 6, 7, 8, 9, 10], sheet_name=1)

X = pd.concat([tarquina, non_tarquina])
y = [1]*len(tarquina) + [0]*len(non_tarquina)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.6, random_state=42, stratify=y)


clf = SVC(gamma='auto')


clf = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)


clf.fit(X_train, y_train)


clf.score(X_test, y_test)


confusion_matrix(y_test, clf.predict(X_test))
