from reconnaissance.fonction_yolo import *
from cv2 import cv2

# transforme la base de données en appliquant yolo
def traitement_yolo(repertoire):
    data = []
    liste = os.listdir(repertoire)
    for dos in liste:
        if dos[0]!=".":
            liste_fichiers = os.listdir(repertoire+'/'+dos)
            for fichier in liste_fichiers:
                if fichier[0]!=".":
                    print(repertoire+'/'+dos+'/'+fichier)
                    l_img = reconnaissance_transf(repertoire+'/'+dos+'/'+fichier)
                    print(l_img)
                    element = l_img[0]
                    if len(l_img)!=1:
                        print(len(l_img))
                    #element = (element*255).astype(np.uint8)
                    cv2.imwrite(repertoire+'/'+dos+'/'+fichier,element)

traitement_yolo('./Dataset/Dataset4')
