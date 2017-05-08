#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>

using namespace std;

#include "pgmb_io.hpp"

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

vector<vector<double> > trasponer(const vector<vector<double> >  &matriz, int filas, int cols){
	vector<vector<double> > traspuesta(cols, vector<double>(filas));

	for (int i = 0; i < cols; i++)
		for (int j = 0; j < filas; j++)
			traspuesta[i][j] = matriz[j][i];

	return traspuesta;
}

int main(int args, char* argsv[]){
	// Para probar, el argumento es la dir de una imagen
	// int fils, cols;
	// unsigned char maxG;
	// vector<double> imagen;
	// if(pgmb_read(argsv[1], fils, cols, maxG, imagen)){
	// 	cout << "Error al leer el archivo" << endl;
	// 	return 1;
	// }

	// cout << "Filas: " << to_string(fils) << endl;
	// cout << "Cols: " << to_string(cols) << endl;

	// for(int i = 0; i < fils * cols; i++){
	// 	if (i % fils == fils - 1)
	// 		cout << to_string(imagen[i]) + " " << endl;
	// 	else	
	// 		cout << to_string(imagen[i]) + " ";
	// }

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
	//Matriz donde cada fila corresponde a una imagen distinta
	//Dividiendo la posicion por nimgp (y sumando 1) obtengo a qué persona pertenece la imagen
	//Cada fila es un vector de tamaño m = fils * cols

	//Cargo cada imagen en memoria:
	for (int i = 0; i < p; i++){
		getline(entrada, linea);
		datos = split(linea, ' ');
		for (int j = 1; j <= nimgp; j++){
			string file = path + datos[0] + datos[j] + ".pgm";
			if (pgmb_read(file, fils, cols, maxG, X[pos])){
				cout << "Error al leer el archivo " << file << endl;
				return 1;
			}
			pos++;
		}
	}
	//Creo una copia para calcular la transformacion caracteristica de los vectores imagen despues
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
		}
	}

	//Calculo la traspuesta de X
	vector<vector<double> > X_t = trasponer(X, n, m);

	//Ahora hay que hacer X_t * X
	//Podemos hacer un archivo aparte con todas las operaciones de matrices (si hace falta)

	getline(entrada, linea);
	int ntest = stoi(linea);			// Cantidad de imagenes a testear
	for (int i = 0; i < ntest; i++){
		getline(entrada, linea);
		datos = split(linea, ' ');
		string path_test = datos[0];
		int persona = stoi(datos[1]);
		vector<double> imagen(fils * cols);
		if (pgmb_read(path_test, fils, cols, maxG, imagen)){
			cout << "Error al leer el archivo de prueba " << path_test << endl;
			return 1;
		}

		//Aca hay que hacer la magia y ver si le embocamos a "persona"
	}

	// Aca se escribe el archivo de salida, con las raices cuadradas de los k autovalores

	return 0;
}