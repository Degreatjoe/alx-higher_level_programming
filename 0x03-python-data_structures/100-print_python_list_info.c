
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: Pointer to the Python list object
 *
 * Description: This function prints the size of a Python list,
 * the amount of memory allocated for it, and the type of each element.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
