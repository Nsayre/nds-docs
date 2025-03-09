======
Python
======

Purpose
=======

Python has excellent documentation. Notably the
`The Python Tutorial <https://docs.python.org/3/tutorial/index.html>`__ and
`The Python Standard Library <https://docs.python.org/3/library/index.html>`__
are excellent resources. Additionally there are countless blogs and guides.
Being well aware of this, I still chose to create my own notes, because
I believed I could make something unique that could fill a niche.
My notes attempt to cover a large variety of topics and weave them together
into a more cohesive and overall guide.

I hope that others find my notes to be educational and useful.

Pythonic Python
===============

"Pythonic" Python is written in a way that the developers and the community
consider to be idiomatic.

Writing idiomatic code is important for two reasons:

* **Clarity**: By following conventions, you make your Python code
  easier to read, debug, and modify. This facilitates collaboration and
  improves productivity.
* **Performance**: Effort has been put into optimizing idiomatic Python, so
  writing Python in an idiomatic way is simply faster in many cases.

`The Zen of Python <https://legacy.python.org/dev/peps/pep-0020/>`__ attempts
to define first principles in the philosophy of Python.

What can we do to make our code more Pythonic?

We can follow guidelines where present, and otherwise regularly reconsider
our approach as we learn from and analyze the code of others.

PEP 8 & PEP 257
^^^^^^^^^^^^^^^

`PEP 8 <https://peps.python.org/pep-0008/>`__ defines coding conventions for
Python code in its standard library. Although it doesn't tell the community
how to write Python outside of its library. In practice it is broadly applied
and widely accepted.

Although it is a long list of conventions, it is notably extremely explicit
that it does not represent rules for the sake of rules. Rather, it defines
general guidelines that broadly can be considered good practice, and leaves
the exact implementation to the developer.

`PEP 257 <https://peps.python.org/pep-0257/>`__ is the other PEP that is good
to keep close at hand, it defines conventions for Python docstrings.

Linting & Formatting
^^^^^^^^^^^^^^^^^^^^

Linting is another term for static code checking, where a program parses
through your code without actually running it, to find problems, or mistakes
that could turn into problems.
A code formatter automatically formats your code for you. This can be useful
to comply with guidelines, maintain consistency, or just save time.

Although PEP8 is relatively brief, that doesn't mean that memorizing all of its
aspects is easy or worthwhile. Being caught up with minor formatting can
negatively impact productivity, and we can recognize times when all of our
efforts should be focused on getting something to work, rather than chasing
some elusive concept of what is "optimal".

There are a variety of tools that can check for PEP8 compliance, and even
automatically enforce it.

TODO try using ruff for formatting and linting, and then make general
recommendation on it.

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
   could implement the desired functionality whenever writing a new function.
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
   list_simple[0] = "new value"
   # Nested lists
   list_nested = [[1, 2, 3], [4, 5, 6]]

TODO slicing & comprehensions
>>> list_comp = [x for x in range(3)]
<EXAMPLE_OUTPUT>
>>> list_comp = [x for x in range(3)]
<EXAMPLE_OUTPUT>

Lists are flexible due to their lack of restrictions. You could say that a list
should be used whenever there are no compelling reasons to use other types.

Tuples
^^^^^^
* Immutable
* Ordered

.. code-block:: python

   tup_len0 = ()
   tup_len1 = 1,
   tup = tuple(1, 2, 3)
   tup = (1, 2, 3)
   tup = 1, 2, 3
   # Tuples may be nested
   tup_nested = 1, 2, (3, 4), [5, 6]

Tuples not only protect data that should not change after assignment, but
operations involving tuples execute faster due to their simpler nature.
Because of this, it is advantageous to use tuples when appropriate.

TODO slicing & comprehensions
>>> list_comp = [x for x in range(3)] <EXAMPLE_OUTPUT>
>>> list_comp = [x for x in range(3)]
<EXAMPLE_OUTPUT>

Dictionaries
^^^^^^^^^^^^
* Key-value pairs with fast lookup
* Mutable
* Ordered*

.. code-block:: python

   dict_len0 = {}
   dict_simple = {"A": 1, "B": 2.3}
   dict_simple = dict([("A", 1), ("B", 2.3)])


TODO slicing & comprehensions
>>> list_comp = [x for x in range(3)]
<EXAMPLE_OUTPUT>
>>> list_comp = [x for x in range(3)]
<EXAMPLE_OUTPUT>

Similar to indexing out of range, attempting to access a key that is not
present in a dict results in a KeyError.

>>> dict_simple["A"]
1
>>> dict_simple["C"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'C'

Use the get method to avoid this.

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

.. code-block:: python

   set_simple = {1, 2, 3}

>>> set([1, 1, 1, 2, 3])
{1, 2, 3}

Functions & Arguments
^^^^^^^^^^^^^^^^^^^^^
TODO function definition example, showing docstring, args, kwargs, and examples
of usage of * and / and their meaning

TODO example calling it with different arguments

Classes, Methods & Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO make my own compelling example of a class

Classes allow defining custom objects that have attributes and methods
.. code-block:: python

   class BankAccount:
       def __init__(self):
           self.balance = 0

       def withdraw(self, amount):
           self.balance -= amount
           return self.balance

       def deposit(self, amount):
           self.balance += amount
           return self.balance

Classes - Inheritance
^^^^^^^^^^^^^^^^^^^^^

Control Flow
============

Importing
^^^^^^^^^


Conditionals
^^^^^^^^^^^^

TODO if, for, else, elif

Looping & Breaking
^^^^^^^^^^^^^^^^^^

TODO for, while, break, return etc.


Testing, test driven dev, errors, exceptions, logging
=====================================================

Debugging
===============================

Benchmarking/performance/profiling
==================================

Packages & Virtual Environments
===============================

Setting up venv
^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activating
| source venv/bin/activate

Deactivating
| deactivate

Unittest
===============
Running only a single test
python -m unittest <module_name>.py

OS/Path/File ops
===============================
