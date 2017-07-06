#!/usr/bin/env python
import os
import sys
import random as ran


cantPersonas = 41

personas=ran.sample(range(1,42),cantPersonas)
kfold1={}
kfold2={}
kfold3={}	
kfold4={}
kfold5={}
kfolds=[kfold1,kfold2,kfold3,kfold4,kfold5]
#total="resultadosGenerales.out"
#archivoA=open(total,"w")
listaResultados=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
for j in personas:
	fotos=range(1,11)
	for k in range(0,5):
		fotosSeleccionadas=ran.sample(fotos,2)
		fotos=[x for x in fotos if x not in fotosSeleccionadas]
		kfolds[k][j]=fotosSeleccionadas
for cantAutovalores in range(1,51):	
	for j in range(0,5):
		archivoBig= "autovalores10_"+str(j+1)+"_Big_" + str(cantPersonas)+"_"+str(cantAutovalores)+".in"
		archivoRed= "autovalores10_"+str(j+1)+"_Red_" + str(cantPersonas)+"_"+str(cantAutovalores)+".in"
		archivoWBig=open(archivoBig,"w")
		archivoWRed=open(archivoRed,"w")
		archivoWBig.write("../data/ImagenesCaras/ 112 92 " + str(cantPersonas)+" 8 "+str(cantAutovalores)+"\n")
		archivoWRed.write("../data/ImagenesCarasRed/ 28 23 " + str(cantPersonas)+" 8 "+str(cantAutovalores)+"\n")
		for persona in personas:
			aux="s"+str(persona)+"/ "
			for i in range(0,5):
				if (i!=j):
					kfold = kfolds[i]
					for foto in kfold[persona]:
						aux+=str(foto)+" "
			aux+="\n"
			archivoWBig.write(aux)
			archivoWRed.write(aux)
		archivoWBig.write(str(cantPersonas*2)+"\n")
		archivoWRed.write(str(cantPersonas*2)+"\n")
		p=0
		for persona in personas:
			p+=1
			for i in range(0,5):
				if (i==j):
					kfold = kfolds[i]
					for foto in kfold[persona]: 
						auxBig="../data/ImagenesCaras/s"+str(persona)+"/"+str(foto)+".pgm "+str(p)+"\n"
						auxRed="../data/ImagenesCarasRed/s"+str(persona)+"/"+str(foto)+".pgm "+str(p)+"\n"
						archivoWBig.write(auxBig)
						archivoWRed.write(auxRed)
		archivoWBig.close()
		archivoWRed.close()
	# os.system("./main "+archivo+" test"+str(j+1)+".out")
	# resultado="resultados.out"
	# archivoR=open(resultado,"r")
	# for i in range(0,3):
	# 	linea=archivoR.readline()
	# 	linea=linea.split(" ")
	# 	for k in range(0,5):
	# 		listaResultados[i][k]+=float(linea[k])
#for i in range(0,3):
#	for k in range(0,5):
#		archivoA.write(str(listaResultados[i][k]/float(5))+" ")
#	archivoA.write("\n")