# TurboStock

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
(venv) Windows\TurboStock\TurboStock$ python manage.py makemigrations
```

3. Populate DB
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py loaddata <fixture>
```
Several fixtures are available (if starting from an empty DB, follow the order):
* populate_stores
* populate_users
* populate_aisles
* populate_products
* populate_stocks

4. Run server
```Shell
(venv) Windows\TurboStock\TurboStock$ python manage.py runserver
```

## Usage

1. Use admin credentials to connect (email : admin@turbostock.fr, password : turbostock)
