#%%

import csv
from traitement.train_test import trains
import os
from cv2 import cv2
import numpy as np
import random

def dico_to_csv(dico, nom_fichier_csv):
    with open(nom_fichier_csv, 'w', newline='') as csvfile:
        mywriter = csv.writer(csvfile, delimiter=' ')
        for x in dico:
            mywriter.writerow([str(x),dico[x]])
 
def cvs_to_dico(nom_fichier_csv):
    dico = {}
    with open('./reseaux/decodage/dico.csv', newline='') as f:
        reader = csv.reader(f,delimiter = " ")
        for row in reader:
            dico[int(row[0])] = row[1]
    return dico


# %%
