#!/bin/bash
FILE="`pwd`/ahab.py"
if test -f $FILE; then
  echo "Link already exists"
  exit 1
fi
sudo ln -s $FILE /usr/local/bin/ahab
