#el metodo comprimir  solo funciona si esta dentro de la carpeta de archivos se solucionara mas adelante
import requests
import urllib.request
import json
import os
import sys
import cv2

#solo llamar si no se tiene descargado 
def bajarEnfermo():
    #a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/enfermo')
    repos = response.json()
    for i in repos:
        ruta_destino = os.path.join("Direccion donde se guardan los enfermos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        #a += 1

#solo llamar si no se tiene descargado 
def bajarSano():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/sano')
    repos = response.json()
    for i in repos:
        ruta_destino = os.path.join("Direccion donde se guardan los sanos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        a += 1




direccionEnfermo = "Direccion de la carpeta enfermos"
archivosEnfermo = os.listdir(direccionEnfermo)

direccionSano = "Direccion de la carpeta sanos"
archivosSano = os.listdir(direccionSano)


def comprimirEnfermo(archivos):
    contador = 0
    for line in archivos:
        if line.endswith('.webp'):
            continue
        elif line.endswith('.gif'):
            continue
        elif line.endswith('.py'):
            continue
        else:
            print("else")
            img = cv2.imread(line)
            scale_percent = 0.50
            width = int(img.shape[1]*scale_percent)
            heigth = int(img.shape[0]*scale_percent)
            dimension=(width,heigth)
            resized=cv2.resize(img,dimension,interpolation=cv2.INTER_CUBIC)
            ruta_destino = os.path.join("En que carpeta quiere que se guarden las imagenes comprimidas", 'comprimido_'+line)
            cv2.imwrite(ruta_destino, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

def comprimirSano(archivos):
    contador = 0
    for line in archivos:
        if line.endswith('.webp'):
            continue
        elif line.endswith('.gif'):
            continue
        elif line.endswith('.py'):
            continue
        else:
            print("else")
            img = cv2.imread(line)
            scale_percent = 0.50
            width = int(img.shape[1]*scale_percent)
            heigth = int(img.shape[0]*scale_percent)
            dimension=(width,heigth)
            resized=cv2.resize(img,dimension,interpolation=cv2.INTER_CUBIC)
            ruta_destino = os.path.join("En que carpeta quiere que se guarden las imagenes comprimidas", 'comprimido_'+line)
            cv2.imwrite(ruta_destino, resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



listaEnfermos = []
listaSano = []
for file in archivosEnfermo:
    listaEnfermos.append(file)
for file in archivosSano:

    listaSano.append(file)







def __main__():
    #bajarEnfermo()
    #bajarSano()
    #print(listaEnfermos)
    #print(listaSano)
    comprimirEnfermo(direccionEnfermo)
    comprimirSano(direccionSano)


__main__()


