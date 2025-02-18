<!-- install virtual environment -->
pip install virtualenv

<!-- create virtual environment -->
virtualenv environment_name
python -m virtualenv env
python -m venv env

<!-- activate virtual environment -->
env\Scripts\activate(PS,cmd)
source env\Scripts\activate

<!-- install django -->
pip install django

<!-- freeze the packages -->
pip install -r requirements.txt

<!-- create django project -->
django-admin startproject project_name .  ['.' is optional]

<!-- start server -->
python manage.py runserver

<!-- create app -->
python manage.py startapp todo

<!-- migration file -->
python manage.py makemigrations

<!-- create db table -->
python manage.py migrate

<!-- view all data -->
Model_name.objects.all()

<!-- create data -->
Model_name.objects.create(fields="...", fields2 = "...")

<!-- view single data -->
a = Model_name.objects.get(field_name = ...)

<!-- updata data -->
a.field_name = "...."
a.save()

<!-- delete data -->
Model_name.objects.get(field_name = ...).delete()
a.delete()

<!-- filter data-->
Model_name.objects.filter(field_name1 = ..., field_name2 = ...)

<!-- count data -->
Model_name.objects.filter(field_name = ...).count

