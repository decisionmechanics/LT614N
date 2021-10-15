#include "library.h"

#include <math.h>
#include <Python.h>

int is_prime(int n)
{
    for (int i = 2; i < sqrt(n) + 1; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }

    return 1;
}

long find_nth_prime(int n)
{
    int count = n;

    long candidate = 1;

    while (count > 0)
    {
        candidate++;

        if (is_prime(candidate))
        {
            count--;
        }
    }

    return candidate;
}

static PyObject *method_find_nth_prime(PyObject *self, PyObject *args)
{
    int n = 0;

    if (!PyArg_ParseTuple(args, "i", &n))
    {
        return NULL;
    }

    long prime = find_nth_prime(n);

    return PyLong_FromLong(prime);
}

static PyMethodDef FindPrimeMethods[] = {
    {"find_nth_prime", method_find_nth_prime, METH_VARARGS, "Python interface for the find_nth_prime C library function"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef find_prime_module = {
    PyModuleDef_HEAD_INIT,
    "findprime",
    "Python interface for the find_nth_prime C library function",
    -1,
    FindPrimeMethods};

PyMODINIT_FUNC PyInit_findprime(void)
{
    return PyModule_Create(&find_prime_module);
}