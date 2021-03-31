# # Obbiettivo
#
# Primo test per verificare se un NN può essere efficace per risolvere il problema.
#
# # Risultati
#
# Ottenuti buoni risultati ~95% accuratezza, i NN sono una strada plausibile

from numpy.random import seed
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from .get_data import ceramiche_DB
import pandas as pd

seed(42)

X, y = ceramiche_DB()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.6, random_state=42, stratify=y)

clf = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)
clf.fit(X_train, y_train)


df = pd.DataFrame(confusion_matrix(y_test, clf.predict(X_test)))
df = df.rename(index={0: 'actual 0', 1: 'actual 1'})
df.to_latex('src/latex/test_iniziale.tex',
            header=['predicted 0', 'predicted 1'])
