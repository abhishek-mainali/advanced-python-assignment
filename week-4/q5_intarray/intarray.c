#include <Python.h>
#include <stdlib.h>

typedef struct {
    size_t size;
    int *data;
} IntArray;

static void intarray_capsule_destructor(PyObject *capsule) {
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(capsule, "IntArray");
    if (arr) {
        free(arr->data);
        free(arr);
    }
}

static PyObject* intarray_init(PyObject *self, PyObject *args) {
    Py_ssize_t size;
    if (!PyArg_ParseTuple(args, "n", &size)) return NULL;
    if (size < 0) {
        PyErr_SetString(PyExc_ValueError, "size must be non-negative");
        return NULL;
    }
    IntArray *arr = (IntArray *)malloc(sizeof(IntArray));
    if (!arr) return PyErr_NoMemory();
    arr->size = (size_t)size;
    arr->data = (int *)calloc(arr->size, sizeof(int));
    if (!arr->data) {
        free(arr);
        return PyErr_NoMemory();
    }
    PyObject *caps = PyCapsule_New((void *)arr, "IntArray", intarray_capsule_destructor);
    return caps;
}

static PyObject* intarray_set(PyObject *self, PyObject *args) {
    PyObject *caps;
    Py_ssize_t idx;
    int value;
    if (!PyArg_ParseTuple(args, "Oni", &caps, &idx, &value)) return NULL;
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(caps, "IntArray");
    if (!arr) {
        PyErr_SetString(PyExc_ValueError, "Invalid IntArray capsule");
        return NULL;
    }
    if (idx < 0 || (size_t)idx >= arr->size) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }
    arr->data[idx] = value;
    Py_RETURN_NONE;
}

static PyObject* intarray_get(PyObject *self, PyObject *args) {
    PyObject *caps;
    Py_ssize_t idx;
    if (!PyArg_ParseTuple(args, "On", &caps, &idx)) return NULL;
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(caps, "IntArray");
    if (!arr) {
        PyErr_SetString(PyExc_ValueError, "Invalid IntArray capsule");
        return NULL;
    }
    if (idx < 0 || (size_t)idx >= arr->size) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }
    return PyLong_FromLong(arr->data[idx]);
}

static PyObject* intarray_free(PyObject *self, PyObject *args) {
    PyObject *caps;
    if (!PyArg_ParseTuple(args, "O", &caps)) return NULL;
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(caps, "IntArray");
    if (!arr) {
        PyErr_SetString(PyExc_ValueError, "Invalid IntArray capsule");
        return NULL;
    }
    free(arr->data);
    free(arr);
    PyCapsule_SetName(caps, "IntArray.freed");
    PyCapsule_SetPointer(caps, NULL);
    Py_RETURN_NONE;
}

static PyMethodDef IntArrayMethods[] = {
    {"init", intarray_init, METH_VARARGS, "Create a new integer array and return a capsule."},
    {"set", intarray_set, METH_VARARGS, "Set array[index] = value."},
    {"get", intarray_get, METH_VARARGS, "Get array[index]."},
    {"free", intarray_free, METH_VARARGS, "Free the array."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef intarraymodule = {
    PyModuleDef_HEAD_INIT,
    "intarray",
    "Integer array manager using a C extension (capsules)",
    -1,
    IntArrayMethods
};

PyMODINIT_FUNC PyInit_intarray(void) {
    return PyModule_Create(&intarraymodule);
}
