#!/usr/bin/env python
import os
import sys
import random as ran

size = int(sys.argv[1])
cantPersonas = int(sys.argv[2])
cantImgXPersonas = int(sys.argv[3])
cantAutovalores = int(sys.argv[4])
cantTest = int(sys.argv[5])

archivo= "test_"+ ("Big_" if size==0 else "Red_") + str(cantPersonas)+"_"+str(cantImgXPersonas)+"_"+str(cantAutovalores)+"_"+str(cantTest)+".in"
archivoW=open(archivo,"w")
archivoW.write("../data/ImagenesCaras"+(""if size==0 else"Red")+"/ "+ ("112 92 " if size==0 else "28 23 ") + str(cantPersonas)+" "+str(cantImgXPersonas)+" "+str(cantAutovalores)+"\n")
fotos={}
for i in range(1,cantPersonas+1):
	aux="s"+str(i)+"/ "
	ranNum= ran.sample(range(1,11),cantImgXPersonas)
	fotos[i]=ranNum
	for j in ranNum:
		aux+=str(j)+" "
	aux+="\n"
	archivoW.write(aux)
archivoW.write(str(cantTest)+"\n")
for i in range(1,cantTest+1):
	aux="../data/ImagenesCaras"+(""if size==0 else"Red")+"/s"+str(i)+"/"
	lista=[x for x in range(1,11) if x not in fotos[i]]
	aux+=str(ran.choice(lista))+".pgm "+str(i)+"\n"
	archivoW.write(aux)




