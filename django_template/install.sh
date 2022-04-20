#!/bin/bash
base_python_interpreter="/usr/bin/python3"
project_name=""
project_path=""
app_name=""

# read -p "Python interpreter: " base_python_interpreter
read -p "Project name: " project_name
read -p "Project path: " project_path

mkdir $project_path/$project_name

cp manage.py $project_path/$project_name/
cp -r config $project_path/$project_name/

cd $project_path/$project_name/

# Virtual environment
python3 -m venv venv
. venv/bin/activate

mkdir -p static/{css,fonts,img,js}
mkdir -p templates/include
touch templates/base.html

# Libraries
pip install -U pip
pip install -U setuptools
pip install autopep8
pip install django

./manage.py makemigrations
./manage.py migrate

pip freeze > requirements.txt

read -p "App name: " app_name

./manage.py startapp $app_name

touch $app_name/urls.py
mkdir -p $app_name/templates/$app_name
touch $app_name/templates/$app_name/index.html
