#include <iostream>
#include "main.h"

using namespace std;


Matrix::Matrix(int rows, int columns) {
    this->rows = rows;
    this->columns = columns;
    double** arr = new double* [rows];
    for (int i = 0; i < rows; i++)
        arr[i] = new double[columns];
    this->data = arr;
}

void Matrix::fill_random() {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++)
            this->data[i][j] = rand() % 100;
    }
}

double& Matrix::operator()(int r, int c) {
    if (r >= this->rows or c >= this->columns) {
        throw "Index is out of bounds";
    }
    return data[r][c];
}



Matrix multiply(Matrix a, Matrix b) {

    Matrix result = Matrix(a.rows, b.columns);

    if (a.columns != b.rows) {
        throw "Wrong dimensionality";
    }

    for (int i = 0; i < a.rows; i++) {
        for (int j = 0; j < b.columns; j++) {
            double dot_product = 0.0f;
            for (int k = 0; k < a.columns; k++) {
                dot_product += a(i, k) * b(k, j);
            }
            result(i, j) = dot_product;
        }
    }
    return result;
}


int main() {

    Matrix a = Matrix(3, 2);
    Matrix b = Matrix(2, 4);

    a.fill_random();
    b.fill_random();

    Matrix result = multiply(a, b);

    for (int i = 0; i < a.rows; i++) {
        for (int j = 0; j < b.columns; j++) {
            cout << result(i, j) << "\t";
        }
        cout << "\n";
    }
    return 0;
}
