# My Users and Posts site

## Development

#### Dependencies
1. Python 3.8+

#### Installation
1. Create virtual environment `$ python/python3 -m venv venv`
2. Install all the requirements `$ pip install -r requirements.txt`

At the root of the project (where is `manage.py`) create shell script `$ vim/nano setenv.sh` and add to it next variables:
```
export SECRET_KEY="<django secret key>"
export DEBUG=True
```
Then activate it `$ ./source setenv.sh`

#### Starting
Project can be started using the command `$ python/python3 manage.py runserver localhost:8000` or `$ ./manage.py runserver localhost:8000`