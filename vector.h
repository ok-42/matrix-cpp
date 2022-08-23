class Vector {
public:
    int length;
    double* values;

    Vector(int length, double* values);
    void print() const;
};

extern "C" {
    Vector make_vector(int length, double* values);
}
