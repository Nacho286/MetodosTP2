#!/usr/bin/env python
import os
import sys
#import matplotlib.pyplot as plt

##Esto se correria una sola vez y despues se comenta, es para generar los resultados y guardarlos, si queremos modificar los graficos ya tenemos los resultados guardados
os.system("python generarArchivos5.py")
os.system("python generarArchivo10.py")
resultadosBig5=open("resultadosBig5","w")
resultadosRed5=open("resultadosRed5","w")
resultadosBig10=open("resultadosBig10","w")
resultadosRed10=open("resultadosRed10","w")
for i in range(1,51):
	listaResultadosBig5=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
	listaResultadosRed5=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
	listaResultadosBig10=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
	listaResultadosRed10=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
	for j in range(1,6):
		os.system("./main "+"autovalores5_"+str(j)+"_Big_41_"+str(i)+".in" +"test.out")
		archivoR=open("resultados.out","r")
		for n in range(0,2):
			linea=archivoR.readline()
			linea=linea.split(" ")
			for k in range(0,5):
				listaResultadosBig5[n][k]+=float(linea[k])
		archivoR.close()
		os.system("./main "+"autovalores5_"+str(j)+"_Red_41_"+str(i)+".in" +"test.out")
		archivoR=open("resultados.out","r")
		for n in range(0,2):
			linea=archivoR.readline()
			linea=linea.split(" ")
			for k in range(0,5):
				listaResultadosRed5[n][k]+=float(linea[k])
		archivoR.close()
		os.system("./main "+"autovalores10_"+str(j)+"_Big_41_"+str(i)+".in" +"test.out")
		archivoR=open("resultados.out","r")
		for n in range(0,2):
			linea=archivoR.readline()
			linea=linea.split(" ")
			for k in range(0,5):
				listaResultadosBig10[n][k]+=float(linea[k])
		archivoR.close()
		os.system("./main "+"autovalores10_"+str(j)+"_Red_41_"+str(i)+".in" +"test.out")
		archivoR=open("resultados.out","r")
		for n in range(0,2):
			linea=archivoR.readline()
			linea=linea.split(" ")
			for k in range(0,5):
				listaResultadosRed10[n][k]+=float(linea[k])
		archivoR.close()
	for n in range(0,2):
		for k in range(0,5):
			resultadosBig5.write(str(listaResultadosBig5[i][k]/float(5))+" ")
			resultadosRed5.write(str(listaResultadosRed5[i][k]/float(5))+" ")
			resultadosBig10.write(str(listaResultadosBig10[i][k]/float(5))+" ")
			resultadosRed10.write(str(listaResultadosRed10[i][k]/float(5))+" ")
		resultadosRed5.write("\n")
		resultadosBig5.write("\n")
		resultadosRed10.write("\n")
		resultadosBig10.write("\n")
resultadosBig5.close()
resultadosRed5.close()
resultadosBig10.close()
resultadosRed10.close()
valoresSPesoRed5={}
valoresModaRed5={}
valoresSPesoBig5={}
valoresModaBig5={}
valoresSPesoRed10={}
valoresModaRed10={}
valoresSPesoBig10={}
valoresModaBig10={}
resultadosBig5=open("resultadosBig5","r")
resultadosRed5=open("resultadosRed5","r")
resultadosBig10=open("resultadosBig10","r")
resultadosRed10=open("resultadosRed10","r")
for i in range(1,51):
	linea=archivoBig5.readline()
	linea=linea.split()
	listaFloats=[float(j) for j in linea]
	valoresHam[i]=listaFloats
	linea=archivoBig5.readline()
	linea=linea.split()
	listaFloats=[float(j) for j in linea]
	valoresMan[i]=listaFloats
	linea=archivoR.readline()
	linea=linea.split()
	listaFloats=[float(j) for j in linea]
	valoresNor[i]=listaFloats
	archivoR.close()



keys=range(1,51)
precisionSPesoBig=[]
precisionModaBig=[]
recallSPesoBig=[]
recallModaBig=[]
specificitySPesoBig=[]
specificityModaBig=[]
f1SPesoBig=[]
f1ModaBig=[]
hitrateSPesoBig=[]
hitrateModaBig=[]
precisionSPesoRed=[]
precisionModaRed=[]
recallSPesoRed=[]
recallModaRed=[]
specificitySPesoRed=[]
specificityModaRed=[]
f1SPesoRed=[]
f1ModaRed=[]
hitrateSPesoRed=[]
hitrateModaRed=[]
for i in keys:
	lineaBig=resultadosBig.readline()
	lineaRed=resultadosRed.readline()
# 	precisionSPeso.append(valoresHam[i][0])
# 	precisionMan.append(valoresMan[i][0])
# 	precisionNor.append(valoresNor[i][0])
# 	recallHam.append(valoresHam[i][1])
# 	recallMan.append(valoresMan[i][1])
# 	recallNor.append(valoresNor[i][1])
# 	specificityHam.append(valoresHam[i][2])
# 	specificityMan.append(valoresMan[i][2])
# 	specificityNor.append(valoresNor[i][2])
# 	f1Ham.append(valoresHam[i][3])
# 	f1Man.append(valoresMan[i][3])
# 	f1Nor.append(valoresNor[i][3])
# 	hitrateHam.append(valoresHam[i][4])
# 	hitrateMan.append(valoresMan[i][4])
# 	hitrateNor.append(valoresNor[i][4])

# plt.xlabel("cantidad de autovalores")
# plt.ylabel("precision")
# plt.title("precision segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
# plt.plot(keys,precisionHam,label='Funcion de Hamming');
# plt.plot(keys,precisionMan,label='Distancia Manhattan');
# plt.plot(keys,precisionNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de autovalores")
# plt.ylabel("recall")
# plt.title("recall segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
# plt.plot(keys,recallHam,label='Funcion de Hamming');
# plt.plot(keys,recallMan,label='Distancia Manhattan');
# plt.plot(keys,recallNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de autovalores")
# plt.ylabel("specificity")
# plt.title("specificity segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
# plt.plot(keys,specificityHam,label='Funcion de Hamming');
# plt.plot(keys,specificityMan,label='Distancia Manhattan');
# plt.plot(keys,specificityNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de autovalores")
# plt.ylabel("f1")
# plt.title("f1 segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
# plt.plot(keys,f1Ham,label='Funcion de Hamming');
# plt.plot(keys,f1Man,label='Distancia Manhattan');
# plt.plot(keys,f1Nor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();

# plt.xlabel("cantidad de autovalores")
# plt.ylabel("hitrate")
# plt.title("hitrate segun la cantidad de autovalores, con "+str(cantPersonas)+" personas");
# plt.plot(keys,hitrateHam,label='Funcion de Hamming');
# plt.plot(keys,hitrateMan,label='Distancia Manhattan');
# plt.plot(keys,hitrateNor,label='Distancia Norma 2');
# plt.legend(bbox_to_anchor=(0.33,1.0));
# plt.show();
