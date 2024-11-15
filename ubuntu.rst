===============
Terminology
===============

| command line: A text-based interface for a user to interact with an operating system.
| shell : The program that accepts user input and returns their output
| terminal : A windowed application that displays the input and output of command line commands.

===============
Software Selections and Motivations
===============
OS : Ubuntu : Stability
Shell :
Terminal :
IDE :


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
| source : execute commands from a file in the current shell environment
| curl : makes an http request
* [curl -s https://example.com/data/example.csv > data/example_data.csv] makes the request silently and suppresses progress output and error messages

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

The make command will execute a makefile (typically named "Makefile"). Makefiles are a convenient way to automate repetitive tasks such as software compilation.
A makefile consists of targets, dependencies, and commands.

Target : The file or action you want to create or run (Ex: myprogram)
Dependencies: Files that are needed to create the target (Such as source code files)
Command : the command to execute to create the target (Ex: gcc -o myprogram main.c)
