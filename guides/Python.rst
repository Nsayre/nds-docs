======
Python
======

Introduction
============

TODO description of what Python is, and where it stands next to other langs

Types
=====

Essentially everything in Python is an object, and every object has a type.

Python's type function will return the type of an object. Here we use it to
exhibit python's built-in types.

>>> print(type(True), type(False))
<class 'bool'> <class 'bool'>
>>> type(3)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type(2+1j)
<class 'complex'>
>>> type(None)
<class 'NoneType'>

Data Structures
===============

Lists
^^^^^
* Data structure for data that is expected to change
* Mutable
* Ordered

.. code-block:: python

   simple_list = [1,2,3]
   # Lists are mutable, therefore can change after assignment
   # Here we reassign the 0th index to a new value
   simple_list[0] = "new value"
   # lists may contain mixed data types
   mixed_list = [True, 1.2, 8, "Hi"]
   # Lists may be nested
   twodim_list = [[1, 2, 3], [4, 5, 6]]

Fundamental List Methods
^^^^^^^^^^^^^^^^^^^^^^^^

Tuples
   data structure for data that should not be changed
   immutable
   ordered

Dicts
   key-value pairs that have fast lookup
   mutable
   unordered

Sets
   collection of unique items that excels at testing membership
   mutable
   unordered

Iterators, Generators
^^^^^^^^^^^^^^^^^^^^^

Comprehensions
^^^^^^^^^^^^^^

Control Flow
============

TODO, is control flow the right name?

if statements
^^^^^^^^^^^^^

for statements
^^^^^^^^^^^^^^

while statements

functions

Keyword arguments
positional and keyword arguments (args, kwargs)

Indexing Iterables
^^^^^^^^^^^^^^^^^^
lists may be indexed until their length - 1.
Negative indexes start at the end of the list and work forwards.
An iterable may be "sliced" in order to refer to specific indexes.


importing
^^^^^^^^^
TODO actually part of control flow?

Debugging
=========


Virtual Environments
====================

Setting up venv
===============

Create project folder, enter it and activate venv
   mkdir my_project
| cd my_project
| python3 -m venv venv
| source venv/bin/activate

Install relevant packages
| pip install numpy
Save requirements.txt
| pip freeze > requirements.txt

Install from requirements.txt
| pip install -r requirements.txt

Activating/Deactivating venv
===============
Activating
| source venv/bin/activate

Deactivating
| deactivate

Unittest
===============
Running only a single test
python -m unittest <module_name>.py
