#!/bin/zsh

echo "Start"


git init
git remote add origin git@github.com:aktifon/django_rest2.git
git add .
git commit -m 'all'
git push -u origin master

echo "Finish"