#!/usr/bin/env python
import os
import sys
import matplotlib.pyplot as plt

size = int(sys.argv[1])
cantPersonas = int(sys.argv[2])
inicio = int(sys.argv[3])
fin = int(sys.argv[4])
valoresMan={}
valoresNor={}
valoresHam={}
for i in range(inicio,fin+1):
	os.system("python kfold.py "+str(size)+" "+str(cantPersonas)+" "+str(i))
	archivoR=open("resultados.out","r")
	linea=archivoR.readline()
	linea=linea.split(" ")
	listaFloats=[float(j) for j in linea]
	valoresHam[i]=listaFloats
	linea=archivoR.readline()
	linea=linea.split(" ")
	listaFloats=[float(j) for j in linea]
	valoresMan[i]=listaFloats
	linea=archivoR.readline()
	linea=linea.split(" ")
	listaFloats=[float(j) for j in linea]
	valoresNor[i]=listaFloats
	archivoR.close()

keys=range(inicio,fin+1)
precisionHam=[]
precisionMan=[]
precisionNor=[]
recallHam=[]
recallMan=[]
recallNor=[]
specificityHam=[]
specificityMan=[]
specificityNor=[]
f1Ham=[]
f1Man=[]
f1Nor=[]
hitrateHam=[]
hitrateMan=[]
hitrateNor=[]
for i in keys:
	precisionHam.append(valoresHam[i][0])
	precisionMan.append(valoresMan[i][0])
	precisionNor.append(valoresNor[i][0])
	recallHam.append(valoresHam[i][1])
	recallMan.append(valoresMan[i][1])
	recallNor.append(valoresNor[i][1])
	specificityHam.append(valoresHam[i][2])
	specificityMan.append(valoresMan[i][2])
	specificityNor.append(valoresNor[i][2])
	f1Ham.append(valoresHam[i][3])
	f1Man.append(valoresMan[i][3])
	f1Nor.append(valoresNor[i][3])
	hitrateHam.append(valoresHam[i][4])
	hitrateMan.append(valoresMan[i][4])
	hitrateNor.append(valoresNor[i][4])

plt.xlabel("cantidad de autovalores")
plt.ylabel("precision")
plt.title("precision segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
plt.plot(keys,precisionHam,label='Funcion de Hamming');
plt.plot(keys,precisionMan,label='Distancia Manhattan');
plt.plot(keys,precisionNor,label='Distancia Norma 2');
plt.show();

plt.xlabel("cantidad de autovalores")
plt.ylabel("recall")
plt.title("recall segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
plt.plot(keys,recallHam,label='Funcion de Hamming');
plt.plot(keys,recallMan,label='Distancia Manhattan');
plt.plot(keys,recallNor,label='Distancia Norma 2');
plt.show();

plt.xlabel("cantidad de autovalores")
plt.ylabel("specificity")
plt.title("specificity segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
plt.plot(keys,specificityHam,label='Funcion de Hamming');
plt.plot(keys,specificityMan,label='Distancia Manhattan');
plt.plot(keys,specificityNor,label='Distancia Norma 2');
plt.show();

plt.xlabel("cantidad de autovalores")
plt.ylabel("f1")
plt.title("f1 segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
plt.plot(keys,f1Ham,label='Funcion de Hamming');
plt.plot(keys,f1Man,label='Distancia Manhattan');
plt.plot(keys,f1Nor,label='Distancia Norma 2');
plt.show();

plt.xlabel("cantidad de autovalores")
plt.ylabel("hitrate")
plt.title("hitrate segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
plt.plot(keys,hitrateHam,label='Funcion de Hamming');
plt.plot(keys,hitrateMan,label='Distancia Manhattan');
plt.plot(keys,hitrateNor,label='Distancia Norma 2');
plt.show();