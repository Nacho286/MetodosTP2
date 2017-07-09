#!/usr/bin/env python
import os
import sys
import matplotlib.pyplot as plt

def iterar(size,autovalores):
	archivoW=open("resultadosImg"+size+str(autovalores),"w")
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
	for i in range(1,10):
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
	for i in range(1,10):
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


# os.system("python generarImagenes.py")
# iterar("Big",5)
# iterar("Big",10)
# iterar("Big",15)
# iterar("Red",5)
# iterar("Red",10)
# iterar("Red",15)

valoresRed5=valores("resultadosImgRed5")
valoresBig5=valores("resultadosImgBig5")
valoresRed10=valores("resultadosImgRed10")
valoresBig10=valores("resultadosImgBig10")
valoresRed15=valores("resultadosImgRed15")
valoresBig15=valores("resultadosImgBig15")

keys=range(1,10)

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("precision") 
plt.title("precision segun la cantidad de imagenes por personas, con 41 personas y 5 autovalores");
plt.plot(keys,valoresRed5[0],label='kNN,imgs red ');
plt.plot(keys,valoresRed5[1],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig5[0],label='kNN,imgs big ');
plt.plot(keys,valoresBig5[1],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();



plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("precision") 
plt.title("precision segun la cantidad de imagenes por personas, con 41 personas y 10 autovalores");
plt.plot(keys,valoresRed10[0],label='kNN,imgs red ');
plt.plot(keys,valoresRed10[1],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig10[0],label='kNN,imgs big ');
plt.plot(keys,valoresBig10[1],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("recall")
plt.title("recall segun la cantidad de imagenes por personas, con 41 personas y 5 autovalores");
plt.plot(keys,valoresRed5[2],label='kNN,imgs red ');
plt.plot(keys,valoresRed5[3],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig5[2],label='kNN,imgs big ');
plt.plot(keys,valoresBig5[3],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("recall")
plt.title("recall segun la cantidad de imagenes por personas, con 41 personas y 10 autovalores");
plt.plot(keys,valoresRed10[2],label='kNN,imgs red ');
plt.plot(keys,valoresRed10[3],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig10[2],label='kNN,imgs big ');
plt.plot(keys,valoresBig10[3],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("specificity")
plt.title("specificity segun la cantidad de imagenes por personas, con 41 personas y 5 autovalores");
plt.plot(keys,valoresRed5[4],label='kNN,imgs red ');
plt.plot(keys,valoresRed5[5],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig5[4],label='kNN,imgs big ');
plt.plot(keys,valoresBig5[5],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();


plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("specificity")
plt.title("specificity segun la cantidad de imagenes por personas, con 41 personas y 10 autovalores ");
plt.plot(keys,valoresRed10[4],label='kNN,imgs red ');
plt.plot(keys,valoresRed10[5],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig10[4],label='kNN,imgs big ');
plt.plot(keys,valoresBig10[5],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("f1")
plt.title("f1 segun la cantidad de imagenes por personas, con 41 personas y 5 autovalores");
plt.plot(keys,valoresRed5[6],label='kNN,imgs red ');
plt.plot(keys,valoresRed5[7],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig5[6],label='kNN,imgs big ');
plt.plot(keys,valoresBig5[7],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("f1")
plt.title("f1 segun la cantidad de imagenes por personas, con 41 personas y 10 autovalores");
plt.plot(keys,valoresRed10[6],label='kNN,imgs red ');
plt.plot(keys,valoresRed10[7],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig10[6],label='kNN,imgs big ');
plt.plot(keys,valoresBig10[7],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("hitrate")
plt.title("hitrate segun la cantidad de imagenes por personas, con 41 personas y 5 autovalores");
plt.plot(keys,valoresRed5[8],label='kNN,imgs red ');
plt.plot(keys,valoresRed5[9],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig5[8],label='kNN,imgs big ');
plt.plot(keys,valoresBig5[9],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();


plt.xlabel("cantidad de imagenes por personas")
plt.ylabel("hitrate")
plt.title("hitrate segun la cantidad de imagenes por personas, con 41 personas y 10 autovalores");
plt.plot(keys,valoresRed10[8],label='kNN,imgs red ');
plt.plot(keys,valoresRed10[9],label='kNN pesado,imgs red ');
plt.plot(keys,valoresBig10[8],label='kNN,imgs big ');
plt.plot(keys,valoresBig10[9],label='kNN pesado,imgs big ');
plt.legend(bbox_to_anchor=(1.1,0.4));
plt.show();

