#!/bin/bash
FILE="`pwd`/ahab.py"
if test -f /usr/local/bin/ahab; then
  echo "Link already exists"
  exit 1
fi
sudo ln -s $FILE /usr/local/bin/ahab
