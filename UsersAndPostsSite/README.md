# My Users and Posts site

## Development

#### Dependencies
1. Python 3.8+

#### Installation
1. Create the virtual environment `$ python/python3 -m venv venv` then activate it `$ source/. venv/bin/activate`
2. Install all the requirements `$ pip install -r requirements.txt`
3. Do makemigrations and migrate `$ python/python3 manage.py makemigrations` then `$ python/python3 manage.py migrate`

At the root of the project (where is `manage.py`) create shell script `$ vim/nano setenv.sh` and add to it next variables:
```shell
export SECRET_KEY="<django secret key>"
export DEBUG=True
```
Then activate it `$ source/. setenv.sh`

#### Starting
Project can be started using the command `$ python/python3 manage.py runserver localhost:8000` or `$ ./manage.py runserver localhost:8000`