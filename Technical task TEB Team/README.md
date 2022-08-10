## Technical task in the TEB Team for position Junior Python Developer

#### Requirements
 - Python 3

#### Installation
- Clone the project from GitHub to your local PC:
```
$ git clone https://github.com/RomanSimachenko/Django.git
$ cd ./Django/Technical task TEB Team/
```
- (Optional) Change environment variables in `setenv.sh`

- Create virtual environment, activate it and environment variables:
```
$ python3 -m venv venv
$ source ./venv/bin/activate && source ./setenv.sh
```

- Install pip packages:
```
$(venv) pip install -r requirements.txt
```

- Do migrations:
```
$(venv) python3 ./manage.py makemigrations && python3 ./manage.py migrate
```

- (Optional) Create superuser:
```
$(venv) python3 ./manage.py createsuperuser
```

#### Running
- Django site: `$(venv) python3 ./manage.py runserver localhost:8000`
- Telegram bot: `$(venv) python3 ./bot.py`

Then, you can access to the site by the address `http://localhost:8000`, and to the Telegram bot by the tag `@TEBTeam_bot`
