#basic directories
mkdir ~/bin ~/resources ~/downloads

#install dotfiles into their rightful places
git clone http://github.com/evidlo/dotfiles ~/resources/dotfiles
cd ~/resources/dotfiles
cp -R .bashrc .eaglerc .git .spacemacs .urxvt .vim .vimperator .vimperatorrc .vimrc .XCompose .Xdefaults ~/
rsync -a .config/ ~/.config/

#install basic utilities
yes|sudo apt-get install vim man htop ncdu tar zip git autojump expect wget aria2 nload gcc octave


#set up i3
# git clone http://github.com/evidlo/i3config
# mv i3config ~/.i3
# mv ~/.i3/statusline_evidlo ~/.i3/i3_custom_status
# chmod +x ~/.i3/startup

#set up scripts 
# git clone http://github.com/evidlo/scripts ~/resources/scripts

######### Desktop Stuff ###############
#yes|sudo apt-get install i3 mpv emacs emacsclient rxvt-unicode-256color acpi mirage shotwell evince feh powertop
#git clone http://github.com/syl20bnr/spacemacs ~/.emacs.d

#yes|sudo apt-get install python3-qt5 python3-sip
#yes|sudo pip3 install qutebrowser mps-youtube
