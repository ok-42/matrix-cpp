#include <iostream>
#include <random>
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
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 100);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++)
            this->data[i][j] = distrib(gen);
    }
}

double& Matrix::operator()(int r, int c) {
    if (r >= this->rows or c >= this->columns) {
        throw "Index is out of bounds";
    }
    return data[r][c];
}

void Matrix::print() {
    for (int i = 0; i < this->rows; i++) {
        for (int j = 0; j < this->columns; j++) {
            cout << this->data[i][j] << "\t";
        }
        cout << "\n";
    }
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
    result.print();

    return 0;
}
