# TurboStock

## Download project

Download the project (git clone or zip download) and open a cmd prompt at its base directory (you should see the README.md in this directory)

## Requirements

1. Create a Python 3 virutal environment

```Shell
Windows\TurboStock$ python -m venv venv
```

2. Activate the venv

```Shell
Windows\TurboStock$ venv\Scripts\activate.bat
```

3. Install the requirements

```Shell
(venv) Windows\TurboStock$ pip install -r requirements.txt
```

## Setup & Launch

1. Make migrations
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py makemigrations
```

2. Migrate DB
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py migrate
```

3. Populate DB
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py loaddata <fixture>
```
Several fixtures are available (if starting from an empty DB, follow the order):
* populate_stores
* populate_aisles
* populate_products
* populate_stocks
* populate_users

1. Run server
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py runserver
```

## Usage

1. Create a superuser 
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py createsuperuser
```

2. Connect with the superuser account at http://localhost:8000/admin/ and create a user (CEO, AisleManager, StoreManager)
3. Login at http://localhost:8000/login/

## Tests
1. Run tests
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py test
```

1. Write more tests
```Shell
TurboStock\TurboStock\app\test.py
```

## Structure
Routes
```Shell
TurboStock\TurboStock\app\urls.py
```

Views( controllers )
```Shell
TurboStock\TurboStock\app\views\
```
Models
```Shell
TurboStock\TurboStock\app\models\
```

Templates ( html )
```Shell
TurboStock\TurboStock\app\template\
```

Authentication system
```Shell
TurboStock\TurboStock\app\authentication\
```