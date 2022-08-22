#include <iostream>

using namespace std;

class Vector {
public:
    int length;
    double* data;

    Vector(int length, double* values);
    void print() const;
};

class Matrix {

    public:

    double** data;
    int rows, columns;

    Matrix(int rows, int columns);
    Matrix(int rows, int columns, double** data);
    void fill_random();
    void print();
    double& operator()(int r, int c);
};

extern "C" {
    Matrix multiply(Matrix a, Matrix b);
    int main();
}
