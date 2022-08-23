#include <iostream>
#include "vector.h"

using namespace std;


class Matrix {
public:
    int rows, columns;
    double** values;

    Matrix(int rows, int columns);
    Matrix(int rows, int columns, double** values);
    void fill_random();
    void print();
    double& operator()(int r, int c);
};

extern "C" {
    Matrix multiply(Matrix a, Matrix b);
    int main();
}
