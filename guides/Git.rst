***
Git
***

Introduction
============

| Git is a distributed version control system (VCS).

| The purpose of a VCS is to document and preserve changes in files
(most notably code) to facilitate development software.

The documentation aspect of VCS provides a medium to capture who made a change,
what they changed, and for what purpose. Preservation of changes prevents data
loss, and allows easily confirming software behavior between versions.

A VCS extends the concept of saving a project beyond a singular view of its
current state to capturing its history over time.
The history of a git repository takes the shape of a tree, formed of instances
of code changes called "commits".

The structure of the history of a git repository forms a tree, which traces a
line from the creation of the repository to the end of each branch, which is
called a "head".

Version control systems are essential for modern collaborative software
development.

Git Hosting Services
^^^^^^^^^^^^^^^^^^^^
Github and Gitlab are examples of services that host git repositories and
provide additional features. Despite not being affiliated with the original
git project, they provide cloud hosting of repositories and useful features.

Git hosting services provide notable features such as pull requests, issue
tracking, and project management that facilitate project collaboration.

Most software development with git occurs via a hosting service.

Terminology
^^^^^^^^^^^
**Remote Repo**: A git repo hosted elsewhere (Could be Github,
could be elsewhere on your machine).

**Origin**: The default name for a repo that you cloned from.

**Commit**: A unit of code-change that advances Git history.
Commits should be a cohesive change to code, and should include messages that
describe the scope of the change and potentially its purpose.

**Staging**: Selecting changes to be committed.

Setup
^^^^^
Git has configuration at the system, user, and repository level.
Initially it is necessary to configure your username and email because this
information will be tied to your commit history.

.. code-block:: text

   # Set git username and email globally
   $ git config --global user.name "<FULL_NAME>"
   $ git config --global user.email <EMAIL_ADDRESS>
   # Optionally you may want to specify the default text editor for commit
   # messages or the default branch name
   $ git config --global core.editor nvim
   $ git config --global init.defaultBranch main

Essential Commands
==================

Repository Creation and Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| **git init**: Initialize a new local git repo.
| **git clone**: Clone an existing repo.
| **git remote**: Manage set of tracked repos.

Repository Status
^^^^^^^^^^^^^^^^^
| **git status**: Show the changes to files in a Git repo.
| **git log**: Show a history of commits.

Commit History Operations
^^^^^^^^^^^^^^^^^^^^^^^^^
| **git add**: Track/stage changes.
| **git rm**: Untrack files and delete them.
| **git reset**: Undo commits or unstage changes.
| **git restore**: Restore working tree files.
| **git fetch**: Download objects and refs from another repo.
| **git merge**: Merge Branches.
| **git pull**: Fetch branch from a remote repository and merge it to local repo.
| **git push**: Push commits to a remote repository.
| **git rebase**: Reapply commits from one branch on top of another branch.
| **git diff**: Show changes between commits, commit and working tree, etc.

Branching
^^^^^^^^^
| **git branch**: List, create, or delete branches.
| **git checkout**: Switch branches or restore working tree files
| **git switch**: Switch between Git branches.

Creating a New Repository
=========================
The following is the canonical way to capture the current state of a directory
as a new git repo:

.. code-block:: text

   $ cd /path/to/my/codebase
   $ git init
   $ git add .
   $ git commit

Cloning an Existing Repository from a Hosting Service
=====================================================
Cloning can be performed via HTTPS or SSH protocols. Cloning will create a
folder with the title of the repo in the directory it is performed in.

.. code-block:: text

   $ cd /path/to/desired/repo/location
   # HTTPS form:
   $ git clone https://github.com/<USERNAME>/<REPO_NAME>.git
   # SSH form:
   $ git clone git@github.com:<USERNAME>/<REPO_NAME>.git

Authentication may be required depending upon the repository. For HTTPS this
takes the form of a username and password, for SSH it means a SSH key.

Pushing to a Remote
===================

.. code-block:: text

   # Check status of current repository
   $ git status
   # Stage changes
   $ git add <FILENAME> <FILENAME> <FOLDER_NAME>/<FILENAME> ...
   # Return a file to its unmodified state with checkout or restore
   $ git checkout -- <FILENAME>
   $ git restore <FILENAME>
   # Untrack a file but preserve it locally
   git rm --cached <FILENAME>
   # Untrack a file and delete it locally
   git rm <FILENAME>
   # Unstage a file with reset or restore
   $ git reset HEAD <FILENAME>
   $ git restore --staged <FILENAME>
   # Commit changes
   $ git commit -m "<COMMIT_MESSAGE>"
   # If you realize that you made a mistake in your commit you can revise it
   git add <FILENAME_5>
   git commit --amend -m "<REVISED_COMMIT_MESSAGE>"
   # Push changes
   $ git push origin main
   # confirm status
   $ git status

Branching
=========

It is considered best practice to keep the main branch of a repo in a clean and
working state. This makes sense since it represents the most stable and
complete version of the codebase. When that main branch is running in
production there is clearly no room for unexpected changes.

To add changes (features or fixes), a new branch is made off of
main, and that branch is later merged when the change is complete and the code
has been reviewed.

Branches are quickly and easily created and destroyed. Developers should feel
free to create branches and experiment freely within them.

.. code-block:: text

   # Create new branch
   $ git branch <BRANCH_NAME>
   # Switch to a branch
   $ git checkout <BRANCH_NAME>
   # Create a new branch and switch to it
   $ git switch -c <BRANCH_NAME>

TODO git switch vs. checkout
TODO other duplicitous git commands

Pulling in Changes
==================

.. code-block:: text

   # Check status of current repository
   $ git status
   # Download changes from the remote and merge them
   $ git pull

Git pull is actually a git fetch followed by a git merge.

The fetch operation gathers the latest changes from the remote, and the merge
operation integrates them into the local repo.

Merging can result in merge commits when the condition of two branches

Merging an outdated version of a branch, with its updated version, occurs as a
"fast-forward" merge.
Fast-forwarded merges do not add a merge commit

New commit history is appended to the outdated version and it advances through
time. If you clone a repo and make no changes to it, and then other developers
advance the main branch of that repo numerous times, a git pull operation will
simply update your local repo to


In the case where there have been no deviating changes to the local branch, a
git pull simply updates the local branch to same condition as the remotes.

However



Merging

When there are no deviating changes in the current branch, a git pull will simply update your current branch to latest version from the remote.

However if your local branch has deviated from the remote, then a pull 

If your local repo has never deviated from the commit history of the remote, then a "fast forward" merge will be performed, and the local will be updated to the remote without any changes to the commit history.

However, if the local repo has deviated, then merging will include a merge commit that changes history and tracks where the two branches have combined.




Behind the scenes, git pull performs a fetch operation followed by a merge operation.
While merge is the default, a rebase can instead be performed via the --rebase option. Merge operations do not alter previous commit history, they simply add a merge commit and combine branches. Rebasing allows altering the commit history, and moving one branch on top of another. 
You can imagine merging as the two branches of a tree growing into each other to form a single branch. Rebasing can be imagined as cutting off a branch and attaching it to the tip of another.

| Merging is always safe because it doesn't interfere with commit history. However, the additional commit that it adds can be unnecessary clutter.
| Rebasing is useful in specific circumstances.

.. code-block:: text

   # Fetch gathers the latest changes from the remote and is the first part of a git pull command.
   $ git fetch
   # Rebasing can be performed instead of the default merging behavior
   $ git pull --rebase

Merging & Rebasing
^^^^^^^^^^^^^^^^^^^^

When a branch has served its purpose and it is time to integrate its changes, it can either be merged or rebased.
The difference between merging and rebasing is in the structure of the commit history.

Once the time has come for branche
When the time has come for 
Merging 
Once changes have been fetched they can be merged into 
TODO

rebase
merge
pull


Resolving Merge Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^
TODO

Uploading an Existing Repo to Github
====================================

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

Github's gitignore templates are a very useful starting point.
https://github.com/github/gitignore

Licensing
=========

TODO
review of licensing options, importantance, etc.
