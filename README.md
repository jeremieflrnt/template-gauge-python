# Gauge avec Pyhton

Ce projet sert d'exemple pour commencer un projet d'automatisation de tests Selenium avec Gauge en Python.  

- [Gauge](https://github.com/getgauge/gauge)
- [Selenium](http://selenium-python.readthedocs.org/)

Cet outil permet un rendu plus lisible et une maintenance des tests plus facile.  
Il se base sur le langage Markdown pour écrire les Specifications / Scenarios qui correspondent respectivement à une suite de test (p. ex. une fonctionnalité à tester), et à un scénario de test (ou plus simplement à un test).  

Un test est un enchaînement de steps (ou étapes) qui représentent une action utilisateur.  
Chaque étape est écrite en français, pour être compréhensible facilement.  
Les steps sont de préférence le plus simple possible, pour faciliter leur réutilisation (p. ex. une step = saisir un texte sur un champ)  

# Liens docs Gauge

- [Docs](https://docsgaugeorg.readthedocs.io/en/master/index.html)
- [Concepts](https://docs.gauge.org/latest/writing-specifications.html#concept)
- [Specification](https://docs.gauge.org/latest/writing-specifications.html#specifications-spec), [Scenario](https://docs.gauge.org/latest/writing-specifications.html#longstart-scenarios) & [Step](https://docs.gauge.org/latest/writing-specifications.html#longstart-steps)

# Prérequis
- Python 3
- [Installer Gauge](https://docs.gauge.org/latest/installation.html)

- [Installer Gauge-Python plugin](https://gauge-python.readthedocs.io/en/latest/installation.html) en lançant  
```
gauge install python
pip3 install getgauge
```
- Google Chrome

# Execution des tests

## Set up
Il faut commencer par installer les dépendances :    
````
pip3 install -r requirements.txt
````

Vérifier [ici](http://chromedriver.storage.googleapis.com/index.html) qu'on a la bonne version de chromedriver par rapport à la version installée de chrome.  
Il faut si besoin la télécharger et la déposer correctement (path en fonction de la version et de l'OS) dans le dossier env/chrome/chromedriver.  
Mettre à jour la version dans le fichier env/chrome/browser.properties.  

## Lancer tous les tests
```
gauge run specs
```

## Lancer un test spécifiquement
Mettre le fichier de specs puis ":" puis le numéro de la ligne du test  
```
gauge run specs/demo.spec:4
```