# Recyclotron

Ce projet vise à améliorer le tri des déchets. On s'est tous déjà posé la question : "Mais dans quelle poubelle va ce déchet ?". Que ce soit les bouteilles en plastique, ou les boites d'oeufs en carton, chaque déchet doit trouver sa place pour être ou non recycler. Mais encore faut-il savoir dans quel poubelle la mettre afin d'éviter le "recycling contamination"?

L'application développée indique, pour chaque déchet, la voie de recyclage appropriée, grâce à la reconnaissance visuelle.
Prenez une photo du déchet que vous voulez trier et cette application vous dira dans quelle poubelle il va. 

## Pour commencer

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prérequis

What things you need to install the software and how to install them
Les modules à installer pour exécuter notre programme :
-keras
-os
-opencv-python  
-numpy
-random
-skimage
-argparse
-time

Nous vous recommandons d'utiliser le package pip pour installer.



```bash 
pip install keras
pip install opencv-python
pip install os
```
Les importations sont déjà écrites dans les codes qui y font appel.



### Installation

A step by step series of examples that tell you how to get a development env running

Say what the step will be

Step 1 : Télécharger le [dataset2] https://gitlab-cw2.centralesupelec.fr/2019afriatg/recyclotron/tree/master/Dataset2
Ce dataset n'est pas nécessaire pour executer le programme mais poeut vous être utile si vous voulez développer d'avatnge l'application ou enrichir la database.

Step 2 : Télécharger le programme [fichieràfaire]

Step 3 : Si application mobile
```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Comment utiliser le logiciel ?

Explain how to run the automated tests for this system


## Auteurs

* **BLANCHOZ--RHÔNE Clément** - *Initial work* - [ClemnetBlanchoz]https://gitlab-cw2.centralesupelec.fr/2019blanchozc
* **DURANTON Lucie** - *Initial work* - [LucieDuranton]https://gitlab-cw2.centralesupelec.fr/2019durantonl
* **AFRIAT Gabriel** - *Initial work* - [GabrielAfriat]https://gitlab-cw2.centralesupelec.fr/2019afriatg
* **MUHLMANN HOLANDA Bruno** - *Initial work* - [BrunoMuhlman]https://gitlab-cw2.centralesupelec.fr/brunomuho
* **RYCKELYNCK Lucas** - *Initial work* - [LucasRyckelynck]https://gitlab-cw2.centralesupelec.fr/2019ryckelynl
* **FROGER Luca** - *Initial work* - [LucaFroger]https://gitlab-cw2.centralesupelec.fr/2019frogerl


## Remerciements

* Robin, notre inspirateur des jours perdus, notre rocher au milieu de la tempête, merci de ton aide précieuse
* Gui, sans lui rien n'aurait été possible

## Commandes à taper

* conda install fastai pytorch=1.1.0 -c fastai -c pytorch -c conda-forge


## Potentielle améliroation du projet 
Cette application pourra être combinée à une poubelle pour en faire une poubelle connectée.