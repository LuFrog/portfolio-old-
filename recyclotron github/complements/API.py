# %%

from cv2 import cv2
import matplotlib.pyplot as plt
import shutil
import requests
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "da38641025e5497da211d887c77fb51e"

def rechercher(element, nom, nombre, repertoire):
    search_term = element
    client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))
    image_results = client.images.search(count=nombre, query=search_term)
    for i in range (len(image_results.value)):
        img = image_results.value[i]
        url = img.thumbnail_url
        response = requests.get(url, stream=True)
        with open(repertoire+nom+str(i)+'.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

# rechercher("bouteille plastique vide","bouteille vide", 40 ,"./Dataset2/plastic/")


# %%
