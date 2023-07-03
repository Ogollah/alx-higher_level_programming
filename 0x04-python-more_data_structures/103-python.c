#include <Python.h>
#include <stdio.h>

/**
 *print_python_list - Prints basic info about a Python list.
 *@p: Python list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

/**
 *print_python_bytes - Prints basic info about a Python bytes object.
 *@p: Python list object.
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *bytes = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	if (size < 10)
	{
		printf("  first %ld bytes: ", size + 1);
	}
	else
	{
		printf("  first 10 bytes: ");
	}

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x", bytes[i] & 0xff);
		if (i == 9 && size >= 10)
		{
			printf("...");
		}
	}
	printf("\n");
}
