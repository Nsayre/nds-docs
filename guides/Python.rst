===============
Python
===============

Lists
   data structure for data that should be changed
   mutable
   ordered

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
