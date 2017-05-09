using namespace std;

namespace matrices{

	vector<vector<double> > trasponer(const vector<vector<double> >  &matriz, int filas, int cols){

		vector<vector<double> > traspuesta(cols, vector<double>(filas));
		for (int i = 0; i < cols; i++)
			for (int j = 0; j < filas; j++)
				traspuesta[i][j] = matriz[j][i];

		return traspuesta;
	}

	// A (mxn) * B (nxm) = C (mxm)
	vector<vector<double> > multiplicar(const vector<vector<double> >  &A, const vector<vector<double> >  &B, int n, int m){
		vector<vector<double> > C(m, vector<double>(m));
		for (int i = 0; i < m; i++){
			for (int j = 0; j < m; j++){
				double sum = 0.0;
				for (int k = 0; k < n; k++)
					sum += A[i][k] * B[k][j];
				C[i][j] = sum;
			}
		}

		return C;
	}
}