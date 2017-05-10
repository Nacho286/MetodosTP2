using namespace std;

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

	// A (n x m) * v (m x 1) = w (n x 1)
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
	double metodo_potencia(const vector<vector<double> >  &A, vector<double> &v, int n, int m, int k){
		for (int i = 0; i < k; i++){
			vector<double> Av = multiplicar_vector(A, v, n, m);

			double norma_Av = norma_v(Av, n, 2);

			//Normalizo al vector
			//Aca es muy importante que n = m, sino no funciona ni a palos
			for (int j = 0; j < n; j++)
				v[j] = Av[j] / norma_Av;
		}

		vector<double> Av = multiplicar_vector(A, v, n, m);
		double v_Av  = producto_escalar(v, Av, n);
		double v_t_v = producto_escalar(v, v, n);

		double lambda = v_Av / v_t_v;

		return lambda;
	}
}