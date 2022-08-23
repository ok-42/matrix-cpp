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
    this->values = arr;
}

Matrix::Matrix(int rows, int columns, double** values) {
    this->rows = rows;
    this->columns = columns;
    this->values = values;
}

void Matrix::fill_random() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> distrib(1, 100);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++)
            this->values[i][j] = distrib(gen);
    }
}

double& Matrix::operator()(int r, int c) {
    if (r >= this->rows or c >= this->columns) {
        throw "Index is out of bounds";
    }
    return this->values[r][c];
}

void Matrix::print() {
    for (int i = 0; i < this->rows; i++) {
        for (int j = 0; j < this->columns; j++) {
            cout << this->values[i][j] << "\t";
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
    double** data_a = new double* [3];
    data_a[0] = new double[2] {1, 2};
    data_a[1] = new double[2] {4, 6};
    data_a[2] = new double[2] {3, 2};

    double** data_b = new double* [2];
    data_b[0] = new double[3] {8, 1, 3};
    data_b[1] = new double[3] {5, 7, 2};

    Matrix a = Matrix(3, 2, data_a);
    Matrix b = Matrix(2, 3, data_b);

    cout << "Matrix A:\n";
    a.print();

    cout << "Matrix B:\n";
    b.print();

    Matrix result = multiply(a, b);

    cout << "Result\n";
    result.print();

    return 0;
}
