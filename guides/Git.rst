***
Git
***

Introduction
============

| Git is a distributed version control system (VCS).

| The purpose of a VCS is to document and preserve changes in files (most notably code) to facilitate development software.

The documentation aspect of VCS provides a medium to capture who made a change, what they changed, and for what purpose.
Preservation of changes prevents data loss, and allows easily confirming software behavior between versions.

A VCS extends the concept of saving a project beyond a singular view of its current state to capturing its history over time.
The history of a git repository takes the shape of a tree, formed of instances of code changes called "commits".

The structure of the history of a git repository forms a tree, which traces a line from the creation of the repository to the end of each branch, which is called a "head".

Version control systems are essential for modern collaborative software development.

Git Hosting Services
^^^^^^^^^^^^^^^^^^^^
Github and Gitlab are examples of services that host git repositories and provide additional features. Despite not being affiliated with the original git project, they provide cloud hosting of repositories and useful features.

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

Cloning can be performed via HTTPS or SSH protocols. Cloning will create a folder with the title of the repo in the directory it is performed in.

.. code-block:: text

   $ cd /path/to/desired/repo/location
   # HTTPS form:
   $ git clone https://github.com/<USERNAME>/<REPO_NAME>.git
   # SSH form:
   $ git clone git@github.com:<USERNAME>/<REPO_NAME>.git

Authentication may be required depending upon the repository. For HTTPS this takes the form of a username and password, for SSH it means a SSH key.

Pushing to a Remote
^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   # Check status of current repository
   $ git status
   # Stage changes
   $ git add <FILENAME_1> <FILENAME_2> <FOLDER_NAME>/<FILENAME_3> ...
   $ git rm <FILENAME_4> ...
   # Commit changes
   $ git commit -m "<COMMIT_MESSAGE>"
   # Push changes
   $ git push origin main
   # confirm status
   $ git status

Pulling From a Remote
^^^^^^^^^^^^^^^^^^^^^

TODO proper way to pull

Creating and Changing Branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TODO

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

Resolving Merge Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^
TODO

Best Practices and Etiquette
============================

README
^^^^^^
TODO

Commit Messages
^^^^^^^^^^^^^^^

TODO 

Clear and concise commit messages make approving pull requests easier and facilitate collaborative development. Here are some general guidelines to keep messages clear and concise.

The first line should be a short summary, like a headline, that describes the purpose of the commit. Ideally it is 50 characters or fewer.

If the first line does not adequately describe the changes, then it should be followed by a blank line and a longer detailed description. The detailed description can add detail to the purpose, as well as elaborate on how it was achieved. It can also include any information that would be helpful to reviewers or contributors that will be viewing the message.

All parts of the message should be written in the imperative mood. Example: "Fix typo in README". The main verbs in the imperative mood are in the present tense, unlike non-imperative mood messages like "Fixed typo in README". Imperative mood messages read as if they are commands to achieve what has been done.

Commit messages should include references to relevant issues or tasks. Example: "Fix login validation bug (#123)

Branching
^^^^^^^^^

TODO

Squashing Commits? something like that
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

Ignoring Files with .gitignore
==============================

Often a codebase will rely on files that are not code, yet are considerably large. 
Since these files do not need to be tracked as closely as code, it is safe to ignore them and provide alternate means to acquire them.
Once files are >1MB it is wise to start considering whether they really need to be tracked.

Ignoring files can be managed in git with the .gitignore file.
the .gitignore file is a file placed in your repository that specifies patterns of files to be ignored by git.

.. code-block:: text

   # Example .gitignore file
   # ignore all files in the data directory
   data/
   # ignore all files in the root directory that end in the .csv extension
   *.csv
   # ignore a specific file
   pattern.gds
   # Make an exception to a previous pattern to specify a file not to ignore
   !data/.config

In order to stop git from tracking a folder that was previously tracked that you would like to ignore:

.. code-block:: text

   git -rm -r --cached my_folder
