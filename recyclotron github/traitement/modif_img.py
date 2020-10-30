#%%
import numpy as np
from cv2 import cv2
import random as rd
import os
from skimage.transform import rotate, resize

def resize_image(img,new_dim):
    height, width = new_dim
    res = cv2.resize(img,(width, height), interpolation = cv2.INTER_CUBIC)    
    return res

def rotate_image(img,degree):
    rows,cols,a = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),degree,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst

def smoothing_image(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    return blur

def draw_rectangle(img,tlcorner,brcorner,color,line_thickness):
    img = cv2.rectangle(img,tlcorner,brcorner,color,1)
    return img

# temp = cv2.imread('/Users/gabrielafriat/Desktop/Coding_weeks_project/facerecognition/Data/tetris_blocks.png',1)
# tlcorner = (50,50)
# brcorner = (100,100)
# color = (0,0,255)
# line_thickness = 1

# img = draw_rectangle(temp,tlcorner,brcorner,color,line_thickness)
# img = resize_image()
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()

duracel='Dataset/Dataset2/battery/pile aa duracell0.png'

def enrichissement(dossier):
    i=0
    for image in os.listdir('./Dataset/Dataset2/'+dossier):
        if image[0]=='.':
            continue
        image='./Dataset/Dataset2/'+dossier+'/'+image
        res=[]
        image=cv2.imread(image)
        (H,W,a)=image.shape
        maxi=max([H,W])
        mini=min([H,W])
        d=((maxi-mini)/2)
        if maxi==H:
            image=np.pad(image,[(0, ), (int(d), ),(0,)],mode='edge')
        else:
            image=np.pad(image,[(int(d), ), (0, ),(0,)],mode='edge')
        for j in range(10):
            res.append(rotate(image,180*rd.random(),mode='edge',resize=True))
            res.append(smoothing_image(rotate(image,180*rd.random(),mode='edge',resize=True)))
        for element in res:
            i+=1
            # cv2.imshow("Image", element)
            # cv2.waitKey(0)
            element = (element*255).astype(np.uint8)
            cv2.imwrite('./Dataset/Dataset4/'+dossier+'/'+dossier+str(i)+'.jpg',element)

# print(enrichissement('cardboard'))
# print(enrichissement('plastic'))
# print(enrichissement('organic'))
# print(enrichissement('battery'))
# print(enrichissement('glass'))




# %%
