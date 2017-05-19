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

vector<double> transformacionCaracteristica(const vector<vector<double> > &autoVectores, const vector<double> &imagen, int k, int sizeImg){
	vector<double> tc(k);
	for(int i = 0; i < k; i++)
		tc[i] = matrices::producto_escalar(autoVectores[i], imagen, sizeImg);	

	return tc;
}

int encontrarPersona(const vector<vector<double> > &tc, const vector<double> &tc_check, int cantImg, int cantVectores, int knn, int nimgp, int cantPersonas,int norma){

	std::priority_queue<par> cola;
	for (int i = 0; i < cantImg; i++){
		vector<double> resta = matrices::restarVector(tc[i], tc_check, cantVectores);
		par p = {i, matrices::norma_v(resta, cantVectores, norma)};
		cola.push(p);
	}

	vector<double> personas(cantPersonas, 0);
	//personas[(cola.top().a) / nimgp] += 1;	
	for (int i = 0; i < knn; i++){
		personas[(cola.top().a) / nimgp] += 1;
/*		if(i==0){
			personas[(cola.top().a) / nimgp] += (2.0/3.0);	
		}
		else if(i==1){
			personas[(cola.top().a) / nimgp] += (1.0/6.0);	
		}		
		else{
			personas[(cola.top().a) / nimgp] += ((1.0/(6.0))*(knn-2));
		}*/
		//cout<<((cola.top().a) / nimgp)+1<<" "<<cola.top().b <<endl;
		cola.pop();

	}

	int maxComun = 0;
	for (int i = 0; i < cantPersonas; i++){
		if (personas[maxComun] < personas[i])
			maxComun = i;
	}
	
	return maxComun;
}

int encontrarPersonaHamming(const vector<vector<double> > &tc, const vector<double> &tc_check, int cantImg, int cantVectores, int knn, int nimgp, int cantPersonas,int cota){

	std::priority_queue<par> cola;
	for (int i = 0; i < cantImg; i++){
		vector<double> resta = matrices::restarVector(tc[i], tc_check, cantVectores);
		for(int j=0;j<cantVectores;j++){
			if(abs(resta[j])<cota){
				resta[j]=0;
			}
			else{
				resta[j]=1;
			}
		}
		par p = {i, matrices::norma_v(resta, cantVectores, 1)};
		cola.push(p);
	}

	vector<int> personas(cantPersonas, 0);
	personas[(cola.top().a) / nimgp] += 1;	
	for (int i = 0; i < knn; i++){
		personas[(cola.top().a) / nimgp] += 1;		
		//cout<<((cola.top().a) / nimgp)+1<<" "<<cola.top().b <<endl;
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

	vector<vector<double> > tc(n, vector<double>(k));
	vector<int> parecidos(1001,0);
	//Matriz de n x k donde cada fila es el vector de la tc de cada imagen
	for(int i = 0; i < n; i++)
	 	tc[i] = transformacionCaracteristica(autoVectores, imagenes[i], k, m);
	
	getline(entrada, linea);
	int ntest = stoi(linea);			// Cantidad de imagenes a testear
	int exitosDis = 0;
	int exitosMan = 0;
	int exitosHam = 0;
	
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
		
		int parecidoMan = encontrarPersona(tc, tc_check, n, k,nimgp, nimgp, p,1);
		int parecidoDis = encontrarPersona(tc, tc_check, n, k,nimgp, nimgp, p,2);
		int parecidoHam = encontrarPersonaHamming(tc, tc_check, n, k,nimgp, nimgp, p,750);	
			
		parecidoMan++;
		parecidoDis++;
		parecidoHam++;
		cout<< endl;
		if (parecidoMan != persona){
			cout << path_test + " Manhattan NO coincide. Persona: " + to_string(persona) + ". Parecido: " + to_string(parecidoMan) << endl;
		}else{
			cout << to_string(persona) +" OK Con Manhattan" << endl;	
			exitosMan++;
		}
		if (parecidoDis != persona){
			cout << path_test + " Norma 2 NO coincide. Persona: " + to_string(persona) + ". Parecido: " + to_string(parecidoDis) << endl;
		}else{
			cout << to_string(persona) +" OK Con Norma 2" << endl;	
			exitosDis++;
		}
		if (parecidoHam != persona){
			cout << path_test + " Hamming NO coincide. Persona: " + to_string(persona) + ". Parecido: " + to_string(parecidoHam) << endl;
		}else{
			cout << to_string(persona) +" OK Con Hamming" << endl;	
			exitosHam++;
		}
		
	}
	
	
	cout << "#Exitos Norma 2: " + to_string(exitosDis) << endl;
	cout << "#Exitos Manhattan : " + to_string(exitosMan) << endl;
	cout << "#Exitos Hamming : " + to_string(exitosHam) << endl;
	
	ofstream archivoSalida;
	archivoSalida.open(argsv[2]);
	for(int i = 0; i < k; i++){
		cout << "sqrt(Autovalor " + to_string(i + 1) + "): " + to_string(sqrt(autoValores[i])) << endl;
		archivoSalida << to_string(sqrt(autoValores[i])) + "\n";	
	}
	archivoSalida.close();	

	return 0;
}




