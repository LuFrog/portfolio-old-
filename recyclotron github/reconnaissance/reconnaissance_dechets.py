#%%
import keras
import numpy as np
from cv2 import cv2
import random
from traitement.modif_img import resize_image
import os
from traitement.train_test import trains
from reseaux.decodage.creation_lecture_fichiers_csv import *
from reseaux.decodage.decode_et_modif_img import *

#from tensorflow import keras
from classification_models.keras import Classifiers

ResNet50, preprocess_input = Classifiers.get('resnet50')


base_model = ResNet50(input_shape=(250,250,3), weights='imagenet', include_top=False)
x = keras.layers.GlobalAveragePooling2D()(base_model.output)
model = keras.models.Model(inputs=[base_model.input], outputs=[x])

top_model = keras.models.load_model('./reseaux/sauvegardes/new_model_10_ep_resnet50.model')

# img = cv2.imread('IMG_3385.jpeg')

# img = resize_image(img,(250,250))

# res = model.predict(np.array([img]))

# pred = top_model.predict(res)

# print(decode_vect(pred))
# %%

# prend en entrée une image (en jpg)
def reconnaissance_d(image):
    img = cv2.imread(image)
    img = resize_image(img,(250,250))
    res = model.predict(np.array([img]))
    pred = top_model.predict(res)
    return decode_vect(pred[0])

# prend en entrée une image sous forme de matrice
def reconnaissance_d2(image_traitee):
    res = model.predict(np.array([image_traitee]))
    pred = top_model.predict(res)
    return decode_vect(pred[0])
# print(reconnaissance('/Users/gabrielafriat/Desktop/verre_crous.jpeg'))

# %%
