#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <utility>
#include <queue>

using namespace std;

#include "matrices.h"
#include "pgmb_io.hpp"

struct par{
	int a;
    double b;
    bool operator<(const par& rhs) const
    {
        return b > rhs.b;
    }
};

bool isZero(double value){
	return (abs(value) <= 1.0e-7);
}

template<typename Out>
void split(const string &s, char delim, Out result) {
	stringstream ss;
	ss.str(s);
	string item;
	while (getline(ss, item, delim))
    	*(result++) = item;
}

vector<string> split(const string &s, char delim) {
	vector<string> elems;
	split(s, delim, back_inserter(elems));
	return elems;
}

// En cada posicion del vector hay una tabla de 2x2 (interpretada como vector fila) de confusion
// Es decir [tp, fn, fp, tn]
vector<vector<double> >	tablasDeConfusion(const vector<vector<double> > m, int size){
	vector<vector<double> > tablas(size, vector<double>(4));

	for (int i = 0; i < size; i++){
		vector<double> t_kunfusion(4);
		t_kunfusion[0] = m[i][i]; //tp

		for (int j = 0; j < size; j++)
			if(j != i)
				t_kunfusion[1] += m[i][j]; //fn

		for (int k = 0; k < size; k++)
			if(k != i)
				t_kunfusion[2] += m[k][i]; //fp

		for (int r = 0; r < size; r++)
			for (int s = 0; s < size; s++)
				if(s !=i && r != i)
					t_kunfusion[3] += m[r][s]; //tn
		tablas[i]= (t_kunfusion);
	}

	return tablas;
}

void calcularMetricas(vector<vector<double> > &t, vector<double> &r, int p){
	for (int i = 0; i < p; i++){
 		//precision_i
 		if (t[i][0] != 0) //hay algun tp
 			r[0] += t[i][0] / (t[i][0] + t[i][2]) / (double) p;
 		else if (t[i][2] != 0)
 			r[0] += 0.0;
 		else
 			r[0] += 1.0 / (double) p;

 		//recall_i
 		if (t[i][0] != 0)	//hay algun tp
 			r[1] += t[i][0] / (t[i][0] + t[i][1]) / (double) p;
 		else if (t[i][1] !=0)
 			r[1] += 0;
 		else
 			r[1] += 1/(double)p;

 		//specificity_i
 		if (t[i][3] != 0) //hay algun fp
 			r[2] += t[i][3] / (t[i][3] + t[i][2]) / (double) p;
 		else if (t[i][2] != 0)
 			r[2] += 0.0;
 		else
 			r[2] += 1.0 / (double) p;
 		//f1_i
	}

	r[3] += ((2* ((r[0] * r[1]) / (r[0] + r[1]))));

 }

vector<double> transformacionCaracteristica(const vector<vector<double> > &autoVectores, const vector<double> &imagen, int k, int sizeImg){
	vector<double> tc(k);
	for(int i = 0; i < k; i++)
		tc[i] = matrices::producto_escalar(autoVectores[i], imagen, sizeImg);

	return tc;
}

int encontrarPersona(const vector<vector<double> > &tc, const vector<double> &tc_check, int cantImg, int cantVectores, int knn, int nimgp, int cantPersonas, int norma){
	priority_queue<par> cola;
	for (int i = 0; i < cantImg; i++){
		vector<double> resta = matrices::restar(tc[i], tc_check, cantVectores);
		par p = {i, matrices::norma_v(resta, cantVectores, norma)};
		cola.push(p);
	}

	vector<double> personas(cantPersonas, 0);
	for (int i = 0; i < knn; i++){
		personas[(cola.top().a) / nimgp] += 1;
		cola.pop();
	}

	int maxComun = 0;
	for (int i = 0; i < cantPersonas; i++){
		if (personas[maxComun] < personas[i])
			maxComun = i;
	}

	return maxComun;
}

int encontrarPersonaPeso(const vector<vector<double> > &tc, const vector<double> &tc_check, int cantImg, int cantVectores, int knn, int nimgp, int cantPersonas, int norma){
	priority_queue<par> cola;
	for (int i = 0; i < cantImg; i++){
		vector<double> resta = matrices::restar(tc[i], tc_check, cantVectores);
		par p = {i, matrices::norma_v(resta, cantVectores, norma)};
		cola.push(p);
	}

	vector<double> personas(cantPersonas, 0);
	personas[(cola.top().a) / nimgp] += 1;
	for (int i = 0; i < knn; i++){
		personas[(cola.top().a) / nimgp] += 1;
		cola.pop();
	}

	int maxComun = 0;
	for (int i = 0; i < cantPersonas; i++){
		if (personas[maxComun] < personas[i])
			maxComun = i;
	}

	return maxComun;
}

int encontrarPersonaModa(const vector<vector<double> > &tc, const vector<double> &tc_check, int cantImg, int cantVectores, int knn, int nimgp, int cantPersonas, int norma){
	priority_queue<par> cola;
	for (int i = 0; i < cantImg; i++){
		vector<double> resta = matrices::restar(tc[i], tc_check, cantVectores);
		par p = {i, matrices::norma_v(resta, cantVectores, norma)};
		cola.push(p);
	}

	vector<double> personas(cantPersonas, 0);
	for (int i = 0; i < knn; i++){
	if (i == 0){
			personas[(cola.top().a) / nimgp] += (2.0/3.0);
		} else if (i == 1){
			personas[(cola.top().a) / nimgp] += (1.0/6.0);
		}else{
			personas[(cola.top().a) / nimgp] += 1.0/(6.0*(knn-2));
		}
		cola.pop();
	}

	int maxComun = 0;
	for (int i = 0; i < cantPersonas; i++){
		if (personas[maxComun] < personas[i])
			maxComun = i;
	}

	return maxComun;
}

int encontrarPersonaHamming(const vector<vector<double> > &tc, const vector<double> &tc_check, int cantImg, int cantVectores, int knn, int nimgp, int cantPersonas, int cota){
	priority_queue<par> cola;
	for (int i = 0; i < cantImg; i++){
		vector<double> resta = matrices::restar(tc[i], tc_check, cantVectores);
		for (int j = 0; j < cantVectores; j++){
			if (abs(resta[j]) < cota)
				resta[j] = 0;
			else
				resta[j] = 1;
		}
		par p = {i, matrices::norma_v(resta, cantVectores, 1)};
		cola.push(p);
	}

	vector<int> personas(cantPersonas, 0);
	//personas[(cola.top().a) / nimgp] += 1;
	for (int i = 0; i < knn; i++){
		personas[(cola.top().a) / nimgp] += 1;
		cola.pop();
	}

	int maxComun = 0;
	for (int i = 0; i < cantPersonas; i++){
		if (personas[maxComun] < personas[i])
			maxComun = i;
	}

	return maxComun;
}

int main(int args, char* argsv[]){
	// Primer argumento: archivo de entrada, donde la primera linea especifica:
	// path de los datos, x, y, #personas, #imagenes por persona, #componentes principales
	string path, linea;
	int fils, cols, p, nimgp, k;
	unsigned char maxG;

	ifstream entrada;
	entrada.open(argsv[1]);
	getline(entrada, linea);
	vector<string> datos = split(linea, ' ');
	path  = datos[0];
	fils  = stoi(datos[1]);
	cols  = stoi(datos[2]);
	p 	  = stoi(datos[3]);
	nimgp = stoi(datos[4]);
	k     = stoi(datos[5]);

	int n = p * nimgp;
	int m = fils * cols;
	int pos = 0;
	vector<vector<double> > X (n, vector<double>(m));
	// Matriz de n x m donde cada fila corresponde a una imagen distinta
	//Dividiendo la posicion por nimgp (y sumando 1) obtengo a qué persona pertenece la imagen
	//Cada fila es un vector de tamaño m = fils * cols

	//Cargo cada imagen en memoria:
	for (int i = 0; i < p; i++){
		getline(entrada, linea);
		datos = split(linea, ' ');
		for (int j = 1; j <= nimgp; j++){
			string file = path + datos[0] + datos[j] + ".pgm";
			if (pgmb_read(file, fils, cols, maxG, X[pos], false)){
				cout << "Error al leer el archivo " << file << endl;
				return 1;
			}
			pos++;
		}
	}

	//Hago una copia de X para calcular la transformacion caracteristica despues
	vector<vector<double> > imagenes = X;

	//Calculo el promedio de las imagenes (se calcula por columnas)
	vector<double> mu(m, 0.0);
	for (int j = 0; j < m; j++){
		for (int i = 0; i < n; i++)
			mu[j] += X[i][j];
		mu[j] = mu[j] / n;
	}

	//Calculo los valores de X
	double raiz_n = sqrt(n - 1);
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			X[i][j] -= mu[j];
			X[i][j] = X[i][j] / raiz_n;
			if (isZero(X[i][j]))
				X[i][j] = 0.0;
		}
	}

	//Calculo la traspuesta de X
	vector<vector<double> > X_t = matrices::trasponer(X, n, m);

	//Calculo M; si existe un parametro mas = 1, hago la multiplicacion (X_t * X)
	int dim_M = n;
	if (args > 3 && stoi(argsv[3]) == 1)
		dim_M = m;

	vector<vector<double> > M(dim_M, vector<double>(dim_M));
	if (dim_M == m)
		M = matrices::multiplicar(X_t, X, m, n);
	else
		M = matrices::multiplicar(X, X_t, n, m);

	vector<vector<double> > autoVectores(k, vector<double>(dim_M));
	vector<double> autoValores = matrices::encontrarAutovalores(M, autoVectores, dim_M, k);

	//Si hice la cuenta al revés, calculo los autovectores que corresponden usar
	if (dim_M == n){
		vector<vector<double> > autoVectores_V(k, vector<double>(m));
		for (int i = 0; i < k; i++){
			vector<double> Xt_u_i = matrices::multiplicar(X_t, autoVectores[i], m, n);
			if (!isZero(autoValores[i])){
				for (int j = 0; j < m; j++)
					Xt_u_i[j] = Xt_u_i[j] / sqrt(autoValores[i]);
			}
			autoVectores_V[i] = Xt_u_i;
		}
		autoVectores.resize(k, vector<double>(m));
		autoVectores = autoVectores_V;
	}

	//Matriz de n x k donde cada fila es el vector de la tc de cada imagen
	vector<vector<double> > tc(n, vector<double>(k));

	//La matriz de confusion es cuadrada y la dimension corresponde a la cantidad de clases
	vector<vector<double> > matriz_kunfusionSinPeso(p, vector<double>(p));
	vector<vector<double> > matriz_kunfusionConPeso(p, vector<double>(p));
	vector<vector<double> > matriz_kunfusionModa(p, vector<double>(p));

	for(int i = 0; i < n; i++)
	 	tc[i] = transformacionCaracteristica(autoVectores, imagenes[i], k, m);

	// Reconocimiento de objetos
	bool objeto = false;
	if (args > 4 && stoi(argsv[4]) == 1) 
		objeto = true;

	// mu es un vector que ya contiene el promedio de las imagenes, nos cae gratis
	vector<double> tc_avg = transformacionCaracteristica(autoVectores, mu, k, m);

	// Obtengo la mayor diferencia entre la tc del promedio y las tc de las imágenes
	double cota_dis = 0.0;
	if (objeto){
		for (int i = 0; i < n; i++){
			double dif = matrices::norma_v(matrices::restar(tc[i], tc_avg, k), k, 2);
			if (dif > cota_dis)
				cota_dis = dif;
		}
	}

	getline(entrada, linea);
	int ntest = stoi(linea);			// Cantidad de imagenes a testear
	int exitosModa    = 0;
	//int exitosConPeso = 0;
	int exitosSinPeso = 0;
	int exitosObj 	  = 0;
	int tpObj, tnObj, fpObj, fnObj = 0;
	for (int i = 0; i < ntest; i++){
		getline(entrada, linea);
		datos = split(linea, ' ');
		string path_test = datos[0];
		int persona = stoi(datos[1]);
		vector<double> imagen(m);
		if (pgmb_read(path_test, fils, cols, maxG, imagen, false)){
			cout << "Error al leer el archivo de prueba " << path_test << endl;
			return 1;
		}
		vector<double> tc_check = transformacionCaracteristica(autoVectores, imagen, k, m);

		// Ahora se ejecuta una u otra operacion, dependiendo si se quiere clasificar un objeto o una persona
		if (!objeto){
			//int parecidoConPeso = encontrarPersonaPeso(tc, tc_check, n, k, nimgp, nimgp, p, 2);
			int parecidoModa = encontrarPersonaModa(tc, tc_check, n, k, nimgp, nimgp, p, 2);
			int parecidoSinPeso = encontrarPersona(tc, tc_check, n, k, nimgp, nimgp, p, 2);

			//parecidoConPeso++;
			parecidoModa++;
			parecidoSinPeso++;

			// if (parecidoConPeso != persona){
			// 	cout << path_test + " Con peso NO coincide. Persona: " + to_string(persona) + ". Parecido: " + to_string(parecidoConPeso) << endl;
			// 	matriz_kunfusionConPeso[persona - 1][parecidoConPeso - 1] += 1;
			// }else{
			// 	cout << to_string(persona) +" OK Con Peso" << endl;
			// 	exitosConPeso++;
			// 	matriz_kunfusionConPeso[persona - 1][persona - 1] += 1;
			// }
			if (parecidoModa != persona){
				cout << path_test + " Moda NO coincide. Persona: " + to_string(persona) + ". Parecido: " + to_string(parecidoModa) << endl;
				matriz_kunfusionModa[persona - 1][parecidoModa - 1] += 1;
			}else{
				cout << to_string(persona) +" OK Con Moda" << endl;
				exitosModa++;
				matriz_kunfusionModa[persona - 1][persona - 1] += 1;
			}
			if (parecidoSinPeso != persona){
				cout << path_test + " Sin Peso NO coincide. Persona: " + to_string(persona) + ". Parecido: " + to_string(parecidoSinPeso) << endl;
				matriz_kunfusionSinPeso[persona - 1][parecidoSinPeso - 1] += 1;
			}else{
				cout << to_string(persona) +" OK Sin Peso" << endl;
				exitosSinPeso++;
				matriz_kunfusionSinPeso[persona - 1][persona - 1] += 1;
			}
		} else{
			double dif = matrices::norma_v(matrices::restar(tc_check, tc_avg, k), k, 2);

			bool esPersona = true;
			if (dif > cota_dis)
				esPersona = false;

			if (persona == 1 && esPersona){
				cout << "CARA OK" << endl;
				tpObj++;
				exitosObj++;
			}else if (persona == 0 && esPersona){
				cout << path_test + " es OBJETO, predicho CARA." << endl;
				fpObj++;
			}else if (persona == 1 && !(esPersona)){
				cout << path_test + " es CARA, predicho OBJETO." << endl;
				fnObj++;
			}else{
				cout << "OBJETO OK" << endl;
				tnObj++;
				exitosObj++;
			}
		}
	}

	if (!objeto){
		//Reportar resultados: precision, recall, specifity, f1 (en ese orden)
		vector<vector<double> > tablasSinPeso(tablasDeConfusion(matriz_kunfusionSinPeso, p));
	 	//vector<vector<double> > tablasConPeso(tablasDeConfusion(matriz_kunfusionConPeso, p));
	 	vector<vector<double> > tablasModa(tablasDeConfusion(matriz_kunfusionModa, p));

	 	//[precision, recall, spec, f1]
	 	vector<double> resultadosSinPeso(4);
	 	//vector<double> resultadosConPeso(4);
	 	vector<double> resultadosModa(4);

	 	calcularMetricas(tablasSinPeso, resultadosSinPeso, p);
	 	//calcularMetricas(tablasConPeso, resultadosConPeso, p);
	 	calcularMetricas(tablasModa, resultadosModa, p);

	 	//[tp, fn, fp, tn]
	 	ofstream results;
		results.open("resultados.out");
		//formato resultados :  precision, recall, specificity, f1, hitrate
		for(int i = 0;i < 4; i++)
			results << resultadosSinPeso[i] << " ";
		results << double(exitosSinPeso) / double(ntest);
		results << endl;

		// for(int i = 0; i < 4; i++)
		// 	results << resultadosConPeso[i] << " ";
		// results << double(exitosConPeso) / double(ntest);
		// results << endl;

		for(int i = 0; i < 4; i++)
			results << resultadosModa[i] << " ";
		results << double(exitosModa) / double(ntest);
		results << endl;

		results.close();

		cout << "#Exitos Sin Peso: " + to_string(exitosSinPeso) << endl;
		//cout << "#Exitos Con Peso: " + to_string(exitosConPeso) << endl;
		cout << "#Exitos Con Moda: " + to_string(exitosModa)    << endl;
	} else{
		cout << "#Exitos: " + to_string(exitosObj) + "/" + to_string(ntest) << endl;
	 	ofstream results;
		results.open("resultados.out");
		// Formato resultados: precision, recall, specificity, hitrate.
		results << to_string(double(tpObj) / double(tpObj + fpObj)) << " ";
		results << to_string(double(tpObj) / double(tpObj + fnObj)) << " ";
		results << to_string(double(tnObj) / double(tnObj + fpObj)) << " ";
		results << double(exitosObj) / double(ntest);
		results.close();
	}

	ofstream archivoSalida;
	archivoSalida.open(argsv[2]);
	for(int i = 0; i < k; i++){
		cout << "sqrt(Autovalor " + to_string(i + 1) + "): " + to_string(sqrt(autoValores[i])) << endl;
		archivoSalida << to_string(sqrt(autoValores[i])) + "\n";
	}
	archivoSalida.close();

	return 0;
}
