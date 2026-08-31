# Deployment on a PaaS provider

In this last example for the course we're goign to walk through how to deploy a django app to a PassProivder. Since [REnder.io](https://render.com/) is a popular and easy to use PaaS provider, which a free tier that is sufficient for small projects, we're going to use Render for this example. The process for deploying to other PaaS providers is similar, so you can use the same steps and just adjust for the specific provider you're using.

We're going to take oiur existing announcements project (from earlier in the course) to Render and deploy it so that it's accessible on the internet. This will involve some changes to our code to prepare it for deployment, as well as some configuration on the Render side to get it up and running.

[Reference to the render docs here](https://render.com/docs/deploy-django) if you'd like to explore more.


## Prerequisites
- Create a new virtual environment and install the packages from the `requirements.txt` file.

## Steps

### 1. Let's talk about deployments and signup for Render.

Deployment are the process of taking your application from your local development environment and making it accessible to users on the internet (this is called the production environment or production for short). This involves several steps, including preparing your code for deployment, configuring your hosting environment, and actually deploying your code.

Getting your backend application from your local machine to hosting provider does take a lot of knowledge here , and that's why as well you folks have a course in the future to cover all of the ins and outs in detail.

Sign up for a Render account if you don't have one already. You can use the free tier for this example, which should be sufficient for our needs.

### 2. Prepare the databases, static file serving, and environment variables so we can configure for differnent environments (development and production).

Note: we've moved the `requirements.txt` file to the root of the project.

- So far in this course we've been using `sqlite` as our database, but now we're going to make our configuration flexible so that we can use a different database in production.

- install required packages for postgres and save them to our `requirements.txt` file.
```
pip install psycopg2-binary
pip install dj-database-url
pip install python-dotenv
pip install whitenoise[brotli]
pip freeze > requirements.txt
```
What did we do here.
- `psycopg2-binary` is a package that allows us to connect to a Postgres database from our Django application.
- `dj-database-url` is a package that allows us to parse the database URL provided by Render and convert it into a format that Django can understand.
- `python-dotenv` is a package that allows us to load environment variables from a `.env` file, which is useful for managing our environment variables in development.
- `whitenoise` is a package that allows us to serve static files in production without needing to set up a separate static file server. This is common in servers that use an nginx webserver (this is a large topic but we can discuss it).

### 3. Let's set up our environment variables and use them in our settings file.

An environment variable is a variable that is set outside of your application and can be accessed by your application at runtime. This is useful for storing sensitive information like database credentials, API keys, etc. that you don't want to hardcode in your code.

In our case we're going to have one environment for:
- development: which is our local machine.
- production: which is the environment on Render where our application will be hosted.

#### 3.1 Create a `.env` file in the root of your project and add the following environment variables:
Let's add the following environment variables to our `.env` file:
```
DEBUG=True
SECRET_KEY=django-insecure-ghoz*3ykeb#bn5k8w!0*h%tm_028r$za!bejs3xme+pk6#5+x=
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost
```

Take note that `.env` files should NEVER be committed to version control (e.g. git) since they contain sensitive information. Make sure to add `.env` to your `.gitignore` file.

#### 3.2 Update your `settings.py` file to use the environment variables.
At the top of the file import and load the envrionment variables using `python-dotenv` and `dj-database-url`:
```python
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()
```
Then update the `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `DATABASES` settings to use the environment variables:
```python
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True' # to convert to a boolean
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") # will be an array of hosts


# ...other settings...
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
}
```

You can test this by taking a look at the shell and running the follwoing commands:
```python
from django.conf import settings
print(settings.SECRET_KEY)
print(settings.DEBUG)
print(settings.ALLOWED_HOSTS)
print(settings.DATABASES)
```
This should print out the values from your `.env` file.
The `dj_database_url` converts your db string into a format that Django can understand, if it looks a bit different than what you're used to, that's why.

### 4. Let's set up our static files configuration for both different environments.

In production, we need to serve our static files (CSS, JavaScript, images, etc.) in a way that is efficient and scalable. In development, Django can serve static files for us, but in production we need to use a different approach. One common approach is to use a package like `whitenoise` which allows us to serve static files directly from our Django application without needing to set up a separate static file server.

To set up `whitenoise`, we need to do the following:
- Add `whitenoise` to our `MIDDLEWARE` in `settings.py`:
```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", # add this line
    # ... other middleware ...
]
```
- change the static files configuration so that it's different for development and production. In development, we can use the default static files configuration, but in production we need to tell `whitenoise` where to find our static files. We can do this by adding the following lines to our `settings.py`:
```python
# static files configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# production level static files
if not DEBUG:
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": ("whitenoise.storage.CompressedStaticFilesStorage"),
        },
    }

```


MEDIA FILES NOTE:
- here we're not going to deal with media files as this is a large topic on it's own, but in production you would also need to set up a way to serve media files (files uploaded by users) which is different than static files.


### 5. Let's use Gunicorn and Uvicorn as our production web server.

S o far in development we've used the built in Django dev server to run our application which is great for development but is not suitable for production.

In production, we need to use a more robust web server that can handle multiple requests at the same time and is more performant. Two popular web servers for Django applications are Gunicorn and Uvicorn, this is what render uses under the hood to run Django applications.

Let's install Gunicorn and Uvicorn and add them to our `requirements.txt` file:
```
pip install gunicorn
pip install uvicorn
pip freeze > requirements.txt
```

Note:
- These will only work on linux based systems, so if you're on windows you won't be able to run these locally, but they will work fine on Render since Render uses linux based servers.
- Linux has a dominant market share in the server world, so it's important to be familiar with linux based tools and commands even if you're on windows or mac for development, you will learn this more in the devops course.

### 6. Let's create a git repository and push our code on github.

Move this folder in a folder that isn't in a git repository already (check with `git status` which should fail), then run the following commands to create a new git repository and push your code to github:
- Create the repo
```
git init
git add .
git commit -m "Initial commit"
```
- Create a repo on github and push your code (replace the remote_url with your repo url with no <>)

```
git remote add origin <remote_url>
git branch -M main
git push -u origin main
```

This is public but since we don't have any sensitive information in our code (since we use environment variables for that) it's fine to have it public. In a real project you would want to make sure to keep your code private if it contains sensitive information.

Note: you can change your github repo to private if you want to keep your code private, but for this example it's not necessary.

### 7. Let's create a new database on render and get the database URL.

In cloud environments (for example like Render, a PaaS provider) you typically create the database separately from your application and then connect to it using a database URL. This is different than in development where we typically use a local database like sqlite that is created and managed by our application.

#### 7.1 On Render click "New Postgres" in the dashboard.

name: `announcements-db`
region: `Oregon`

Then click "Create Database".

It should look something like this:
![Create database](images/1_create_database.gif)

Once created copy the "External Database URL" which should look something like this, save this in a text file for now since we'll need it in the next step:
```
postgres://username:password@hostname:port/databasename
```
Here's where to click:
![External DB Url](images/2_extenal_db_url.png)

There's a lot more to databases in the cloud such as backups, scaling, security, etc. but we'll cover that in the devops course.

### 8. Let's deploy our application to render.

#### 8.1 Let's create an `.env.production` file in the root of our project and add the following environment variables:
In the `.env.production` file add the following environment variables (replace the `DATABASE_URL` with the one you got from Render in the previous step):

```
DEBUG=False
SECRET_KEY=some_random_secret_key
DATABASE_URL=external_database_url_from_render_from_previous_step
ALLOWED_HOSTS=*
```


#### 8.2 Create a new web service on Render.

- Click "New Web Service" in the Render dashboard.
- Connect your github repo (if it's public which should be easier just paste the github repo url).

- Use the following settings (without the ticks):
    - Name: `announcements-app`
    - Root Directory: (ignore this)
    - Region: `Oregon`
    - Branch: `main`
    - Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
    - Start Command: `python -m gunicorn announcements_project.asgi:application -k uvicorn.workers.UvicornWorker`

- Environment Variables click "add from .env file" and select the `.env.production` file we created in the previous step.

Then click "Create Web Service".

It should look something like this:
![Create web service](images/3_build_webservice.gif)

#### 8.3 Wait for the deployment to finish and then click on the URL to see your application live on the internet.

Give yourself a self high five, you just deployed your application to the cloud and it's now accessible to anyone on the internet!

**IMPORTANT NOTE:** Permissions are using the django permission system but we're not adding this on registration for now so if you want to use this you can use:
- the admin panel (add a super user in the build command on render)
- or you can use the `IsTeacherRoleMixin` that we created earlier and add it to the permissions of the viewset, then you can create a user and give them the teacher role and then use that user's credentials to access the endpoints that require the teacher role.

### Troubleshooting:

There's a lot that can go wrong on a deployment and can lead to a lot of frustration, but don't worry it's all part of the learning process and you'll get better at it with time and practice. Here are some tips for troubleshooting:
- Check the logs: Render provides logs for your web service which can be very helpful for troubleshooting. You can check the logs by going to your web service dashboard and clicking on the "Logs" tab. This will show you the output of your application and any errors that may have occurred.
- Check your environment variables: Make sure that your environment variables are set correctly and that they match the ones in your `settings.py` file. A common issue is having a typo in the environment variable name or value.
- Check your database connection: If you're having issues connecting to your database, make sure that your `DATABASE_URL` is correct and that your database is running. You can also try connecting to your database using a database client like pgAdmin to see if you can connect successfully.
- Check your static files configuration: If your static files are not loading, make sure that your static files configuration is correct and that you have run the `collectstatic` command to collect your static files for production.
- Search for the error message: If you see an error message in your logs, try searching for it online. There's a good chance that someone else has encountered the same issue and has posted a solution on a forum like Stack Overflow.

Lot's can go wrong here and it can be frustrating, but with practice and experience you'll get better at troubleshooting and deploying your applications to the cloud.

## Conclusion

In this example, we walked through the process of deploying a Django application to a PaaS provider (Render). We covered how to prepare our code for deployment by using environment variables, configuring static file serving, and using a production web server. We also went through the steps of creating a database on Render and connecting our application to it. Finally, we discussed some common troubleshooting tips for deployments.
