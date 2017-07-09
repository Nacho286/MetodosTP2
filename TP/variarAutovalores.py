#!/usr/bin/env python
import os
import sys
import matplotlib.pyplot as plt

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
##Esto se correria una sola vez y despues se comenta, es para generar los resultados y guardarlos, si queremos modificar los graficos ya tenemos los resultados guardados
# os.system("python generarArchivos5.py")
# os.system("python generarArchivo10.py")
# resultadosBig5=open("resultadosAutoBig5","w")
# resultadosRed5=open("resultadosAutoRed5","w")
# resultadosBig10=open("resultadosAutoBig10","w")
# resultadosRed10=open("resultadosAutoRed10","w")
# for i in range(1,51):
# 	listaResultadosBig5=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
# 	listaResultadosRed5=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
# 	listaResultadosBig10=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
# 	listaResultadosRed10=[[0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0]]
	
# 	for j in range(1,6):
# 		os.system("./main "+"autovalores5_"+str(j)+"_Big_41_"+str(i)+".in " +"test.out")
# 		archivoR=open("resultados.out","r")
# 		for n in range(0,2):
# 			linea=archivoR.readline()
# 			linea=linea.split(" ")
# 			for k in range(0,5):
# 				listaResultadosBig5[n][k]+=float(linea[k])
# 		archivoR.close()
# 		os.system("./main "+"autovalores5_"+str(j)+"_Red_41_"+str(i)+".in " +"test.out")
# 		archivoR=open("resultados.out","r")
# 		for n in range(0,2):
# 			linea=archivoR.readline()
# 			linea=linea.split(" ")
# 			for k in range(0,5):
# 				listaResultadosRed5[n][k]+=float(linea[k])
# 		archivoR.close()
# 		os.system("./main "+"autovalores10_"+str(j)+"_Big_41_"+str(i)+".in " +"test.out")
# 		archivoR=open("resultados.out","r")
# 		for n in range(0,2):
# 			linea=archivoR.readline()
# 			linea=linea.split(" ")
# 			for k in range(0,5):
# 				listaResultadosBig10[n][k]+=float(linea[k])
# 		archivoR.close()
# 		os.system("./main "+"autovalores10_"+str(j)+"_Red_41_"+str(i)+".in " +"test.out")
# 		archivoR=open("resultados.out","r")
# 		for n in range(0,2):
# 			linea=archivoR.readline()
# 			linea=linea.split(" ")
# 			for k in range(0,5):
# 				listaResultadosRed10[n][k]+=float(linea[k])
# 		archivoR.close()
# 	for n in range(0,2):
# 		for k in range(0,5):
# 			resultadosBig5.write(str(listaResultadosBig5[n][k]/float(5))+" ")
# 			resultadosRed5.write(str(listaResultadosRed5[n][k]/float(5))+" ")
# 			resultadosBig10.write(str(listaResultadosBig10[n][k]/float(5))+" ")
# 			resultadosRed10.write(str(listaResultadosRed10[n][k]/float(5))+" ")
# 		resultadosRed5.write("\n")
# 		resultadosBig5.write("\n")
# 		resultadosRed10.write("\n")
# 		resultadosBig10.write("\n")
# resultadosBig5.close()
# resultadosRed5.close()
# resultadosBig10.close()
# resultadosRed10.close()



valoresRed5=valores("resultadosAutoRed5")
valoresBig5=valores("resultadosAutoBig5")
valoresRed10=valores("resultadosAutoRed10")
valoresBig10=valores("resultadosAutoBig10")
keys=range(1,51)


plt.xlabel("cantidad de autovalores");
plt.ylabel("precision");
plt.title("precision segun la cantidad de autovalores, con 41 personas y 5 fotos");
plt.plot(keys,valoresRed5[0],label='kNN,imgs red');
plt.plot(keys,valoresRed5[1],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig5[0],label='kNN,imgs big');
plt.plot(keys,valoresBig5[1],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("precision");
plt.title("precision segun la cantidad de autovalores, con 41 personas y 8 fotos");
plt.plot(keys,valoresRed10[0],label='kNN,imgs red');
plt.plot(keys,valoresRed10[1],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig10[0],label='kNN,imgs big');
plt.plot(keys,valoresBig10[1],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("recall");
plt.title("recall segun la cantidad de autovalores, con 41 personas y 5 fotos");
plt.plot(keys,valoresRed5[2],label='kNN,imgs red');
plt.plot(keys,valoresRed5[3],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig5[2],label='kNN,imgs big');
plt.plot(keys,valoresBig5[3],label='skNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6))
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("recall");
plt.title("recall segun la cantidad de autovalores, con 41 personas y 8 fotos");
plt.plot(keys,valoresRed10[2],label='kNN,imgs red');
plt.plot(keys,valoresRed10[3],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig10[2],label='kNN,imgs big');
plt.plot(keys,valoresBig10[3],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("specificity");
plt.title("specificity segun la cantidad de autovalores, con 41 personas y 5 fotos");
plt.plot(keys,valoresRed5[4],label='kNN,imgs red');
plt.plot(keys,valoresRed5[5],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig5[4],label='kNN,imgs big');
plt.plot(keys,valoresBig5[5],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();
plt.xlabel("cantidad de autovalores");
plt.ylabel("specificity");
plt.title("specificity segun la cantidad de autovalores, con 41 personas y 8 fotos");
plt.plot(keys,valoresRed10[4],label='kNN,imgs red');
plt.plot(keys,valoresRed10[5],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig10[4],label='kNN,imgs big');
plt.plot(keys,valoresBig10[5],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("f1");
plt.title("f1 segun la cantidad de autovalores, con 41 personas y 5 fotos");
plt.plot(keys,valoresRed5[6],label='kNN,imgs red');
plt.plot(keys,valoresRed5[7],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig5[6],label='kNN,imgs big');
plt.plot(keys,valoresBig5[7],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("f1");
plt.title("f1 segun la cantidad de autovalores, con 41 personas y 8 fotos");
plt.plot(keys,valoresRed10[6],label='kNN,imgs red');
plt.plot(keys,valoresRed10[7],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig10[6],label='kNN,imgs big');
plt.plot(keys,valoresBig10[7],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();

plt.xlabel("cantidad de autovalores");
plt.ylabel("hitrate");
plt.title("hitrate segun la cantidad de autovalores, con 41 personas y 5 fotos");
plt.plot(keys,valoresRed5[8],label='kNN,imgs red');
plt.plot(keys,valoresRed5[9],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig5[8],label='kNN,imgs big');
plt.plot(keys,valoresBig5[9],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();


plt.xlabel("cantidad de autovalores");
plt.ylabel("hitrate");
plt.title("hitrate segun la cantidad de autovalores, con 41 personas y 8 fotos");
plt.plot(keys,valoresRed10[8],label='kNN,imgs red');
plt.plot(keys,valoresRed10[9],label='kNN pesado,imgs red');
plt.plot(keys,valoresBig10[8],label='kNN,imgs big');
plt.plot(keys,valoresBig10[9],label='kNN pesado,imgs big');
plt.legend(bbox_to_anchor=(1.0,0.6));
plt.show();



