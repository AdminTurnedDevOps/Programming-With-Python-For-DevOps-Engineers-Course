https://docs.djangoproject.com/en/3.2/intro/tutorial01/

## Django Projects vs Apps
An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


## Creating a Project

1. `pip install django`

2. Use the django-admin tool to generate a project folder, the basic file templates, and manage.py, which serves as your project management script.

3. `mkdir django-api`

4. `cd django-api`

5. `django-admin startproject localwebsite`

Once you create the `localwebsite`, it contains the following:

- `__init__.py` is an empty file that instructs Python to treat this directory as a Python package.
- `settings.py` contains all the website settings, including registering any applications we create, the location of our static files, database configuration details, etc.  
- `urls.py` defines the site URL-to-view mappings. While this could contain all the URL mapping code, it is more common to delegate some of the mappings to particular applications, as you'll see later.
- `wsgi.py` is used to help your Django application communicate with the webserver. You can treat this as boilerplate.
- `asgi.py` is a standard for Python asynchronous web apps and servers to communicate with each other. ASGI is the asynchronous successor to WSGI and provides a standard for both asynchronous and synchronous Python apps (whereas WSGI provided a standard for synchronous apps only). It is backward-compatible with WSGI and supports multiple servers and application frameworks.
- The `manage.py` script is used to create applications, work with databases, and start the development web server.

6. Start the site: `python manage.py runserver`

By default, Django runs on port `8000`. If you want to change the port, you can pass it in when you run `manage.py` like so:
    `python manage.py runserver 8080`


## Creating an app

1. To create your app, make sure you’re in the same directory as manage.py and type this command:
    `python manage.py startapp cloudskillsapp`

2. Add in the following code to the `views.py` file
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the cloudskills index.")
```

3. Create a file called `urls.py` to map the URL to the new site.

4. In the directory `cloudskillsapp`, add the following code to `urls.py`:
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

5. In the directory `localwebsite`, add the following code to `urls.py`
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cloudskills/', include('cloudskillsapp.urls')),
    path('admin/', admin.site.urls),
]
```