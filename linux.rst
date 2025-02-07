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
Audio : pavucontrol : Ubiquity
Shell : zsh : plugins, popularity
Terminal : TODO trying alacritty
Text editor/IDE : neovim : vim style hotkeys and philosophy
Neovim package manager: TODO trying vim-plug 

===============
Common commands, symbols, and special variables
===============

| whatis : Display a one line description of a command
| man : View the manual of a command
| echo : display a line of text
| cd : Change directory
* cd : navigate to previous directory
| touch : change file timestamps (though is used to create empty files)
| ls : List directory contents
ls -l shows file permissions
ls -al shows hidden files
| cp : Copy files and directories
| rm : Remove files or directories
* [rm -R] remove a directory and it's contents recursively
| mv : Move a file to a different directory
| cat : concatenate files and print on the standard output
| ~ : refers to the HOME directory
| eval : Evaluates and executes strings as a shell command
| $_ : special variable that refers to the last argument of the previous command
| source : execute commands from a file in the current shell environment
| curl : makes an http request
* [curl -s https://example.com/data/example.csv > data/example_data.csv] makes the request silently and suppresses progress output and error messages
| zip : package and compress a files
| unzip : list, test, or extract compressed files in a ZIP archive
| chsh : change login shell
chmod : change file mode bits
chmod +x <filename> gives execute permissions
chmod 700 <directory/filename> set permission for .ssh directory
useradd : low level command that requires some flags to setup a fully functional user
adduser :minteractive higher level tool that will prompt information like password, phone number etc.
mserdel : remove a user
userdel -r <username> : removes user and their home directory
usermod: modify a user account
usermod -aG sudo <username> : adds a user to the sudo group
sed: stream editor for filtering and transforming test
sed -i "s/<oldstring>/<newstring>/" <file>
sed -i '$ a This is appended to the last line' file.txt
su : change user
su <username>
passwd : change user password
passwd -d <username> : delete a user's password
scp 
scp myfile.txt user@192.168.1.10:/home/user/
sudo: Execute a command as another user
sudo -u <username> : run command as username user
chown: Change file ownership
chown <USER>:<GROUP> <FILE>

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

NOTE: Software installed from .deb files will only be able to update if you enable an associated repository, by default they do not update when <apt get upgrade> is run

sudo dpkg -i filename.deb

If the previous command fails, then run the following command to resolve missing dependencies

sudo apt-get install -f

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

===============
How to handle zipped files
===============

TODO
