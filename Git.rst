======
Git
======

Common Commands
===============
git clone :
git pull :
git push : 
git status :

Cloning a directory
===============

TODO

Example standard git workflow
===============

Check status of current repository to see if local code is up to date
git status

add changes
git add [filename]  

commit changes
git commit -m "commit message"

push changes
git push origin main

confirm status
git status

Adding local code to github
===============
Initializing a git repository

git init -b main
add all files in current directory
git add .
commit files
git commit -m "First commit"

Adding a local repository to github with Github CLI (follow prompts)
gh repo create

Ignoring files
===============

Files can be ignored in git by adding lines to a file named .gitignore.
Patterns can be specified in this file to ignore files.

Examples:
ignore all .csv files : \*.csv
ignore an entire directory : temp/
ignore a specific file : pattern.gds
make exceptions to previous patterns : !temp/donotdelete.txt

in order to stop git from tracking a folder that was tracked and then added to .gitignore.
git rm -r --cached my_folder

Commit messages
===============

Clear and concise commit messages make approving pull requests easier and facilitate collaborative development. Here are some general guidelines to keep messages clear and concise.

The first line should be a short summary, like a headline, that describes the purpose of the commit. Ideally it is 50 characters or fewer.

If the first line does not adequately describe the changes, then it should be followed by a blank line and a longer detailed description. The detailed description can add detail to the purpose, as well as elaborate on how it was achieved. It can also include any information that would be helpful to reviewers or contributors that will be viewing the message.

All parts of the message should be written in the imperative mood. Example: "Fix typo in README". The main verbs in the imperative mood are in the present tense, unlike non-imperative mood messages like "Fixed typo in README". Imperative mood messages read as if they are commands to achieve what has been done.

Commit messages should include references to relevant issues or tasks. Example: "Fix login validation bug (#123)
