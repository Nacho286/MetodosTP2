#!/usr/bin/env python
import os
import sys
import random as ran

cantPersonas = 41
cantImgXPersonas = int(sys.argv[1])


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
# total="resultadosGeneralesKfoldImg.out"
# archivoA=open(total,"w")
listaResultados=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
for j in range(0,cantImgXPersonas):
	archivoBig5= "ImgXPersonas_"+str(cantImgXPersonas-1)+"_"+str(j+1)+"_Big_41_5.in"
	archivoRed5= "ImgXPersonas_"+str(cantImgXPersonas-1)+"_"+str(j+1)+"_Red_41_5.in"
	archivoBig10= "ImgXPersonas_"+str(cantImgXPersonas-1)+"_"+str(j+1)+"_Big_41_10.in"
	archivoRed10= "ImgXPersonas_"+str(cantImgXPersonas-1)+"_"+str(j+1)+"_Red_41_10.in"
	archivoBig15= "ImgXPersonas_"+str(cantImgXPersonas-1)+"_"+str(j+1)+"_Big_41_15.in"
	archivoRed15= "ImgXPersonas_"+str(cantImgXPersonas-1)+"_"+str(j+1)+"_Red_41_15.in"
	archivoWBig5=open(archivoBig5,"w")
	archivoWRed5=open(archivoRed5,"w")
	archivoWBig10=open(archivoBig10,"w")
	archivoWRed10=open(archivoRed10,"w")
	archivoWBig15=open(archivoBig15,"w")
	archivoWRed15=open(archivoRed15,"w")
	archivoWBig5.write("../data/ImagenesCaras/ 112 92 41 "+str(cantImgXPersonas-1)+" 5\n")
	archivoWRed5.write("../data/ImagenesCarasRed/ 28 23 41 "+str(cantImgXPersonas-1)+" 5\n")
	archivoWBig10.write("../data/ImagenesCaras/ 112 92 41 "+str(cantImgXPersonas-1)+" 10\n")
	archivoWRed10.write("../data/ImagenesCarasRed/ 28 23 41 "+str(cantImgXPersonas-1)+" 10\n")
	archivoWBig15.write("../data/ImagenesCaras/ 112 92 41 "+str(cantImgXPersonas-1)+" 15\n")
	archivoWRed15.write("../data/ImagenesCarasRed/ 28 23 41 "+str(cantImgXPersonas-1)+" 15\n")
	for persona in personas:
		aux="s"+str(persona)+"/ "
		for i in range(0,cantImgXPersonas):
			if (i!=j):
				kfold = kfolds[i]
				aux+=str(kfold[persona])+" "
		aux+="\n"
		archivoWBig5.write(aux)
		archivoWRed5.write(aux)
		archivoWBig10.write(aux)
		archivoWRed10.write(aux)
		archivoWBig15.write(aux)
		archivoWRed15.write(aux)
	archivoWBig5.write(str(cantPersonas)+"\n")
	archivoWRed5.write(str(cantPersonas)+"\n")
	archivoWBig10.write(str(cantPersonas)+"\n")
	archivoWRed10.write(str(cantPersonas)+"\n")
	archivoWBig15.write(str(cantPersonas)+"\n")
	archivoWRed15.write(str(cantPersonas)+"\n")
	p=0
	for persona in personas:
		p+=1
		for i in range(0,cantImgXPersonas):
			if (i==j):
				kfold = kfolds[i]	 
				auxBig="../data/ImagenesCaras/s"+str(persona)+"/"+str(kfold[persona])+".pgm "+str(p)+"\n"
				auxRed="../data/ImagenesCarasRed/s"+str(persona)+"/"+str(kfold[persona])+".pgm "+str(p)+"\n"
				archivoWBig5.write(auxBig)
				archivoWRed5.write(auxRed)
				archivoWBig10.write(auxBig)
				archivoWRed10.write(auxRed)
				archivoWBig15.write(auxBig)
				archivoWRed15.write(auxRed)
	archivoWBig5.close()
	archivoWRed5.close()
	archivoWBig10.close()
	archivoWRed10.close()
	archivoWBig15.close()
	archivoWRed15.close()
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