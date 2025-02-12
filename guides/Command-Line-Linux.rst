******************
Command Line Linux
******************

| This guide aims to be a concise and practical guide to the linux command line.

.. only:: comment

   TODO refine the objective.

.. note::
   | Capitalization and angle brackets will be used to indicate placeholders.
   | A placeholder is a symbolic representation of a value. 
   | Ex: Today is <TODAYS_DATE>.


Introduction
============

| The command line is a direct text-based interface to an operating system.
| It is composed of a shell, and a terminal.
| Shell: Parses (interprets) commands and executes them
| Terminal: Graphically displays your commands and their results.
| The command line is powerful, however its usefulness can be limited by your ability to understand its capability.

.. code-block:: text

   # The number sign "#" indicates a comment. 
   # Anything following it on the same line does not affect the command.
   # Anatomy of a command:
   <PROMPT> <COMMAND> <PARAMETER1> <PARAMETER2> <PARAMETER3> ...
   # More specifically:
   <PROMPT> <COMMAND> <OPTIONS> <ARGUMENTS>
   # Examples of commands:
   $ mv Downloads/file1.txt /media/user/backup/
   $ sudo chown -R $USERNAME:$USERNAME /var/www/$DOMAIN

The prompt proceeds the command. It indicates that a line is ready for user input.
The prompt can be customized to display relevant information, however its default behavior reveals whether the current user is a normal user (with a "$" prompt) or the root user (with a "#" prompt). 
The root user is also referred to as the superuser.

.. only:: comment

   TODO link to section on root user, and privileges

A command may be followed by any number of parameters.
Parameters modify the command, changing how it executes and on what it executes.
Parameters can be options or arguments.
Arguments define *what* the command will act on, and options define *how* it will be achieved.

.. code-block:: text

   # The following command lists all files in the Documents directory
   # We can see that a normal user is using the ls command on their 
   # Documents folder and specifying for all files 
   # (including those starting with ".") to be shown.
   $ ls --all /Documents/ 

Getting Help
============

You will need to know various commands and their options in order to get anything done, so knowing how to find help on the command line is important. Searching online for answers is sometimes more efficient, however it carries the risk of being irrelevant or out of date. Nothing beats going to the source of truth, which is the help option and the system reference manuals.

For quick and concise information, appending the --help option to any command is a good start.

.. code-block:: console
   
   $ cp --help
   Usage: cp [OPTION]... [-T] SOURCE DEST
   or:  cp [OPTION]... SOURCE... DIRECTORY
   or:  cp [OPTION]... -t DIRECTORY SOURCE...
   Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
   ...

For more detailed information, it is wise to consult the system reference manual of a command.
The "man" command displays those manuals.

.. code-block:: console
   
   $ man cp   
   (manual pager opens)
   NAME
          cp - copy files and directories

   SYNOPSIS
          cp [OPTION]... [-T] SOURCE DEST
          cp [OPTION]... SOURCE... DIRECTORY
          cp [OPTION]... -t DIRECTORY SOURCE...
   ...
   # You can even look at the manual's manual
   $ man man
   (manual pager opens)
   NAME
       man - an interface to the system reference manuals

   SYNOPSIS
       man [man options] [[section] page ...] ...
   ...

tldr-pages (https://tldr.sh/) aims to simplify man pages and can sometimes be the fastest way to find commonly used commands.

Linux Anatomy
=============
TODO overall structure of the OS, filesystem, inodes, concepts of ownership, group, permissions, distributions

At the highest level all software runs on hardware
's diagram beautifully illustrates how the Linux kernel is at the core of a Linux operating system.
It is perhaps more correct to say that what we call 

Computers execute operating systems (OS) which 

File System
^^^^^^^^^^^
files, special files, directories, inodes

User, Group, and Privilege?
^^^^^^^^^^^^^^^^^^^^^^^^^^
TODO There must be a better term for this

Distributions
^^^^^^^^^^^^^
What actually differs in distributions

Hotkeys
=======

TODO Resume work here.

Ctrl+a to jump to the beginning of the line,
Ctrl+e (I think, my muscle memory is better than my real memory) to jump to the end.
Tab+arrow key to skip words, forward or backwards
Ctrl+r to enter “history search”, you can type the beginning of a command and it’ll auto-fill the last-executed match. Keep pressing to get more matches.

Commands
========

File & System Interaction
^^^^^^^^^^^^^^^^^^^^^^^^^
man
info
exit

history
pwd
cd
ls
alias
unalias
cal
free

mv
cp
rm
mkdir
rmdir
touch
which
locate
find
free
ln
mount
umount

file
zip
unzip
tar

export
env
unset
printenv

df
du
top/htop

uname
hostname

time
systemctl

watch
jobs
kill
pkill
pgrep
shutdown

Text Interaction
^^^^^^^^^^^^^^^^
echo
cat
head
tail
grep
sed
awk
sort
cut
diff
tee

nano/vi/jed

User and Privilege Control
^^^^^^^^^^^^^^^^^^^^^^^^^^
whoami
finger
last
sudo
su
chmod
chown
umask
chgrp
useradd
adduser
userdel
passwd

Network
^^^^^^^
ping
wget
curl
scp
rsync
ip
netstat
nslookup
dig
nmap
ufw
fail2ban

Package Managers
^^^^^^^^^^^^^^^^

Ubuntu:
apt
apt-get

| whatis : Display a one line description of a command
| man : View the manual of a command
| echo : display a line of text
| cd : Change directory
* cd : navigate to previous directory
| touch : change file timestamps (though is used to create empty files)
| ls : List directory contents
ls -l shows file permissions
ls -al shows hidden
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
sed: stream editor for filtering and transforming text
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

Symbols and Special Variables
=============================

Working title, maybe variables is not correct


Scripting
=========

The Shebang
-----------

Set
---
set -x

Chaining Commands
-----------------------

&& : Performs the following command only if the previous command succeeds
|| : Performs the following command only if the previous command fails

Pipes connect the stout of the previous command to the stin of the following command.

Example:
cat file.txt | grep "error" && echo "Errors found!" : prints "Errors found!" if file.txt contains lines that contain the word "error"

Expansions, Aliases, and Environment
------------------------------------
TODO what makes your scrip run differently on my machine.

IO Redirection
-----------------
<
>
2>
2>&1
<()
> /dev/null
&>
1>&2
>>

Handling Text
-------------
Use cases for echo, sed, awk

Here Document
^^^^^^^^^^^^^

Package Management
==================

The Purpose of Package Management
---------------------------------

Package Management on Ubuntu
----------------------------

Types of Packages on Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ubuntu has apt, snap, flatpak, and .deb
TODO correct?

How to install a .deb file on ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NOTE: Software installed from .deb files will only be able to update if you enable an associated repository, by default they do not update when <apt get upgrade> is run

sudo dpkg -i filename.deb

If the previous command fails, then run the following command to resolve missing dependencies

sudo apt-get install -f

SSH
===

Makefiles
=========

The make command will execute a makefile (typically named "Makefile"). Makefiles are a convenient way to automate repetitive tasks such as software compilation.
A makefile consists of targets, dependencies, and commands.

Target : The file or action you want to create or run (Ex: myprogram)
Dependencies: Files that are needed to create the target (Such as source code files)
Command : the command to execute to create the target (Ex: gcc -o myprogram main.c)
