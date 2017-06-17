#!/usr/bin/env python
import os
import sys
import random as ran

archivos={}
for i in range (2,10):
	personas=ran.sample(range(1,43),42)
	fotosDePersonas={}
	for i in personas:
		fotos=range(1,11)
		fotosDePersonas[i]=fotos

	kfolds=[]
	for j in range(0,i):
		kfoldAux={}
		for j in personas:
			fotoSeleccionada= ran.choice(fotosDePersonas[j])
			kfoldAux[j]=fotoSeleccionada
			fotosDePersonas[j].remove(fotoSeleccionada)
		kfolds.append(kfoldAux)
	arhivos[i]=kfolds
print(archivos)
# size = int(sys.argv[1])
# cantPersonas = int(sys.argv[2])
# cantImgXPersonas = int(sys.argv[3])
# cantAutovalores = int(sys.argv[4])
# cantTest = int(sys.argv[5])
#
# archivo= "test_"+ ("Big_" if size==0 else "Red_") + str(cantPersonas)+"_"+str(cantImgXPersonas)+"_"+str(cantAutovalores)+"_"+str(cantTest)+".in"
# archivoW=open(archivo,"w")
# archivoW.write("../data/ImagenesCaras"+(""if size==0 else"Red")+"/ "+ ("112 92 " if size==0 else "28 23 ") + str(cantPersonas)+" "+str(cantImgXPersonas)+" "+str(cantAutovalores)+"\n")
# fotos={}
# fotosPrueba={}
# for i in range(1,cantPersonas+1):
# 	aux="s"+str(i)+"/ "
# 	ranNum= ran.sample(range(1,11),cantImgXPersonas)
# 	fotos[i]=ranNum
# 	fotosPrueba[i]=[x for x in range(1,11) if x not in fotos[i]]
# 	for j in ranNum:
# 		aux+=str(j)+" "
# 	aux+="\n"
# 	archivoW.write(aux)
#
# archivoW.write(str(cantTest)+"\n")
# for i in range(1,cantTest+1):
#
# 	j=ran.choice(range(1,cantPersonas+1))
#
# 	while(len(fotosPrueba[j])==0):
# 		j=ran.choice(range(1,cantPersonas+1))
# 	aux="../data/ImagenesCaras"+(""if size==0 else"Red")+"/s"+str(j)+"/"
# 	lista=fotosPrueba[j]
# 	d=ran.choice(lista)
# 	lista.remove(d)
# 	fotosPrueba[j]=lista
# 	aux+=str(d)+".pgm "+str(j)+"\n"
# 	archivoW.write(aux)
#
# archivoW.close()
# os.system('./main '+archivo+' test.out');
#
# archivoR=open("cantExitos.out","r")
# linea=archivoR.readline()
# print linea
