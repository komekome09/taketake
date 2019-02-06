#!/bin/bash
echo "-----------------------------"
echo "[LOG]($(date)): take.sh start"
echo "[LOG]($(date)): \$HOME = $HOME"
type direnv > /dev/null 2>&1 && eval "$(direnv hook zsh)" 
[[ -s $HOME/.pythonz/etc/bashrc ]] && source $HOME/.pythonz/etc/bashrc

/usr/local/bin/direnv exec /home/komekome09/take python /home/komekome09/take/take.py
echo "[LOG]($(date)): take.sh end"
