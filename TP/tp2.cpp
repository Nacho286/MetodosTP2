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

int main(int args, char* argsv[]){
	// Para probar, el argumento es la dir de una imagen
	// int fils, cols;
	// unsigned char maxG;
	// unsigned char *g;
	// if(pgmb_read(argsv[1], fils, cols, maxG, &g)){
	// 	cout << "Error al leer el archivo" << endl;
	// 	return 1;
	// }

	// cout << "Filas: " << to_string(fils) << endl;
	// cout << "Cols: " << to_string(cols) << endl;

	// for(int i = 0; i < fils * cols; i++){
	// 	if (i % fils == fils - 1)
	// 		cout << to_string(g[i]) + " " << endl;
	// 	else	
	// 		cout << to_string(g[i]) + " ";
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

	int pos = 0;
	unsigned char *imagenes[p * nimgp];			// Arreglo de punteros donde se almacena la posicion del vector de cada imagen (en filas)
	//Haciendo módulo p de la posición se puede obtener a qué persona corresponde cada imagen
	//Recordar que p empieza en 1 y la posición en 0, por lo que habría que sumarle 1 para saber a quién corresponde.

	//Cargo cada imagen en memoria:
	for (int i = 0; i < p; i++){
		getline(entrada, linea);
		datos = split(linea, ' ');
		for (int j = 1; j <= nimgp; j++){
			string file = path + datos[0] + datos[j] + ".pgm";
			if (pgmb_read(file, fils, cols, maxG, &(imagenes[pos]))){
				cout << "Error al leer el archivo " << file << endl;
				return 1;
			}
			pos++;
		}
	}

	getline(entrada, linea);
	int ntest = stoi(linea);			// Cantidad de imagenes a testear
	for (int i = 0; i < ntest; i++){
		getline(entrada, linea);
		datos = split(linea, ' ');
		string path_test = datos[0];
		int persona = stoi(datos[1]);
		unsigned char *imagen;
		if (pgmb_read(path_test, fils, cols, maxG, &imagen)){
			cout << "Error al leer el archivo de prueba " << path_test << endl;
			return 1;
		}

		//Aca hay que hacer la magia y ver si le embocamos a "persona"
	}

	// Aca se escribe el archivo de salida, con las raices cuadradas de los k autovalores

	return 0;
}