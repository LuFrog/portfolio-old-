# import tensorflow.keras as keras
# import tensorflow as tf
import os
from cv2 import cv2
import numpy as np
from traitement.modif_img import resize_image
import random
import csv


def trains(repertoire):
    liste_dos = os.listdir(repertoire)
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    dico = {}
    ind = -1
    for dos in liste_dos:
        if dos[0] != '.':
            ind +=1
            dico[ind] = dos
            liste_fichiers = os.listdir(repertoire+'/'+dos)
            random.shuffle(liste_fichiers)
            n = len(liste_fichiers)
            p = int(0.8 * n)
            for k in range(p):
                if liste_fichiers[k][0] != '.':
                    img = cv2.imread(repertoire+'/'+dos+'/'+liste_fichiers[k])
                    try:
                        img = resize_image(img, (250,250))
                        x_train.append(img)
                        y_train.append(ind)
                    except:
                        continue
            for k in range(p,n):
                if liste_fichiers[k][0] != '.':
                    img = cv2.imread(repertoire+'/'+dos+'/'+liste_fichiers[k])
                    try:
                        img = resize_image(img, (250,250))
                        x_test.append(img)
                        y_test.append(ind)
                    except:
                        continue
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    return (x_train,y_train),(x_test,y_test),dico

