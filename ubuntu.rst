===============
Common commands, symbols, and special variables
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
| $_ : special variable that refers to the last argument of the previous command

===============
Man Pages
===============

TODO

===============
Linux Directory Structure
===============

TODO

===============
Scripts
===============

TODO

===============
Aliases
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

===============
Chaining shell commands
===============

&& : Performs the following command only if the previous command succeeds
|| : Performs the following command only if the previous command fails

Pipes connect the stout of the previous command to the stin of the following command.

Example:
cat file.txt | grep "error" && echo "Errors found!" : prints "Errors found!" if file.txt contains lines that contain the word "error"

===============
Makefiles
===============

TODO
