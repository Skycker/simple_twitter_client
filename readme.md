# About

Simple twitter client 

# Local run

To run the project locally

* clone repo
* `cd simple_twitter_client/`  
* `virtualenv venv --prompt='(stc)'`  
* `source venv/bin/activate`  
* `pip install *r requirements.txt`  
* create file `simple_twitter_client/local_settings.py`  
* create database, user, grant perms to user  
* run migrations `./manage.py migrate`
* create superuser `./manage.py createsuperuser`
* run development `./manage.py runserver`  
* make sure that Site for your domain exists (django.contrib.sites instance matching settings.SITE_ID). [http://127.0.0.1:8000/admin/sites/site/](http://127.0.0.1:8000/admin/sites/site/)
* go to [http://127.0.0.1:8000/admin/socialaccount/socialapp/](http://127.0.0.1:8000/admin/socialaccount/socialapp/)  and create new record
  * Fill data about social app 
    * Provider: twitter  
    * Name: for app (for example `twitter social app`)
    * Client id 
    * Secret key
    * Sites: select site in with settings.SITE_ID 
* go to `http://127.0.0.1:8000/` and check the project  

**Development local_settings.py example**

    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<db name>',
            'USER': '<db user>',
            'PASSWORD': '<db user password>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


