#!/usr/bin/env python
import os
import sys
import matplotlib.pyplot as plt

os.system("python kfold.py 0 41 15")
archivoR = open("cantExitos.out","r")
exitosNorma = archivoR.readline()
exitosNorma = [float(i) for i in exitosNorma.split()]
exitosCota = archivoR.readline()
exitosCota = [float(i) for i in exitosCota.split()]
keys=range(1,1501)

plt.xlabel("norma o cota")
plt.ylabel("hitrate") 
plt.title("hitrate segun el numero que se usa como cota en Hamming o la norma con la que se calcula la distancia");
plt.plot(keys,exitosCota,label='Funcion de Hamming');
plt.plot(keys,exitosNorma,label='Distancia Norma');
plt.show();