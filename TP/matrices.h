using namespace std;

#define LIMITE 1000
#define UMBRAL 1.0e-7

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

	
	// A (n x m) - B (n x m) = C (n x m)
	vector<vector<double> > restar(const vector<vector<double> > &A, const vector<vector<double> > &B, int n, int m){
		vector<vector<double> > C(n, vector<double>(m));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)		
				C[i][j] = A[i][j] - B[i][j];

		return C;
	}

	// A (m x 1) - B (m x 1) = C (m x 1)
	vector<double> restarVector(const vector<double> &A, const vector<double> &B, int m){
		vector<double>  C(m);
		for (int i = 0; i < m; i++)
			C[i] = A[i] - B[i];

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

	vector<double> normalizar(const vector<double> &v, int n){
			vector<double> res(n);
			double norma2 = norma_v(v, n, 2);			
			for (int j = 0; j < n; j++)
				res[j] = v[j] / norma2;

			return res;
	}

	//A (n x m), v (m x 1)
	//Necesariamente n = m; caso contrario, no coincide la dimension de Av (n x 1) con v (m x 1)
	double metodo_potencia(const vector<vector<double> >  &A, vector<double> &v, int n, int m){
		double anterior = 0.0;
		double actual = 0.0;

		for (int i = 0; i < LIMITE; i++){
			vector<double> Av = multiplicar(A, v, n, m);
			v = normalizar(Av, n);

			Av = multiplicar(A, v, n, m);

			double v_t_Av  = producto_escalar(v, Av, n);
			double v_t_v   = producto_escalar(v, v, n);		// Esto equivale a la norma 2 de v al cuadrado 

			actual = v_t_Av / v_t_v;

			if (abs(actual - anterior) < UMBRAL){
				cout << "#Iteraciones: " + to_string(i) << endl;
				return actual;
			}else
			 	anterior = actual;
		}

		return actual;
	}

	vector<vector<double> > deflacion(const vector<vector<double> > &A, const vector<double> &v, int n, double lambda){
		vector<vector<double> > B = multiplicar(v, v, n);
		multipicar_por_escalar(B, -lambda, n, n);

		return sumar(A, B, n, n);
	}

	// alpha determina cuantos autovalores/autovectores se encuentran
	// V (alpha x n) = matriz donde cada fila es un autovector de M distinto
	vector<double> encontrarAutovalores(vector<vector<double> > &A, vector<vector<double> > &V, int n, int alpha){
		vector<double> lst_autovalores(alpha);
		
		//Declaro el vector por fuera del bucle porque sino se indefine cuando se sale del scope para llamar a "metodo_potencia"
		vector<double> x_0(n);

		int i = 0;
		while (i < alpha){
			//X_0 vector con elementos aleatorios entre 0 y 1
			//Esto disminuye la probabilidad de que resulte ortogonal al autovector que queremos encontrar
			for (int j = 0; j < n; j++){
				double r = ((double) rand() / RAND_MAX);
				x_0[j] = r;
			}
			double lambda_i = metodo_potencia(A, x_0, n, n);
			V[i] = x_0;
			lst_autovalores[i] = lambda_i;						
			A = deflacion(A, x_0, n, lambda_i);
			i++;
		}

		return lst_autovalores;
	}
}  
