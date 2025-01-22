===============
Secure Shell (SSH)
===============
SSH protocol is a cryptographic network protocol for operating network services securely over an unsecured network.
Regarding security, it has the advantage of not exposing username or password information.
SSH uses public-key cryptography to authenticate the remote computer and allow it to authenticate the user, if necessary.
In public-key cryptography each key consists of a public key and a private key.
TODO What is a key? What are the relationship between public and private?
Keeping the private key secret is critical to keeping the key secure. 
The public key can be shared without compromising security.
Metaphorically, public keys are compared to physical locks while private keys are compared to physical keys.

===============
How to create an SSH key, add it to ssh-agent, upload public key, and verify connection to github
===============
Before generating a new key, it is a good idea to check for existing keys to prevent unnecessary overwriting and to audit what is already present.
List the contents of the .ssh directory, if they exist.
$ ls -al ~/.ssh
Create a new SSH key.

ssh-keygen -t ed25519 -C "your_email@example.com"

Adding your SSH key to ssh-agent
Manually start the ssh-agent in the background.

eval "$(ssh-agent -s)"

Manually add your SSH private key to the ssh-agent.

ssh-add ~/.ssh/id_ed25519

TODO Rather than manually do this every shell session, or add these steps to ~/.bashrc (or .zshrc etc.) keychain can be used to manage starting the ssh-agent and adding private keys.
Keychain allows easily having one long running ssh-agent process per system, rather than one ssh-agent instance per login.

sudo apt-get install keychain

add the following to ~/.bashrc to run keychain on every new shell instance

eval `keychain --eval id_rsa`

Print the public key to the console
$ cat ~/.ssh/id_ed25519.pub
Attempt to SSH to github
ssh -T git@github.com
