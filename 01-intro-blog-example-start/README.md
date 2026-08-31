# Intro to Django and Backend Web Development fundamentals

In this example we'll be going through the basics of Django and backend web development. This is a simple blog application that will allow you to create, read, update and delete blog posts. We'll be using Django's built in admin interface to manage the blog posts.


## Steps

1. Create a virtual envirnment and install Django
`python3 -m venv ./venv`

activate the virtual environment:
- linux/mac: `source ./venv/bin/activate`
- windows: `.\venv\Scripts\activate`

2. install django (we'll be using version 5.2) and freeze the requirements:
`pip install django==5.2`


`pip freeze > requirements.txt`
Note: this will create a requirements.txt file that contains all of the packages that are installed in the virtual environment. This is important for deployment and sharing the project with others.

3. Create a new Django project called `myblogwebsite`:
- checkout what the `django-admin` is doing:
You should see something like this:
```
$ django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```
Note, we'll be discussing a lot of these commands in this course. For now we'll be creating

- create a new project called `myblogwebsite`:
`django-admin startproject myblogwebsite`
This will create a new directory called `myblogwebsite` with the following structure:
```
myblogwebsite/
    manage.py
    myblogwebsite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
- if you see the above then your project is set up correctly!
4. Let's run the project to make sure everything is working
`python manage.py runserver`
Note: you need to navigate to the `myblogwebsite` directory before running this command. This will start the development server and you should see something like this:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 06, 2025 - 14:36:02
Django version 5.2, using settings 'myblogwebsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
```

5. Open your browser and navigate to `http://localhost:8000/` and you should see the following page
![image](images/started_successfully.png)

6. Let's take a look at the project structure and the files that were created. The most important files are:
- `manage.py`: this is the main entry point for the project. You can use this to run the server, create migrations, and other commands.
  - you already used this to run the server with `python manage.py runserver`. This is the main entry point for the project.
- `myblogwebsite/settings.py`: this is where you configure the project. You can set the database, static files, and other settings here.
  - You'll be using this a lot in this course. This is where you configure things for the project. In this course we'll be using a lot of default settings but we'll be customizing a ton of them:
    - `INSTALLED_APPS`: this is a list of apps that are installed in the project. You can add your own apps here and configure them.
    - `STATIC_URL`: this is the URL that is used to serve static files. You can set this to `/static/` for development but you should set this to the domain name for production.
    - `TEMPLATES`: this is a list of templates that are used in the project. You can add your own templates here and configure them.
    - `DATABASES`: this is where you configure the database. You can set the database engine, name, user, password, and other settings here.
    - `ALLOWED_HOSTS`: this is a list of hosts that are allowed to connect to the server. You can set this to `['*']` for development but you should set this to the domain name for production.
    - `MIDDLEWARE`: this is a list of middleware that are used in the project. Middleware are classes that process requests and responses. You can add your own middleware here and configure them.
  - We'll be discussing a lot more of these settings in this course. For now, you can leave them as is.
- `myblogwebsite/urls.py`: this is where you define the URL patterns for the project. You can map URLs to views here.
  - This is where you define the URL patterns for the project. You can map URLs to views here, we're going to be using this a lot in the course.
- `myblogwebsite/wsgi.py`: this is the entry point for the WSGI server. You don't need to worry about this for now.
  - This is the standard way to deploy Django applications. You can use this to run the server in production. We won't need to worry about this for now.s
- `myblogwebsite/asgi.py`: this is the entry point for the ASGI server. You don't need to worry about this for now.
  - Note We won't be using this for this course but it's a great way to build web applications that are asynchronous and require concurrent connections. This is a great way to build applications that require real time updates like chat applications, games, etc.
