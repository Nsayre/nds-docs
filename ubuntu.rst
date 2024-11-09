===============
Common commands & Special symbols
===============
| cd : Change directory
* cd : navigate to previous directory
| touch : change file timestamps (though is used to create empty files)
| ls : List directory contents
| cp : Copy files and directories
| rm : Remove files or directories
* [rm -R] remove a directory and it's contents recursively
| mv : Move a file to a different directory
| man : View the manual of a command
| cat : concatenate files and print on the standard output
| ~ : refers to the HOME directory
| eval : Evaluates and executes strings as a shell command

===============
How to navigate man pages
===============
TODO

===============
Explanation of folders
===============

TODO
===============
How to write and execute scripts

===============
TODO
===============
How to setup an alias
===============
TODO

===============
Environmental variables
===============
TODO

===============
How to install a .deb file on ubuntu
===============

sudo dpkg -i filename.deb

If the previous command fails, then run the following command to resolve missing dependencies

sudo apt-get install -f

===============
Essential packages
===============
sudo apt update
sudo apt install neovim git keychain gh curl
sudo apt upgrade
TODO manage automatically
