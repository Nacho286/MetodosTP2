using namespace std;

namespace matrices{

	#define LIMITE 100;
	#define UMBRAL  1.0e-2;
	#define PASO_CONVERGENCIA 10;
	vector<vector<double> > trasponer(const vector<vector<double> >  &matriz, int filas, int cols){
		vector<vector<double> > traspuesta(cols, vector<double>(filas));
		for (int i = 0; i < cols; i++)
			for (int j = 0; j < filas; j++)
				traspuesta[i][j] = matriz[j][i];

		return traspuesta;
	}

	// A (n x m) * B (m x n) = C (n x n)
	vector<vector<double> > multiplicar(const vector<vector<double> >  &A, const vector<vector<double> >  &B, int n, int m){
		vector<vector<double> > C(n, vector<double>(n));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				double sum = 0.0;
				for (int k = 0; k < m; k++)
					sum += A[i][k] * B[k][j];
				C[i][j] = sum;
			}
		}

		return C;
	}

	// v*vt = C(nxn)
	vector<vector<double> > multiplicar(const vector<double>  &v1, const vector<double>  &v2, int n){
		vector<vector<double> > C(n, vector<double>(n));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){				
					elem += v1[i] * v2[j];
					C[i][j] = elem;
			}
		}
		return C;
	}


	// A (n x m) * v (m x 1) = w (n x 1)
	//--se podria hacer overloading

	vector<double> multiplicar_vector(const vector<vector<double> >  &A, const vector<double> &v, int n, int m){
		vector<double> w(n);
		for (int i = 0; i < n; i++){
			double sum = 0.0;
			for (int j = 0; j < m; j++)
				sum += A[i][j] * v[j];
			w[i] = sum;
		}

		return w;
	}

	//En teoria modifica la referencia de A. Podría hacerse una copia, pero no le veo demasiado sentido
	vector<vector<double> > multipicar_por_escalar(vector<vector<double> > &A, const int lambda,int n, int m){
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){				
					A[i][j] *= lambda ;
			}
		}	
		return A;
	}

	vector<vector<double> > suma(const vector<vector<double> > &A, const vector<vector<double> > &B, int n){
		vector<vector<double> > C(n, vector<double>(n));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){				
					Ci][j] = A[i][j] + B[i][j];
			}
		}	
		return C;
	}


	double norma_v(const vector<double> &v, int n, int p){
		double res = 0.0;
		for (int i = 0; i < n; i++)
			res += pow(abs(v[i]), p);

		return sqrt(res);
	}

	//v_t (1 x n) * w (n x 1) = a (1 x 1)
	double producto_escalar(const vector<double> &v, const vector<double> &w, int n){
		double res = 0.0;
		for (int i = 0; i < n; i++)
			res += v[i] * w[i];

		return res;
	}


	//A (n x m), v (m x 1), k = cant. de iteraciones
	//Necesariamente n = m; caso contrario, no coincide la dimension de Av (n x 1) con v (m x 1)
	//Esto implica que el metodo de la potencia solo esta definido para matrices cuadradas?
	//--En clase vimos para cuadradas creo.
	vector<double> normalizar(const vector<double> &v){

			//Normalizo al vector
			//Aca es muy importante que n = m, sino no funciona ni a palos
			double norma_v = norma_v(v, v.size(), 2);			
			for (int j = 0; j < n; j++)
				v[j] = v[j] / norma_v;
	}

	//v es el autovector del autovalor que se devuelve. Por que tiene sentido?
	double metodo_potencia(const vector<vector<double> >  &A, vector<double> &v, int n, int m, int k){
		for (int i = 0; i < k; i++){
			vector<double> Av = multiplicar_vector(A, v, n, m);

			double norma_Av = norma_v(Av, n, 2);

			//Normalizo al vector
			//Aca es muy importante que n = m, sino no funciona ni a palos
			for (int j = 0; j < n; j++)
				v[j] = Av[j] / norma_Av;
			//v = normalizar(Av);

		 }

		vector<double> Av = multiplicar_vector(A, v, n, m);
		double v_Av  = producto_escalar(v, Av, n);
		double v_t_v = producto_escalar(v, v, n);

		double lambda = v_Av / v_t_v;

		return lambda;
	}

	double autoValorMaximo(const vector<vector<double> >  &A, vector<double> &v, int n, int m){
		//Algo que no esta bueno es que el metodo tiene que calcular de vuelta todas las matrices...
		//Este metodo se podría usar como heuristica para encontrar un k adecuado. 
		//Habria que ver si ese k sirve para todo autovalor de la matriz.
		double anterior = 0;
		for(int k = 0; k < LIMITE;k+=PASO_CONVERGENCIA){
			double actual =  metodo_potencia(A,v,n,m,k)
			if(abs(actual -  anterior) < UMBRAL)
				return actual;
			else
				anterior = actual;
		}

	}

	vector<vector<double> > deflacion(const vector<vector<double> > &A, vector<double> &V, int n , int m, int lambda){
		return suma(A,multipicar_por_escalar(-lambda,multiplicar(v,v,n)));


	vector<double> encontrarAutovalores(const vector<vector<double> > &A, int n, vector<vector<double> > &V){
		vector<double> lst_autovalores(n); 
		//Deberia ser aleatorio
		//Uhm...
		vector<vector<double> > A_i(A);
		for(int i ⁼ 0; i<n;i++){
			//X_0 un vector cualquiera que tenga la primer coordenada en la base de autovectores no nula. En principio, este podria no andar...
			vector<double> x_0(n,1);
			lambda_i = autoValorMaximo(A_i,x_0,n,n);
			V.push_back(x_0);
			lst_autovalores.push_back(lambda_i);
			A_i = deflacion(A_i,v,n,n,lambda_i);
		}
		return lst_autovalores;

	}




}  