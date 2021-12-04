# django-drf-test
Простейшее приложение опроса на django - drf.

open terminal

pip install pipenv 

mkdir polls

cd polls

 clone https://github.com/GolangHack/test_drf_polls.git

cd test_drf_polls

pipenv shell

pipenv install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

open localhost:8000

