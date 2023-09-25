#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyListObject *list = (PyListObject *)p;

	size = Py_SIZE(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Print information about Python bytes
 * @p: PyObject pointer to Python bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", Py_SIZE(p));
	printf("  trying string: %s\n", PyUnicode_DecodeUTF8(PyBytes_AsString(p), Py_SIZE(p), NULL));
	printf("  first %ld bytes: ", Py_SIZE(p) > 10 ? 10 : Py_SIZE(p));
	for (i = 0; i < Py_SIZE(p) && i < 10; i++)
		printf("%02x%s", bytes->ob_sval[i], i < 9 ? " " : "\n");
}

/**
 * print_python_float - Print information about Python float objects
 * @p: PyObject pointer to Python float
 */
void print_python_float(PyObject *p)
{
	PyObject *str_repr;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str_repr = PyObject_Repr(p);
	printf("  value: %s\n", PyUnicode_AsUTF8(str_repr));
	Py_XDECREF(str_repr);
}
