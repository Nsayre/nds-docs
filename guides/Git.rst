***
Git
***

Purpose
============

These notes demonstrate common git operations with real commands, and provide
some general best practices.
This is my attempt to distill what is most important to know regarding git.
I hope for it to be helpful to myself and to others.

Introduction
============

Git is a distributed version control system (VCS). The purpose of a VCS is to
document and preserve changes in files (most notably code) to facilitate
software development.

The messages in git commit history provide a medium to record who made
changes, what they changed, and for what purpose. The existence of commit
history prevents data loss, and allows easily confirming software behavior
between versions.

A VCS extends the concept of saving a project beyond a singular view of its
current state to capturing its history over time.
The history of a git repository takes the shape of a tree, formed of instances
of code changes called "commits".

Version control systems are essential for modern collaborative software
development.

Git Hosting Services
^^^^^^^^^^^^^^^^^^^^
Github and Gitlab are examples of services that host git repositories and
provide additional features. Despite not being affiliated with the original
git project, they provide cloud hosting of repositories and useful features.

Git hosting services provide notable features such as pull requests, issue
tracking, and project management that facilitate project collaboration.

Most software development with git occurs with the involvement of a hosting
service.

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
| **git config**: Manage git configuration.
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
| **git pull**: Fetch branch from a remote repository and merge it to local repo.
| **git push**: Push commits to a remote repository.
| **git rebase**: Reapply commits from one branch on top of another branch.
| **git diff**: Show changes between commits, commit and working tree, etc.

| **Branching**:
| **git branch**: List, create, or delete branches.
| **git checkout**: Switch branches or restore working tree files
| **git merge**: Merge Branches.
| **git switch**: Switch between Git branches.

| **Repository Tidying**:
| **git stash**: Stash local changes in a temporary area.
| **git clean**: Revove files not tracked by git.

Creating, Cloning, and Uploading Repositories
=============================================

Creating a New Repository
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   $ cd <FILEPATH_TO_CODEBASE>
   $ git init
   $ git add .
   $ git commit

Cloning an Existing Repository from a Hosting Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cloning can be performed via HTTPS or SSH protocols. Cloning will create a
folder with the title of the repo in the directory it is performed in.

.. code-block:: text

   $ cd <FILEPATH_TO_CODEBASE>
   # HTTPS form:
   $ git clone https://github.com/<USERNAME>/<REPO_NAME>.git
   # SSH form:
   $ git clone git@github.com:<USERNAME>/<REPO_NAME>.git

Authentication may be required depending upon the repository. For HTTPS this
takes the form of a username and password, for SSH it means a SSH key.

Uploading an Existing Repo to Github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   $ cd <FILEPATH_TO_CODEBASE>
   $ git remote add origin <GITHUB_REPO_URL>
   # verify that you set remote URL correctly
   $ git remote -v
   # push local changes to github repo
   $ git push origin main

.. code-block:: text

   # Alternatively this can be done with github cli:
   $ cd <FILEPATH_TO_CODEBASE>
   gh repo create <REPO_NAME> --source=. --remote=origin --public

Pushing to a Remote
===================

.. code-block:: text

   # Committing and pushing all changes in its simplest form:
   $ git commit -am "<COMMIT_MESSAGE>"
   $ git push origin main

.. code-block:: text

   # Detailed form of committing and pushing:
   # Check status
   $ git status
   # Stage changes
   $ git add <FILENAME> <FILENAME> <FOLDER_NAME>/<FILENAME> ...
   # Commit changes
   $ git commit -m "<COMMIT_MESSAGE>"
   # If you realize that you made a mistake in your commit you can revise it
   git add <FILENAME_5>
   git commit --amend -m "<REVISED_COMMIT_MESSAGE>"
   # Push changes
   $ git push origin main
   # confirm status
   $ git status

Untracking Changes
^^^^^^^^^^^^^^^^^^

.. code-block:: text

   # Untrack a file but preserve it locally
   git rm --cached <FILENAME>
   # Untrack a file and delete it locally
   git rm <FILENAME>

Returning to Previous States
============================

.. code-block:: text

   # Return a file to its unmodified state with checkout or restore
   $ git checkout <FILEPATH>
   $ git restore <FILEPATH>
   # Replace a file with its version in another branch
   $ git checkout <BRANCH_NAME> -- <FILEPATH>

   # Unstage specific files
   $ git reset <FILENAME>
   $ git restore --staged <FILENAME>
   # Unstage everything
   $ git reset

   # Reset the working directory to its previous status...
   # Keeping unstaged changes (default):
   $ git reset --mixed <COMMIT>
   # Keeping staged changes:
   $ git reset --soft <COMMIT>
   # Not keeping any changes (dangerous, will delete untracked files):
   $ git reset --hard <COMMIT>

   # Create a new commit that reverses the changes of a previous commit
   $ git revert <COMMIT>

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

If the purpose of a branch is only to house changes for a feature or fix then
likely it will be deleted after merging in order to keep the repo clean.
However, another strategy is to have a long lived development branch that is
never deleted, and instead periodically merged into the main branch.

.. code-block:: text

   # Merge branch and then delete it:
   $ git switch main
   $ git merge <BRANCH_NAME>
   # Delete local branch
   $ git branch -d <BRANCH_NAME>

If the branch was never pushed to a remote, then the previous commands will be
sufficient to delete it.

.. code-block:: text

   # Delete remote branch
   $ git push -d <REMOTE> <BRANCH_NAME>

If other collaborators have pulled in your remote branch, then even if you
delete it, that obsolete branch will still exist in their repo until they
execute a fetch command with the --prune flag.

.. code-block:: text

   # Delete all obsolete remote-tracking branches
   $ git fetch <REMOTE> --prune

Pulling in Changes from the Remote
==================================

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
=======

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

   # Merge specified branch into active branch:
   $ git merge <BRANCH_NAME>

Merging can always be aborted if one wasn't expecting conflicts or realized
they had made a mistake.

.. code-block:: text

   # Abort merge:
   $ git merge --abort

Rebasing
========

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
====================

Merging is always safe because it doesn't alter previous commit history.
However, the additional commit that it adds can be seen as unnecessary clutter.

Rebasing can make very clean commits, because it can make work that occurred in
parallel appear to have happened linearly.

However, rebasing should never be performed on commits that have left your
local repo, because they will alter the history that everyone that works with
that repo sees, and potentially force them to do additional work to reconcile
with the new history you have created.

Which you use depends on best practices and the philosophy of the project.
If you believe that commit history should reflect absolute history as it
occurred, then rebasing may not be preferred. However if you believe that
minor discrepencies are worth the added clarity then you may rebase often.

Resolving Merge Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^
If two branches have conflicting changes, they cannot be merged without
specifying which branches changes to include in the merge commit. Conflicts can
be manually resolved by editing conflicting files line-by-line.


.. code-block:: text

   # Manually resolving conflicts:
   $ git switch main
   $ git merge <BRANCH_TO_MERGE>
   CONFLICT (content): Merge conflict in <FILENAME>
   Automatic merge failed; fix conflicts and then commit the result.
   # Edit line by line, removing undesired changes
   $ vim <FILENAME>
   $ git add <FILENAME>
   $ git commit -m "Resolved merge conflict in <FILENAME>"

Alternatively, one of the branches may be chosen to resolve the merge. Where
there are conflicts, the chosen branches version will be selected for the merge
commit.

.. code-block:: text

   # Resolving conflicts by favoring a branch:
   $ git switch main
   $ git merge <BRANCH_TO_MERGE>
   CONFLICT (content): Merge conflict in <FILENAME>
   Automatic merge failed; fix conflicts and then commit the result.
   # "ours" and "theirs" terminology is used. Since the perspective is from
   # the main branch, "ours" will mean the main branches version.
   $ git checkout --ours <FILENAME>
   $ git add <FILENAME>
   $ git commit -m "Resolved merge conflict in <FILENAME>"

The git mergetool command, or IDEs built in tools (like VS Code) can be used
for more sophisticated manual merging.

Stashing Work
=============

If you want to switch branches while in the middle of work, you may stash the
state of your current branch so that you can revisit it later.

.. code-block:: text

   # Stash current working directory
   $ git stash
   # View list of stashes
   $ git stash list
   # Revert to stashed state
   $ git stash apply

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

Changing History
^^^^^^^^^^^^^^^^

Generally git commit history should only be changed when those changes have
only ever existed on your local computer. Changing git history on aremote will
change the history for many others, and will create pointless work in order to
resolve.

.. code-block:: text

   # Replace the last commit message
   $ git commit --amend
   # The most recent commit will be replaced, and its SHA-1 hash updated
   # Use the interactive mode of the git rebase command for more flexible
   # editing of history
   $ git rebase -i
   $ git checkout main
   $ git merge <BRANCH_TO_MERGE>
   # (Alternatively) Squashing a feature branch during merging
   $ git merge --squash <BRANCH_TO_SQUASH>

Squashing
^^^^^^^^^

Commit history can be squashed to condense multiple commits into a single
commit. This is useful when writing a feature branch, to condense a longer
history of commits into a single cohesive commit for a clean history. Generally
this is considered good practice. Squashing, like rebasing alters commit
history so is only viable for local branches. Feature branches can first be
rebased onto the latest history of main, before squashing for the cleanest
and simplest commit history.

.. code-block:: text

   # Squash all commits from the specified branch into current branch
   $ git squash <BRANCH_TO_SQUASH>

Ignoring Files with .gitignore
==============================

It is desirable to not track files that are irrelevant to a repo, or simply too
large to track (>1MB is a good threshold to consider ignoring).

Ignoring files can be managed in git with the .gitignore file.
the .gitignore file is a file placed in your repository that specifies patterns
of files to be ignored by git.

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

In order to stop git from tracking a folder that was previously tracked that
you would like to ignore:

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
^^^^^^^^^

Software licenses specify how others can use, modify, and distribute your code.
Not having a license would mean that you reserve all rights to your code,
pending any software use agreements provided by the hosting service.

Github can be used to automatically generate popular license files.
MIT or Apache 2.0 are popularly recommended open source licenses.
