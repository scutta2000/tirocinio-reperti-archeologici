# Report

* Test iniziale con valori di default di scikit-learn, risultato inaspettatamente buono: accuratezza ~97%

* Test meta parametri per MLPClassifier

* Grid search da risultati variabili da run a run quindi l'ho eseguito piu` volte analizzando i risultati ottenuti

* Nested cross validation per valutare il modello separando correttamente traing e testing set

* Test iniziale di learning non supervisionato per il dataset non classificato, risultati promettenti

* Confronto con nested CV di vari tecniche di classificazione supervisionata, risultati buoni soprattuto per `naive bayes`

* test nn con 2 hidden layer, risultati sostanzialmente uguali

* i modelli non supervisionati funzionano rimuovendo dal database le ripetizioni ma meno bene









---

# Risorse usate

* [1.17. Neural network models (supervised) &mdash; scikit-learn 0.24.1 documentation](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)

* [Nested versus non-nested cross-validation &mdash; scikit-learn 0.24.1 documentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

* [2. Unsupervised learning &mdash; scikit-learn 0.24.1 documentation](https://scikit-learn.org/stable/unsupervised_learning.html)