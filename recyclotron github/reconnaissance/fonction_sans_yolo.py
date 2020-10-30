from reconnaissance.reconnaissance_dechets import *
from traitement.modif_img import *
from cv2 import cv2

def reconnaissance_sans_yolo(img):

    # x=int(img.shape[0]/10)
    # y = int(img.shape[1]/10)
    # img = resize_image(img,(x,y))

    img2 = resize_image(img, (250,250))
    text = reconnaissance_d2(img2)
    x,y = img.shape[0],img.shape[1]
    police = x/550
    l = text.split()
    if l[3] == 'verte':
        color = (0,200,0)
    if l[3] == 'jaune':
        color = (0,215,255)
    if l[3] == 'marron':
        color = (17,60,91)
    if l[3] == 'piles':
        color = (198,162,142)
    res = cv2.putText(img, text, (int(x/30),int(0.5*y)), cv2.FONT_HERSHEY_SIMPLEX,police, color, 2)
    return res

# img = cv2.imread('/Users/gabrielafriat/Desktop/bouteille_eau.png')
# img = reconnaissance_sans_yolo(img)

# # cv2.imshow('img',img)
# # cv2.waitKey(0)
