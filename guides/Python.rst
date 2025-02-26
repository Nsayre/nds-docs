======
Python
======

Introduction
============

TODO description of what Python is, and where it stands next to other langs

Types
=====

TODO revisit, maybe delete

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
>>> type("word")
<class 'str'>

**Bool**: True or False
**int**: Integer


Data Structures
===============

Lists
^^^^^
* Data structure for data that is expected to change
* Mutable
* Ordered

.. code-block:: python

   list_len0 = []
   list_simple = [1,2,3]
   # Lists are mutable, therefore they can be changed after assignment
   # Here we reassign the value in the 0th index of our list to a new value
   list_simple[0] = "new value"
   # Lists may contain mixed data types
   list_mixed = [True, 1.2, 8, "Hi"]
   # Lists may be nested
   list_twodim = [[1, 2, 3], [4, 5, 6]]

All iterables in python are zero-indexed. Values in lists can be read or
reassigned from their index.

>>> list_simple[0]
1
>>> list_simple[0] = "something else"
>>> list_simple[0]
'something else'

As with other iterables, care must be taken not to attempt to index outside of
an iterables range. Attempting this results in an IndexError.

>>> list_simple[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

The usefulness of lists come from their versatility.
They should be used whenever you have a group of data that needs to change
after assignment, where there is no unique identifier for the values.

Tuples
^^^^^^
* Data structure for data that should not change after assignment
* Immutable
* Ordered

.. code-block:: python

   tup_len0 = ()
   tup_len1 = 1,
   tup = (1, 2, 3)
   tup = 1, 2, 3
   tup = tuple(1, 2, 3)
   # Tuples may contain mixed data types
   tup_mixed = ("string", False, 1.41)
   # Tuples may be nested
   tup_nested = 1, 2, (3, 4), [5, 6]

Tuples may be read from indexes just like lists, however attempting to
reassign a value to a tuple by index will result in a TypeError.

>>> tup[0]
1
>>> tup[0] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

Tuples excel at representing fixed data structures where length, order, and
content does not change after assignment. Tuples not only protect data that
should not change, but operations involving tuples execute faster due to their
simpler nature. Because of this, it is advantageous to use tuples when
appropriate.

Dictionaries
^^^^^^^^^^^^
* Key-value pairs with fast lookup
* Mutable
* Ordered*

.. code-block:: python

   dict_len0 = {}
   dict_simple = {"A": 1, "B": 2.3}
   dict_simple = dict([("A", 1), ("B", 2.3)])

>>> dict_simple["A"]
1
>>> dict_simple["C"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'C'

Similar to indexing out of range, attempting to access a key that is not
present in a dict results in a KeyError.

A convenient way to avoid this is to use the get method.

It will return the value if present, and None (default) if not.

>>> dict_simple.get("C")
>>> dict_simple.get("B")
2.3

Dictionaries (dicts) should be used for their fast lookup when storing values
with unique names.

\*Dicts have dependable insertion order in Python 3.6+. beyond that the
OrderedDict class is a more appropriate choice.

Sets
^^^^
* Collection of unique items that excels at testing membership
* Mutable
* Unordered

>>> set([1, 1, 1])
{1}

.. code-block:: python

   set_simple = {1, 2, 3}

Concepts such as order, index, and slicing have no meaning with regards to a
set.

Like the mathematical concept on which they are based, sets are groups of
unique values. They are useful for extracting unique values from other data
types and testing membership. Various mathematical set operations are
available.

Iterators, Generators
=====================

TODO

Comprehensions
==============

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
