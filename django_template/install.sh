#!/bin/bash
base_python_interpreter="/usr/bin/python3.9"
project_name=""
project_path=""

# read -p "Python interpreter: " base_python_interpreter
read -p "Project name: " project_name
read -p "Project path: " project_path

python3.9 -m venv $project_path/$project_name/venv
. $project_path/$project_name/venv/bin/activate

# Libraries
pip install -U pip
pip install django
pip install Pillow
pip install requests
pip install dj-database-url
pip install django-cleanup

cp manage.py $project_path/$project_name/
cp config $project_path/$project_name/
