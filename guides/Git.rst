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

| **Repository Creation and Configuration**:
| **git init**: Initialize a new local git repo.
| **git clone**: Clone an existing repo.
| **git remote**: Manage set of tracked repos.

| **Repository Status**:
| **git status**: Show the changes to files in a Git repo.
| **git log**: Show a history of commits.

| **Commit History Operations**:
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

| **Branching**:
| **git branch**: List, create, or delete branches.
| **git checkout**: Switch branches or restore working tree files
| **git switch**: Switch between Git branches.

| **Repository Tidying**:
| **git stash**: Stash local changes in a temporary area.
| **git clean**: Revove files not tracked by git.

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
complete version of the codebase. If your main branch houses production code,
then clearly there is no room for unexpected changes.

To add changes (features or fixes), a new branch is made off of
main, and that branch is later merged when the change is complete and the code
has been reviewed.

Branches are quickly and easily created and destroyed. Developers should feel
free to create branches and experiment freely within them.

Branches can be "moved" which results in renaming them. However, in a
collaborative environment this shouldn't be done without the permission of all
developers using that branch, since it could cause confusion or disruption.

.. code-block:: text

   # List current branches
   $ git branch
   * main
     old_feature_branch
   # The asterisk indicates the branch that is currently active
   # a -vv flag will show the latest commit hash
   # and whether branches are ahead or behind
   $ git branch -vv
   # Fetch and show all branches verbosely
   $ git fetch --all; git branch -vv

.. code-block:: text

   # Create new branch
   $ git branch <BRANCH_NAME>
   # Switch to a branch
   $ git switch <BRANCH_NAME>
   # Create a new branch and switch to it
   $ git switch -c <BRANCH_NAME>

Once a branch has served its purpose it may be merged into another branch. It
is good practice to delete a branch after merging since it no longer is
necessary due to its changes being integrated with another branch.

.. code-block:: text

   # Merge branch into main
   $ git switch main
   $ git merge <BRANCH_NAME>
   # Delete local branch
   $ git branch -d <BRANCH_NAME>

If the branch was never pushed to a remote, then the previous commands will be
sufficient to delete it. However, it is actually a push command that allows
deletion of a remote branch.

.. code-block:: text

   # Delete remote branch
   $ git push -d <REMOTE> <BRANCH_NAME>

Even if you delete a remote branch, and other collaborators fetch your changes,
the obsolete branch will still exist in their repo until they execute a fetch
command with the --prune flag.

.. code-block:: text

   # Delete all obsolete remote-tracking branches
   $ git fetch <REMOTE> --prune

Pulling in Changes
==================

When your local repository no longer has the latest commit history, you can
use the git pull command to pull in the latest changes. It is a good idea to
stay on top of pulling in the latest changes to make sure you aren't working
with out of date files.

.. code-block:: text

   # Check status of current repository
   $ git status
   # Download changes from the remote and merge them
   $ git pull

The git pull command actually runs a git fetch followed by a git merge.

The fetch operation gathers the latest changes from the remote, and the merge
operation integrates them into the local repo.

Merging
^^^^^^^

The result of a merge can look different depending on whether the changes are
divergent and/or conflicting.

If there is no divergent commit history, a "fast-forward merge" will occur, and
commit history will be advanced without the creation of a merge commit.

If there is divergent non conflicting commit history, a three way merge will
occur, where a merge commit will be created that will act as the point the two
branches merge.

If there is divergent conflicting commit history, then a new merge commit will
be created and the user will be required to resolve the conflict by specifying
the exact status of the conflicting portion of files that will go into the new
merge commit.

.. code-block:: text

   # Merge specified branch into active branch
   $ git merge <BRANCH_NAME>

Rebasing
^^^^^^^^

Rebasing allows moving one branch on top of another one. It is a way to alter
commit history for clarity or convenience. However, unlike merging where commit
history is never destroyed, rebasing opens the door to losing valuable history.

.. code-block:: text

   $ git switch <BRANCH_TO_REBASE>
   # Rebase current active branch onto specified branch
   $ git rebase <BRANCH_TO_REBASE_ONTO>
   First, rewinding head to replay your work on top of it...
   Applying: added staged command

Merging vs. Rebasing
^^^^^^^^^^^^^^^^^^^^

Merging is always safe because it doesn't alter previous commit history.
However, the additional commit that it adds can be seen as unnecessary clutter.

Rebasing can make very clean commits, because it can make work that occurred in
parallel appear to have happened linearly.

However, rebasing should never be performed on commits that have left your
local repo, because they will alter the history that everyone that works with
that repo sees, and potentially force them to do additional work to reconcile
with the new history you have created.

Which you use depends on best practices and the philosophy of the project.
The best practices dictate the previous rule that rebasing should only be
performed on commits that you and only you have touched. If you believe that
commit history should reflect absolute history as it occurred, then rebasing
may not be preferred. However if you believe that minor discrepencies are worth
the added clarity then you may rebase often.

Resolving Merge Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^
TODO


Stashing Work
^^^^^^^^^^^^^

If you want to switch branches while in the middle of work, you may stash the
state of your current branch so that you can revisit it later.

.. code-block:: text

   # Stash current working directory
   $ git stash
   # View list of stashes
   $ git stash list
   # Revert to stashed state
   $ git stash apply

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

Commit Messages
^^^^^^^^^^^^^^^

Commits should focus on a single issue, and their messages should be clear
and concise. The first line should be a summary, that describes the purpose in
50 characters or less.

If the first line isn't sufficient to describe the change, then it can be
followed with a blank line and a more detailed description. The details could
describe what was changed, and how it was achieved. Since the purpose of this
message is collaboration and posterity, it should make sense in the context
of developer reviewing the changes. It should be written in the imperative mood
, as in "Fix", not "Fixed" or "Fixes". Related issues can be referenced in the
following way: "Fix login bug (#49)"


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

README and CONTRIBUTING Files
=============================

A README file can be includedin a repository to indicate
* Project purpose
* Installation instructions
* Guide to running/configuring the project
* Software license information
* Instructions for contributing

A CONTRIBUTING file acts as a template for pull requests, giving a way to
convey preferences whenever someone opens a new pull request on your repository
.

Licensing
=========

TODO
review of licensing options, importantance, etc.
