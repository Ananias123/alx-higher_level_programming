#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - A function that prints info about python
 * @p: The pointer 
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < size; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
