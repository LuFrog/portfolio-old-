#%%

import keras
#from tensorflow import keras
from classification_models.keras import Classifiers

ResNet50, preprocess_input = Classifiers.get('resnet50')

import numpy as np
from cv2 import cv2
import random
from traitement.modif_img import resize_image
import os
from traitement.train_test import trains

base_model = ResNet50(input_shape=(250,250,3), weights='imagenet', include_top=False)
print(base_model.output)
x = keras.layers.GlobalAveragePooling2D()(base_model.output)
#output = keras.layers.Dense(7, activation='softmax')(x)
model = keras.models.Model(inputs=[base_model.input], outputs=[x])


print(model.output.shape)

#%%
top_model = keras.models.Sequential()
top_model.add(keras.layers.Dense(7,activation="softmax",input_shape=(2048,)))


(x_train,y_train),(x_test,y_test),dico = trains("./Dataset/Dataset4")

print(x_train.shape)

x_train_2 = model.predict(x_train)
x_test_2 = model.predict(x_test)

print(x_train_2.shape)

top_model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

top_model.fit(x=x_train_2, y=y_train, epochs=10)

#%%
top_model.save('new_model_10_ep_resnet50.model')

#%%
val_loss, val_acc = top_model.evaluate(x_test_2, y_test)
print(f'Validation loss: {val_acc}, Validation accuracy: {val_acc}')


# %%
