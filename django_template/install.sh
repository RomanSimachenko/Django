#!/bin/bash
base_python_interpreter="/usr/bin/python3"
project_name=""
project_path=""

# read -p "Python interpreter: " base_python_interpreter
read -p "Project name: " project_name
read -p "Project path: " project_path

mkdir $project_path/$project_name

cp manage.py $project_path/$project_name/
cp -r config $project_path/$project_name/
cp -r static $project_path/$project_name/
cp -r templates $project_path/$project_name/

cd $project_path/$project_name/

python3 -m venv venv
. venv/bin/activate

# Libraries
pip install -U pip
pip install django

python manage.py makemigrations
python manage.py migrate

pip freeze > requirements.txt
