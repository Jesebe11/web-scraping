import requests
from bs4 import BeautifulSoup
import urllib.request as urllib



def run():
    for i in range(1, 3):
        # se hace una peticion
        response = requests.get('https://xkcd.com/{}'.format(i))
        # se parsea la respuesta 
        soup = BeautifulSoup(response.content, 'html.parser')
        # se obtiene una referencia a la etiqueta de imagen
        image_container = soup.find(id='comic')
        # se obtiene la url del atributo src del image_container
        image_url = image_container.find('img')['src']
        # se obtiene una referencia al nombre de la imagen
        image_name = image_url.split('/')[-1]
        print('Descargando la imagen {}'.format(image_name))
        # se guarda la imagen 
        urllib.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == '__main__':
    run()