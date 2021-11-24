#el metodo comprimir  solo funciona si esta dentro de la carpeta de archivos se solucionara mas adelante
import requests
import urllib.request
from huffman import HuffmanCoding
from numpy import genfromtxt 
from matplotlib import pyplot as plt
from PIL import Image
import seam_carving
import numpy
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





def comprimirYdescomprimirConPerdidasYsinPerdidas():
    f = r"Ponga la ruta del archivo aqui"
    print(type(f))
    f = genfromtxt(f, delimiter = ",") 
    print(f.shape)
    f_h, f_w= f.shape
    dst = seam_carving.resize(
        f, (f_w - 100, f_h-100),
        energy_mode='forward',   
        order='width-first', 
        keep_mask=None
    )

    imgplot = plt.imshow(f, cmap = "gray") 
    plt.show()

    imgplot = plt.imshow(dst, cmap = "gray") 
    plt.show()
    dst = numpy.array(dst)
    numpy.savetxt(r"ponga la ruta con el nombre de archivo alfinal", dst, delimiter = ",")
    #dst.tofile(r"C:\Users\juane\Documents\Proyectos Datos y algoritmos\proyecto\codigo\comprimidoT.csv", sep=",")
    path = "comprimidoT.csv"
    h = HuffmanCoding(path)

    output_path = h.compress()
    print("Compressed file path: " + output_path)

    decom_path = h.decompress(output_path)
    print("Decompressed file path: " + decom_path)

    f2 = "comprimidoT_decompressed.csv" 
    print(type(f2))

    f2 = genfromtxt(f2, delimiter = ",") 
    print(f2.shape)
    f2_h, f2_w= f2.shape
    dst2 = seam_carving.resize(
        f2, (f2_w + 100, f2_h+100),
        energy_mode='forward',   # Choose from {backward, forward}
        order='width-first',  # Choose from {width-first, height-first}
        keep_mask=None
    )
    imgplot = plt.imshow(dst2, cmap = "gray") 
    plt.show()

def comprimirYdescomprimirEnfermoSinPerdidas():
    path = r"ponga la ruta del archivo aqui"
    h = HuffmanCoding(path)

    output_path = h.compress()
    print("Compressed file path: " + output_path)

    decom_path = h.decompress(output_path)
    print("Decompressed file path: " + decom_path)

    f = genfromtxt(decom_path, delimiter = ",")
    imgplot = plt.imshow(f, cmap = "gray") 
    plt.show()
    

def comprimirEnfermoCsvConPerdidas():  
    f = "ponga la ruta del archivo aqui" 

    f = genfromtxt(f, delimiter = ",") 

    f_h, f_w= f.shape
    dst = seam_carving.resize(
    f, (f_w - 150, f_h - 100),
    energy_mode='forward',   # Choose from {backward, forward}
    order='width-first',  # Choose from {width-first, height-first}
    keep_mask=None
    )

    imgplot = plt.imshow(f, cmap = "gray") 
    plt.show()

    imgplot = plt.imshow(dst, cmap = "gray") 
    plt.show()

    dst = seam_carving.resize(
    f, (f_w + 100, f_h + 100),
    energy_mode='forward',   # Choose from {backward, forward}
    order='width-first',  # Choose from {width-first, height-first}
    keep_mask=None
    )
    imgplot = plt.imshow(dst, cmap = "gray") 
    plt.show()



def comprimirEnfermoImagen(archivos):
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

#direccionEnfermo = "Direccion de la carpeta enfermos"
#archivosEnfermo = os.listdir(direccionEnfermo)

#direccionSano = "Direccion de la carpeta sanos"
#archivosSano = os.listdir(direccionSano)


def __main__():
    #bajarEnfermo()
    #bajarSano()
    #comprimirEnfermoImagen(direccionEnfermo)
    #comprimirSano(direccionSano)
    #comprimirEnfermoCsvConPerdidas()
    #comprimirYdescomprimirEnfermoSinPerdidas()
    comprimirYdescomprimirConPerdidasYsinPerdidas()
__main__()


