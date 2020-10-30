#%%%
from keras.applications.vgg16 import VGG16
from tensorflow import keras
import numpy as np
from cv2 import cv2
import random
from traitement.modif_img import resize_image
import os
from traitement.train_test import trains

base_model = VGG16(weights = 'imagenet', include_top=False,input_shape=(250,250,3),pooling='avg')

# for layer in base_model.layers:
#     layer.trainable=False

top_model = keras.models.Sequential()
top_model.add(keras.layers.Dense(7,activation="softmax",input_shape=(512,)))


(x_train,y_train),(x_test,y_test),dico = trains("./Dataset/Dataset4")

print(x_train.shape)

x_train_2 = base_model.predict(x_train)
x_test_2 = base_model.predict(x_test)

print(x_train_2.shape)

top_model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

top_model.fit(x=x_train_2, y=y_train, epochs=10)

#%%
top_model.save('model_10_ep.model')

#%%
val_loss, val_acc = top_model.evaluate(x_test_2, y_test)
print(f'Validation loss: {val_acc}, Validation accuracy: {val_acc}')


# %%
