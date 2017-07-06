#!/usr/bin/env python
import os
import sys
import random as ran

cantPersonas = 41
cantImgXPersonas = 5


personas=ran.sample(range(1,42),cantPersonas)
fotosDePersonas={}
for i in personas:
	fotos=range(1,11)
	fotosDePersonas[i]=fotos

kfolds=[]

for i in range(0,cantImgXPersonas):
	kfoldAux={}
	for j in personas:
		fotoSeleccionada= ran.choice(fotosDePersonas[j])
		kfoldAux[j]=fotoSeleccionada
		fotosDePersonas[j].remove(fotoSeleccionada)
	kfolds.append(kfoldAux)
total="resultadosAutovalores5.out"
#archivoA=open(total,"w")
listaResultados=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
for cantAutovalores in range(1,51):	
	for j in range(0,cantImgXPersonas):
		archivoBig= "autovalores5_"+str(j+1)+"_Big_" + str(cantPersonas)+"_"+str(cantAutovalores)+".in"
		archivoWBig=open(archivoBig,"w")
		archivoRed= "autovalores5_"+str(j+1)+"_Red_" + str(cantPersonas)+"_"+str(cantAutovalores)+".in"
		archivoWRed=open(archivoRed,"w")
		archivoWBig.write("../data/ImagenesCaras/ 112 92 " + str(cantPersonas)+" "+str(cantImgXPersonas-1)+" "+str(cantAutovalores)+"\n")
		archivoWRed.write("../data/ImagenesCarasRed/ 28 23 " + str(cantPersonas)+" "+str(cantImgXPersonas-1)+" "+str(cantAutovalores)+"\n")
		for persona in personas:
			aux="s"+str(persona)+"/ "
			for i in range(0,cantImgXPersonas):
				if (i!=j):
					kfold = kfolds[i]
					aux+=str(kfold[persona])+" "
			aux+="\n"
			archivoWBig.write(aux)
			archivoWRed.write(aux)
		archivoWBig.write(str(cantPersonas)+"\n")
		archivoWRed.write(str(cantPersonas)+"\n")
		p=0
		for persona in personas:
			p+=1
			for i in range(0,cantImgXPersonas):
				if (i==j):
					kfold = kfolds[i]	 
					auxBig="../data/ImagenesCaras"+"/s"+str(persona)+"/"+str(kfold[persona])+".pgm "+str(p)+"\n"
					auxRed="../data/ImagenesCarasRed"+"/s"+str(persona)+"/"+str(kfold[persona])+".pgm "+str(p)+"\n"
					archivoWBig.write(auxBig)
					archivoWRed.write(auxRed)
		archivoWBig.close()
		archivoWRed.close()
# 	os.system("./main "+archivo+" testKFoldImgXPersonas_"+str(j+1)+".out")
# 	resultado="resultados.out"
# 	archivoR=open(resultado,"r")
# 	for i in range(0,3):
# 		linea=archivoR.readline()
# 		linea=linea.split(" ")
# 		for k in range(0,5):
# 			listaResultados[i][k]+=float(linea[k])
# for i in range(0,3):
# 	for k in range(0,5):
# 		archivoA.write(str(listaResultados[i][k]/float(cantImgXPersonas))+" ")
# 	archivoA.write("\n")