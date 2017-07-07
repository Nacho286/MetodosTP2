#!/usr/bin/env python
import os
import sys
import matplotlib.pyplot as plt

os.system("python generarImagenes.py")
iterar("Big",5)
iterar("Big",10)
iterar("Big",15)
iterar("Red",5)
iterar("Red",10)
iterar("Red",15)

valoresRed5=valores("resultadosImgRed5")
valoresBig5=valores("resultadosImgBig5")
valoresRed10=valores("resultadosImgRed10")
valoresBig10=valores("resultadosImgBig10")
valoresRed15=valores("resultadosImgRed15")
valoresBig15=valores("resultadosImgBig15")

keys=range(1,10)

# plt.xlabel("cantidad de imagenes por personas")
# plt.ylabel("precision") 
# plt.title("precision segun la cantidad de imagenes por personas, con "+str(cantPersonas)+" personas y usando "+str(cantAutovalores)+" autovalores");
# plt.plot(keys,precisionHam,label='Funcion de Hamming');
# plt.plot(keys,precisionMan,label='Distancia Manhattan');
# plt.plot(keys,precisionNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de imagenes por personas")
# plt.ylabel("recall")
# plt.title("recall segun la cantidad de imagenes por personas, con "+str(cantPersonas)+" personas y usando "+str(cantAutovalores)+" autovalores");
# plt.plot(keys,recallHam,label='Funcion de Hamming');
# plt.plot(keys,recallMan,label='Distancia Manhattan');
# plt.plot(keys,recallNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de imagenes por personas")
# plt.ylabel("specificity")
# plt.title("specificity segun la cantidad de imagenes por personas, con "+str(cantPersonas)+" personas y usando "+str(cantAutovalores)+" autovalores");
# plt.plot(keys,specificityHam,label='Funcion de Hamming');
# plt.plot(keys,specificityMan,label='Distancia Manhattan');
# plt.plot(keys,specificityNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de imagenes por personas")
# plt.ylabel("f1")
# plt.title("f1 segun la cantidad de imagenes por personas, con "+str(cantPersonas)+" personas y usando "+str(cantAutovalores)+" autovalores");
# plt.plot(keys,f1Ham,label='Funcion de Hamming');
# plt.plot(keys,f1Man,label='Distancia Manhattan');
# plt.plot(keys,f1Nor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de imagenes por personas")
# plt.ylabel("hitrate")
# plt.title("hitrate segun la cantidad de imagenes por personas, con "+str(cantPersonas)+" personas y usando "+str(cantAutovalores)+" autovalores");
# plt.plot(keys,hitrateHam,label='Funcion de Hamming');
# plt.plot(keys,hitrateMan,label='Distancia Manhattan');
# plt.plot(keys,hitrateNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

def iterar(size,autovalores):
	archivoW=open("resultadosImg"+size+autovalores,"w")
	for i in range(1,10):
		listaResultados=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
		for j in range(1,i+2):
			os.system("./main "+"ImgXPersonas_"+str(i)+"_"+str(j)+"_"+size+"_41_"+str(autovalores)+".in " +"test.out")
			archivoR=open("resultados.out","r")
			for n in range(0,2):
				linea=archivoR.readline()
				linea=linea.split(" ")
				for k in range(0,5):
					listaResultados[n][k]+=float(linea[k])
			archivoR.close()
		for n in range(0,2):
			for k in range(0,5):
				archivoW.write(str(listaResultados[n][k]/float(i+1))+" ")
			archivoW.write("\n")
	archivoW.close()

def valores(archivo):
	archivoR=open(archivo,"r")
	valoresSPeso={}
	valoresModa={}
	for i in range(1,51):
		linea=archivoR.readline()
		linea=linea.split()
		listaFloats=[float(j) for j in linea]
		valoresSPeso[i]=listaFloats
		linea=archivoR.readline()
		linea=linea.split()
		listaFloats=[float(j) for j in linea]
		valoresModa[i]=listaFloats
	archivoR.close()
	precisionSPeso=[]
	precisionModa=[]
	recallSPeso=[]
	recallModa=[]
	specificitySPeso=[]
	specificityModa=[]
	f1SPeso=[]
	f1Moda=[]
	hitrateSPeso=[]
	hitrateModa=[]
	for i in range(1,51):
	 	precisionSPeso.append(valoresSPeso[i][0])
		precisionModa.append(valoresModa[i][0])
		recallSPeso.append(valoresSPeso[i][1])
		recallModa.append(valoresModa[i][1])
		specificitySPeso.append(valoresSPeso[i][2])
		specificityModa.append(valoresModa[i][2])
		f1SPeso.append(valoresSPeso[i][3])
		f1Moda.append(valoresModa[i][3])
		hitrateSPeso.append(valoresSPeso[i][4])
		hitrateModa.append(valoresModa[i][4])
	return [precisionSPeso,precisionModa,recallSPeso,recallModa,specificitySPeso,specificityModa,f1SPeso,f1Moda,hitrateSPeso,hitrateModa]