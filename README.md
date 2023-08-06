# OMSLeet
Mock Interviewing Platform for GaTech Students
Nick - test

## Installing Django
Requirements:
- Python 3.10+
- PostgresSQL: https://www.postgresql.org/download/
- NodeJS: https://nodejs.org/it/download/current 
- Django: `python -m pip install Django`

## Create a new project

run : ` django-admin startproject oms_leet_app`
The command will create the following project:
```
oms_leet_app/
    manage.py
    oms_leet_app/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Add your first view

1. Create a file under `oms_leet_app` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Create a new APP:
`python manage.py startapp oms_leet_v2`

Running server `python manage.py runserver`
You’ll see the following output on the command line:
```
    Performing system checks...

    System check identified no issues (0 silenced).

    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.

    August 04, 2023 - 15:50:53
    Django version 4.2, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C. 

```

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

