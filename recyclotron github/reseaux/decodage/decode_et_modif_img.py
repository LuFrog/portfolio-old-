#%%
import numpy as np
from cv2 import cv2
import random
from traitement.modif_img import resize_image
import os
from traitement.train_test import trains
from reseaux.decodage.creation_lecture_fichiers_csv import *
from reseaux.decodage.affectation_poubelle import affectation

#from tensorflow import keras
from classification_models.keras import Classifiers


def decode_vect(vect):
    # print(vect)
    m = vect[0]
    ind = 0
    for i in range(len(vect)):
        if m<vect[i]:
            ind = i
            m = vect[i]
    dico = cvs_to_dico("dico.csv")
    # print(ind)
    return affectation(dico[ind])


# %%
