#include <Python.h>

static PyObject* square_square(PyObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n)) return NULL;
    long long res = (long long)n * (long long)n;
    return PyLong_FromLongLong(res);
}

static PyMethodDef SquareMethods[] = {
    {"square", square_square, METH_VARARGS, "Return square of integer."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT,
    "csquare",
    "CSquare module",
    -1,
    SquareMethods
};

PyMODINIT_FUNC PyInit_csquare(void) {
    return PyModule_Create(&squaremodule);
}
