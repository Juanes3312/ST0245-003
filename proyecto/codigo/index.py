import urllib.request
import requests
import json
import os, sys

#solo llamar si no se tiene descargado 
def bajarEnfermo():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/enfermo_csv')
    repos = response.json()
    for i in repos:
        urllib.request.urlretrieve(i["download_url"], i["name"])
        a += 1

#solo llamar si no se tiene descargado.
def bajarSano():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/sano_csv')
    repos = response.json()
    for i in repos:
        urllib.request.urlretrieve(i["download_url"], i["name"])
        a += 1



direccion = "Poner aqui la direccion de la carpeta con los archivos de enfermos"
archivosEnfermo = os.listdir(direccion)

direccion = "Poner aqui la direccion de la carpeta con los archivos de sano"
archivosSano = os.listdir(direccion)

listaEnfermos = []
listaSano = []

for file in archivosEnfermo:
    listaEnfermos.append(file)

for file in archivosSano:
    listaSano.append(file)

def __main__():
    print(listaEnfermos)
    print(listaSano)

