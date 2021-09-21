import urllib.request
import requests
import json
import os, sys, csv

#solo llamar si no se tiene descargado 
def bajarEnfermo():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/enfermo_csv')
    repos = response.json()
    for i in repos:
        ruta_destino = os.path.join("direccion de la carpeta enfermos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        a += 1

#solo llamar si no se tiene descargado 
def bajarSano():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/sano_csv')
    repos = response.json()
    for i in repos:
        ruta_destino = os.path.join("direccion de la carpeta sanos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        a += 1



direccion = "direccion de la carpeta enfermos"
archivosEnfermo = os.listdir(direccion)

direccion = "direccion de la carpeta sanos"
archivosSano = os.listdir(direccion)

listaEnfermos = []
listaSano = []

for file in archivosEnfermo:
    listaEnfermos.append(file)

for file in archivosSano:
    listaSano.append(file)







def __main__():
    #bajarSano()
    #bajarEnfermo()
    print(listaEnfermos)
    print(listaSano)

__main__()


