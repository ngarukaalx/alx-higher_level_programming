#include <Python.h>

/**
 * print_python_list_info - fuction name
 * @p: parameter
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
