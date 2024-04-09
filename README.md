# Safe-Haven
 
Authors: 

Ilan Travin - ilantr@ac.sce.ac.il

Emil Abdumalikov - emilab@ac.sce.ac.il

Nitzan Steiner - nitzast@ac.sce.ac.il

Description:

The project is part of a "Fundamentals in Software Engineering" course. We are group #4. This is a website for Hosting families in times of danger, and also for aid organizations that want to help.

The website has three users:

admin -

host/donator -

hosted family - 


Environment:
the code was devloped on pycharm, the framework is django 4.0.0, most of the code is python, but we have some html and css code. Database: SQlite3

for windows:
1. open terminal through pycharm
2. myenv\Scripts\activate.bat
3. py manage.py runserver

for macos:
1. open terminal through pycharm
2. source myenv/bin/activate
3. python3 manage.py runserver

How to run:
git clone https://github.com/

Requirements:
pip install asgiref
pip install Django   
pip install django-filter  
pip install Pillow 
pip install pip
pip install reportlab 
pip install sqlparse
pip install tzdata
pip install xlwt

Create tables
 python manage.py makemigrations
 python manage.py migrate
 
Start the application (development)
python manage.py runserver
Access the web app in browser: http://127.0.0.1:8000/

Unit Test:
python manage.py test                # all tests
python manage.py test aid_org        # organization test
python manage.py test forum          # donation request test
python manage.py test Donations      # Donations test
python manage.py test host           # host test
python manage.py test hosted         # hosted test
python manage.py test Report         # Report test
python manage.py test success_story  # success_story test

