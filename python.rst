===============
Data Structures
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

===============
Setting up venv
===============

| mkdir my_project
| cd my_project
| python3 -m venv venv
| source venv/bin/activate

Save requirements.txt
pip freeze > requirements.txt

Install from requirements.txt

pip install -r requirements.txt

| deactivate venv
| deactivate
| requirements.txt...
