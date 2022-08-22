#include <iostream>

using namespace std;


class Matrix {

    public:

    double** data;
    int rows, columns;

    Matrix(int rows, int columns);
    void fill_random();
    double& operator()(int r, int c);
};

extern "C" {
    Matrix multiply(Matrix a, Matrix b);
    int main();
}
