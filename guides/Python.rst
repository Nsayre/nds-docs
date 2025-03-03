======
Python
======

Purpose
=======

Python has excellent documentation, and there are already countless blogs and
guides on Python. However, I still see an opportunity for guides to be more
condensed and practical.

I hope these guides are useful and educational.

Pythonic Python
===============

"Pythonic" Python is written in a way that the developers and the community
consider to be idiomatic.

Writing idiomatic code is important for two reasons:

* **Clarity**: By following conventions, you make your Python code
  easier to read, debug, and modify. This Fosters collaboration and improves
  productivity.
* **Performance**: Effort has been put into optimizing idiomatic Python, so
  writing Python in an idiomatic way is simply faster in many cases.

The Zen of Python attempts to define first principles in the philosophy of
Python.
https://legacy.python.org/dev/peps/pep-0020/

What can we do to write more Pythonic code?

We can follow guidelines where present, and otherwise regularly reconsider
our approach.

PEP8
^^^^

PEP8 represents the current guidelines to writing 

TODO PEP8, linting, formatting, and what it doesn't cover

Choosing, Creating, and Manipulating Objects
============================================

It is necessary to consider the type of objects in order to write clear and
performant Python. There are many ways to achieve the same result in
programming, however not all of those ways are equally intuitive or performant.

The benefit of performance is obvious, however the benefit of intuitiveness is
sometimes understated. The intuitiveness of code is valuable whenever code must
be read and understood by others.

Therefore it is important to know the built-in types and understand when and
how they should be used, as well as how to create your own classes when the
need arises.

.. note::

   Built-in functions and methods are implemented in C, making them much faster
   than an equivalent solution in Python. Therefore they should be used when
   possible. One good way to build awareness of built-in functions and methods
   is to consider whether there is a built-in function or method that
   could implement the desired functionality whenever we write as new function.
   Searching through auto-complete options for functions or methods and reading
   their documentation in an IDE is an excellent way to build familiarity
   through practice. Memorizing them before needing to use them is likely
   unnecessary preoptimization.

Lists
^^^^^
* Mutable
* Ordered

.. code-block:: python

   list_len0 = []
   list_simple = [1, 2, 3]
   # Lists are mutable, therefore they can be changed after assignment
   # Here we reassign the value in the 0th index of our list to a new value
   list_simple[0] = "new value"
   # Lists may contain mixed data types
   list_mixed = [True, 1.2, 8, "Hi"]
   # Lists may be nested
   # Nested lists
   list_nested = [[1, 2, 3], [4, 5, 6]]
   # List comprehensions
   list_comp = [x for x in range(3)]
   TODO
   list_comp_nested = [x for x in range(3)]
   # List slicing

Lists are flexible due to their lack of restrictions. You could say that a list
should be used whenever there are no compelling reasons to use other types.

Tuples
^^^^^^
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
content do not change after assignment. Tuples not only protect data that
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
* Collection of unique items that excels at exctracting unique values and
  testing membership
* Concepts such as order, index, and slicing have no meaning with regards to a
  set.
* Mutable
* Unordered

>>> set([1, 1, 1])
{1}

.. code-block:: python

   set_simple = {1, 2, 3}

Slicing
^^^^^^^

Comprehensions & Generators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Packages & Virtual Environments

OS/Path/File ops

Debugging

Clean Code with PEP8

Testing, errors, exceptions, logging

Test driven development and when not to

Benchmarking/performance/profiling


Control Flow
============

TODO, is control flow the right name?


Keyword arguments
positional and keyword arguments (args, kwargs)

Indexing Iterables
^^^^^^^^^^^^^^^^^^
lists may be indexed until their length - 1.
Negative indexes start at the end of the list and work forwards.
An iterable may be "sliced" in order to refer to specific indexes.

Debugging
=========

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
