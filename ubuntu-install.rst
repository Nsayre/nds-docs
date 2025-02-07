===============
One time install
===============

# TODO figure out $XDG_CONFIG_HOME and consolidate configs

# NOTE update, upgrade, and install all apps first

sudo apt-get update && sudo apt-get -y upgrade

sudo apt install neovim git keychain gh curl zsh i3 docker.io nginx tldr python3-venv build-essential

# Remove snap firefox and install .deb firefox
Can follow instructions here: https://support.mozilla.org/en-US/kb/install-firefox-linux

# Change default shell to zsh
chsh -s /usr/bin/zsh
# Verify change via running echo $0 to print current running shell

# Change default terminal to Alacritty
# TEST the following command, I think it works
sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator /usr/bin/alacritty 50
# Alternatively... use the following and select from the list of options
sudo update-alternatives --config x-terminal-emulator

# Download alacritty themes and set zenburn
mkdir -p ~/.config/alacritty/themes
git clone https://github.com/alacritty/alacritty-theme ~/.config/alacritty/themes

# edit the following into alacritty.toml which needs to be created at ~/.config/alacritty/alacritty.toml
# NOTE if alacritty.toml was in dotfiles, not necessary
import = [
    "~/.config/alacritty/themes/themes/zenburn.toml"
]

Install powerlevel10k
# NOTE, if ~/.p10k.zsh was copied in dotfiles, no config is necessary
# clone repo, the following line must be in .zshrc
# echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
# TODO install recommended fonts, see github repo

# Login required?

# install nvim plugins by running the following inside nvim
:PlugInstall

# sign in to 1password and link to firefox plugin
Follow instructions on https://developer.1password.com/docs/cli/get-started/

# Install 1password cli
# WARNING Not sure if this is actually necessary...
Follow instructions on https://developer.1password.com/docs/cli/get-started/
# op signin
# op plugin init gh
# Follow prompts


# Change firefox settings
type about:config into address bar and set
browser.sessionstore.restore_on_demand = false
browser.sessionstore.restore_tabs_lazily = false
