===============
Common Commands
===============
git clone :
git pull :
git push : 
git status :

===============
Cloning a directory
===============

TODO

===============
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

===============
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

===============
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

