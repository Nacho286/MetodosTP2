using namespace std;

#define LIMITE 100
#define UMBRAL 1.0e-2
#define PASO_CONVERGENCIA 10

namespace matrices{

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

	// v * v_t = C (n x n)
	vector<vector<double> > multiplicar(const vector<double>  &v, const vector<double>  &v_t, int n){
		vector<vector<double> > C(n, vector<double>(n));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				C[i][j] = v[i] * v_t[j];

		return C;
	}

	// A (n x m) * v (m x 1) = w (n x 1)
	vector<double> multiplicar(const vector<vector<double> >  &A, const vector<double> &v, int n, int m){
		vector<double> w(n);
		for (int i = 0; i < n; i++){
			double sum = 0.0;
			for (int j = 0; j < m; j++)
				sum += A[i][j] * v[j];
			w[i] = sum;
		}

		return w;
	}

	// A * lambda
	void multipicar_por_escalar(vector<vector<double> > &A, double lambda, int n, int m){
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)				
				A[i][j] *= lambda;
	}

	// A (n x m) + B (n x m) = C (n x m)
	vector<vector<double> > sumar(const vector<vector<double> > &A, const vector<vector<double> > &B, int n, int m){
		vector<vector<double> > C(n, vector<double>(m));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)		
				C[i][j] = A[i][j] + B[i][j];

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

	void normalizar(vector<double> &v, int n){
			double norma2 = norma_v(v, n, 2);			
			for (int j = 0; j < n; j++)
				v[j] = v[j] / norma2;
	}

	//A (n x m), v (m x 1), k = cant. de iteraciones
	//Necesariamente n = m; caso contrario, no coincide la dimension de Av (n x 1) con v (m x 1)
	//Esto implica que el metodo de la potencia solo esta definido para matrices cuadradas?
	//--En clase vimos para cuadradas creo.
	//v es el autovector del autovalor que se devuelve. Por que tiene sentido?
	double metodo_potencia(const vector<vector<double> >  &A, vector<double> &v, int n, int m, int k){
		for (int i = 0; i < k; i++){
			vector<double> Av = multiplicar(A, v, n, m);
			normalizar(Av, n);
			v = Av;
		}

		vector<double> Av = multiplicar(A, v, n, m);

		double v_t_Av  = producto_escalar(v, Av, n);
		double v_t_v   = producto_escalar(v, v, n);		// Esto equivale a la norma 2 de v al cuadrado 

		double lambda = v_t_Av / v_t_v;

		return lambda;
	}

	double autoValorMaximo(const vector<vector<double> >  &A, vector<double> &v, int n, int m){
		//Algo que no esta bueno es que el metodo tiene que calcular de vuelta todas las matrices...
		//Este metodo se podría usar como heuristica para encontrar un k adecuado. 
		//Habria que ver si ese k sirve para todo autovalor de la matriz.
		double anterior = 0.0;
		for (int k = PASO_CONVERGENCIA; k <= LIMITE; k += PASO_CONVERGENCIA){
			double actual = metodo_potencia(A, v, n, m, k);
			// Para la primera iteracion:
			// Qué pasa si actual es realmente chico pero no es el autovalor que buscamos?
			if (abs(actual - anterior) < UMBRAL)
				return actual;
			else
				anterior = actual;
		}
	}

	vector<vector<double> > deflacion(const vector<vector<double> > &A, const vector<double> &v, int n, double lambda){
		vector<vector<double> > B = multiplicar(v, v, n);
		multipicar_por_escalar(B, -lambda, n, n);

		return sumar(A, B, n, n);
	}

	// alpha determina cuantos autovalores/autovectores se encuentran
	// V (alpha x n) = matriz donde cada fila es un autovector de M distinto
	vector<double> encontrarAutovalores(const vector<vector<double> > &A, vector<vector<double> > &V, int n, int alpha){
		vector<double> lst_autovalores(alpha);
		vector<vector<double> > A_i = A;

		//Uso while porque for da a entender que estamos recorriendo algo
		int i = 0;
		while (i < alpha){
			//X_0 vector con elementos aleatorios entre 0 y 1
			//Esto disminuye la probabilidad de que resulte ortogonal al autovector que queremos encontrar
			vector<double> x_0(n);
			for (int j = 0; j < n; j++){
				double r = ((double) rand() / RAND_MAX);
				x_0.push_back(r);
			}
			double lambda_i = autoValorMaximo(A_i, x_0, n, n);
			V.push_back(x_0);							
			lst_autovalores.push_back(lambda_i);
			A_i = deflacion(A_i, x_0, n, lambda_i);
			i++;
		}

		return lst_autovalores;
	}
}  