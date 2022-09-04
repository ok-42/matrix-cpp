#include <iostream>
#include "vector.h"

using namespace std;

Vector::Vector(int length, double *values) {
    this->length = length;
    this->values = values;
}

void Vector::print() const {
    for (int i = 0; i < this->length; i++)
        cout << this->values[i] << "\t";
    cout << "\n";
}

Vector make_vector(int length, double* values) {
    double* copy = new double[length];
    for (int i = 0; i < length; ++i) {
        copy[i] = values[i];
    }
    return Vector(length, copy);
}

void print_vector(Vector vector) {
    vector.print();
}
