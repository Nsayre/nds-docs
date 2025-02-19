***
Git
***

Introduction
============

| Git is a distributed version control system (VCS).

| The purpose of a VCS is to document and preserve changes in files (most notably code) to facilitate development.

Code is typically only documented in its current state, without a description of why it changed from its previous version.
The documentation aspect of VCS provides a medium to capture who made a change, what they changed, and for what purpose.
Preservation of changes prevents data loss, and allows easily confirming software behavior between versions. This is immensely helpful in debugging.

A VCS extends the concept of saving a project beyond a singular view of its current state to capturing its history over time.
The history of a git repository takes the shape of a tree, formed of instances of code changes called "commits".

The structure of the history of a git repository forms a tree, which began at the first commit

Version control systems are essential for modern collaborative software development.


Git Hosting Services
^^^^^^^^^^^^^^^^^^^^
Github and Gitlab are examples of services that host git repositories and provide additional features. Despite not being affiliated with the original Git project, they provide cloud hosting of repositories and useful features.

Git hosting services provide notable features such as pull requests, issue tracking, and project management that facilitate project collaboration.

Most software development with git occurs via a hosting service.

Terminology
^^^^^^^^^^^
| **Remote Repo**: A git repo hosted elsewhere (Could be Github, could be elsewhere on your machine).
| **Commit**: A unit of code-change that advances Git history. Commits should be a cohesive change to code, and should include messages that describe the scope of the change and potentially its purpose.
| **Staging**: Selecting changes to be committed.

Essential Commands
==================
| git clone : Clone (copy) an existing repository.
| git pull : Fetch branch from a remote repository and merge it to local repository.
| git push : Push commits to a remote repository
| git status : Show the changes to files in a Git repository.

Simple Workflows
================

Creating a New Repository
^^^^^^^^^^^^^^^^^^^^^^^^^
The following is the canonical way to capture the current state of a directory as a new git repo:

.. code-block:: text

   $ cd /path/to/my/codebase
   $ git init
   $ git add .
   $ git commit

Cloning an Existing Repository from a Hosting Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cloning is the act of making a local copy of a repository that exists on another computer (remote) onto your computer.

TODO

Creating 

Pushing to a Remote
^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   # Check status of current repository
   $ git status
   # Stage changes
   $ git add [filename]
   # Commit changes
   $ git commit -m "<COMMIT_MESSAGE>"
   # Push changes
   $ git push origin main
   # confirm status
   $ git status

Pulling from a Remote
^^^^^^^^^^^^^^^^^^^^^

Creating a New Repository and Uploading it to Github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO is uploading the correct word?

Initializing a git repository

git init -b main
add all files in current directory
git add .
commit files
git commit -m "First commit"

Adding a local repository to github with Github CLI (follow prompts)
gh repo create

Best Practices and Etiquette
============================

Commit Messages
^^^^^^^^^^^^^^^

Clear and concise commit messages make approving pull requests easier and facilitate collaborative development. Here are some general guidelines to keep messages clear and concise.

The first line should be a short summary, like a headline, that describes the purpose of the commit. Ideally it is 50 characters or fewer.

If the first line does not adequately describe the changes, then it should be followed by a blank line and a longer detailed description. The detailed description can add detail to the purpose, as well as elaborate on how it was achieved. It can also include any information that would be helpful to reviewers or contributors that will be viewing the message.

All parts of the message should be written in the imperative mood. Example: "Fix typo in README". The main verbs in the imperative mood are in the present tense, unlike non-imperative mood messages like "Fixed typo in README". Imperative mood messages read as if they are commands to achieve what has been done.

Commit messages should include references to relevant issues or tasks. Example: "Fix login validation bug (#123)

Branching
^^^^^^^^^

Squashing Commits? something like that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ignoring Files with .gitignore
==============================

Files can be ignored in git by adding lines to a file named .gitignore.
Patterns can be specified in this file to ignore files.

Examples:
ignore all .csv files : \*.csv
ignore an entire directory : temp/
ignore a specific file : pattern.gds
make exceptions to previous patterns : !temp/donotdelete.txt

in order to stop git from tracking a folder that was tracked and then added to .gitignore.
git rm -r --cached my_folder


Additional Common Commands
==========================

Resolving Merge Conflicts
=========================
