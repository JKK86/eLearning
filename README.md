# eLearning

An e-learning application built with Django Framework.

## Technologies:
- Python
- Django
- HTML
- CSS

## Setup

First you should clone this repository:
```
git clone https://github.com/JKK86/elearning.git
cd  elearning
```

To run the project you should have Python 3 installed on your computer. Then it's recommended to create a virtual environment for your projects dependencies. To install virtual environment:
```
pip install virtualenv
```
Then run the following command in the project directory:
```
virtualenv venv
```
That will create a new folder venv in your project directory. Next activate virtual environment:
```
source venv/bin/active
```
Then install the project dependencies:
```
pip install -r requirements.txt
```
Now you can run the project with this command:
```
python manage.py runserver
```

**Note** in the settings file you should complete your own database settings.

## Source

This app is based on Antonio Mele book „Django 3”.
