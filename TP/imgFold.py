#!/usr/bin/env python
import os
import sys
import random as ran

size = int(sys.argv[1])
cantPersonas = int(sys.argv[2])
cantImgXPersonas = int(sys.argv[3])
cantAutovalores = int(sys.argv[4])


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
total="resultadosGeneralesKfoldImg.out"
archivoA=open(total,"w")
listaResultados=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
for j in range(0,cantImgXPersonas):
	archivo= "pruebaKFoldImgXPersonas_"+str(j+1)+"_"+ ("Big_" if size==0 else "Red_") + str(cantPersonas)+"_"+str(cantImgXPersonas-1)+"_"+str(cantAutovalores)+".in"
	archivoW=open(archivo,"w")
	archivoW.write("../data/ImagenesCaras"+(""if size==0 else"Red")+"/ "+ ("112 92 " if size==0 else "28 23 ") + str(cantPersonas)+" "+str(cantImgXPersonas-1)+" "+str(cantAutovalores)+"\n")
	for persona in personas:
		aux="s"+str(persona)+"/ "
		for i in range(0,cantImgXPersonas):
			if (i!=j):
				kfold = kfolds[i]
				aux+=str(kfold[persona])+" "
		aux+="\n"
		archivoW.write(aux)
	archivoW.write(str(cantPersonas)+"\n")
	p=0
	for persona in personas:
		p+=1
		for i in range(0,cantImgXPersonas):
			if (i==j):
				kfold = kfolds[i]	 
				aux="../data/ImagenesCaras"+(""if size==0 else"Red")+"/s"+str(persona)+"/"+str(kfold[persona])+".pgm "+str(p)+"\n"
				archivoW.write(aux)
	archivoW.close()
	os.system("./main "+archivo+" testKFoldImgXPersonas_"+str(j+1)+".out")
	resultado="resultados.out"
	archivoR=open(resultado,"r")
	for i in range(0,3):
		linea=archivoR.readline()
		linea=linea.split(" ")
		for k in range(0,5):
			listaResultados[i][k]+=float(linea[k])
for i in range(0,3):
	for k in range(0,5):
		archivoA.write(str(listaResultados[i][k]/float(cantImgXPersonas))+" ")
	archivoA.write("\n")