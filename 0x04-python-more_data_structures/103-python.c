#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;

        printf("Element %zd: %s\n", i, typeName);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", PyBytes_GET_SIZE(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; ++i) {
        printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
        if (i < 9) {
            printf(" ");
        }
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    Py_Initialize();

    // Example usage
    PyObject *list = PyList_New(3);
    PyList_SetItem(list, 0, PyLong_FromLong(1));
    PyList_SetItem(list, 1, PyLong_FromLong(2));
    PyList_SetItem(list, 2, PyLong_FromLong(3));

    PyObject *bytes = PyBytes_FromStringAndSize("Hello, World!", 13);

    print_python_list(list);
    print_python_bytes(bytes);

    Py_Finalize();
    return 0;
}

