import urllib.request
import json
import os, sys, csv
import requests

#solo llamar si no se tiene descargado 
def bajarEnfermo():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/imagenes/color/enfermo')
    repos = response.json()
    for i in repos:
        ruta_destino = os.path.join("./imagenes_enfermos", i["name"])
        urllib.request.urlretrieve(i["download_url"], ruta_destino)
        a += 1

#solo llamar si no se tiene descargado.
def bajarSano():
    a = 0
    response = requests.get('https://api.github.com/repos/mauriciotoro/ST0245-Eafit/contents/proyecto/datasets/csv/sano_csv')
    repos = response.json()
    for i in repos:
        urllib.request.urlretrieve(i["download_url"], i["name"], 0,'./../sanos')
        a += 1
listaEnfermos = []
listaSano = []
vacaEnfermoFinal = []
listaSuprema =[]
tam = len(listaEnfermos)
for i in range(tam):
    vacaEnfermoFinal.append("vacaEnfermo" + str(i))



def convertirEnMatriz():
    carpeta = "./../prueba"
    archivos = os.listdir(carpeta)
    for archivo in archivos:
        nombre = []
        #assert os.path.isfile(archivo)
        archivo_destino = os.path.join("./../prueba", archivo)
        with open (archivo_destino, "r") as csv_file:
            #csv_reader = csv.reader(csv_file)
            for line in csv_file:
                vaca = [item.strip() for item in line.split(',')]
                nombre.append(vaca)
            listaSuprema.append(nombre)


direccion = "./enfermos"
archivosEnfermo = os.listdir(direccion)

direccion = "./sanos"
archivosSano = os.listdir(direccion)

def comprimir(nombre:str):
    img = cv2.imread(nombre)

    scale_percent = 0.15
    width = int(img.shape[1]*scale_percent)
    heigth = int(img.shape[0]*scale_percent)
    dimension=(width,heigth)

    resized=cv2.resize(img,dimension,interpolation=cv2.INTERAREA)

    print(resized.shape)
    cv2.imwrite('rezised'+nombre,resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


for file in archivosEnfermo:
    listaEnfermos.append(file)

for file in archivosSano:
    listaSano.append(file)

def __main__():
    #convertirEnMatriz()
    bajarEnfermo()
    #print(listaEnfermos)
   # print(listaSano)
    #print(listaSuprema)
__main__()

