#!/usr/bin/env python
import os
import sys
import random as ran

size = int(sys.argv[1])
cantPersonas = int(sys.argv[2])
cantAutovalores = int(sys.argv[3])

if cantPersonas > 10:
	cantPersonas = 10
personas = ran.sample(range(1,42),cantPersonas)
kfold1 = {}
kfold2 = {}
kfold3 = {}	
kfold4 = {}
kfold5 = {}
kfolds = [kfold1, kfold2, kfold3, kfold4, kfold5]
total = "resultados_" + str(cantPersonas) + "_" + str(cantAutovalores) + ".out"
archivoA = open(total, "w")
listaResultados = [0.0, 0.0, 0.0, 0.0]
for j in personas:
	fotos=range(1,11)
	for k in range(0,5):
		fotosSeleccionadas=ran.sample(fotos,2)
		fotos=[x for x in fotos if x not in fotosSeleccionadas]
		kfolds[k][j]=fotosSeleccionadas
for j in range(0,5):
	archivo= "pruebaKFold"+str(j+1)+"_"+ ("Big_" if size==0 else "Red_") + str(cantPersonas)+"_"+str(cantAutovalores)+".in"
	archivoW=open(archivo,"w")
	archivoW.write("../data/ImagenesCaras"+(""if size==0 else"Red")+"/ "+ ("112 92 " if size==0 else "28 23 ") + str(cantPersonas)+" 8 "+str(cantAutovalores)+"\n")
	for persona in personas:
		aux="s"+str(persona)+"/ "
		for i in range(0,5):
			if (i!=j):
				kfold = kfolds[i]
				for foto in kfold[persona]:
					aux+=str(foto)+" "
		aux+="\n"
		archivoW.write(aux)
	cantObjetos = 10
	ntest = 31 * 10 + cantObjetos # + cantPersonas * 2
	archivoW.write(str(ntest)+"\n")
	# p=0
	# for persona in personas:
	# 	p+=1
	# 	for i in range(0,5):
	# 		if (i==j):
	# 			kfold = kfolds[i]
	# 			for foto in kfold[persona]: 
	# 				aux="../data/ImagenesCaras"+(""if size==0 else"Red")+"/s"+str(persona)+"/"+str(foto)+".pgm 1 \n"
	# 				archivoW.write(aux)
	count = 0
	for i in range(1, 42):
		if i not in personas:
			count += 1
			for foto in range(1, 11):
				aux="../data/ImagenesCaras" + ("" if size == 0 else "Red") + "/s" + str(i) + "/" + str(foto) + ".pgm 1 \n"
				archivoW.write(aux)
		if count >= 31:
			break
	for i in range(1, 11):
		aux="../data/ImagenesCaras" + ("" if size == 0 else "Red") + "/obj/" + str(i) + ".pgm 0 \n"
		archivoW.write(aux)
	archivoW.close()
	os.system("./main "+archivo+" test"+str(j+1)+".out 0 1")
	resultado = "resultados.out"
	archivoR  = open(resultado,"r")
	linea     = archivoR.readline()
	linea     = linea.split(" ")
	for k in range(0, 4):
		listaResultados[k] += float(linea[k])
	os.remove(archivo)
	os.remove("test" + str(j + 1) + ".out")
	os.remove(resultado)
for k in range(0, 4):
	archivoA.write(str(listaResultados[k] / float(5)) + " ")
archivoA.close()