import os

def runserver():
    os.system("python manage.py runserver")

def makemigrations():
    os.system("python manage.py makemigrations")

def migrate():
    os.system("python manage.py migrate")


