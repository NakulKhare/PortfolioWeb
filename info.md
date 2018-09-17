# Django model creation
1. Django model creation
    > go to app > models > create model
    
2. use the migration commands
    > python manage.py migrate
    
    > python manage.py makemigrations
    
    > python manage.py migrate
    
3. add app in settings.py
    INSTALLED_APPS = [
    'django.apps.JobsConfig' (i added this),
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]

4. add media root in settings.py
    > MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    
    >MEDIA_URL = '/media/'
    
5. register in apps > admin.py
    > from .models import Jobs

    > admin.site.register(Jobs)
    
6. show the media file urls.py add this
    > from django.conf.urls.static import static
    
    > from django.conf import settings

    urlpatterns = [
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
 # Setting mysql database in django on the place of sqlite
 1. create a databse in phpmyadmin
 
 2. install module
    > https://stackoverflow.com/questions/46902357/error-loading-mysqldb-module-did-you-install-mysqlclient-or-mysql-python
    
    > create super user again and login
    
 # Showing dat in template
    > add home page in urls.py
    
    > add template in >templates >jobs >home.html
    
 # serving static file
    > STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
    > STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    > STATIC_URL = '/static/'
    
    >run command:
    python manage.py collectstatic