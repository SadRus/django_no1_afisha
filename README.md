# django_no1_afisha

### Description  
Interactive map shows the most popular places added by author.  
My example:  
https://sadrus.pythonanywhere.com/  

Test ownership data from the site  
https://github.com/devmanorg/where-to-go-places

### Objective of project
The app is written for educational purposes within online courses for web developers dvmn.org.

### Installing

Python3 must be installed. 
Use `pip` (or `pip3`) for install requirements:
```
pip install -r requirements.txt
```  

### Enviroment variables

You need to create .env file for the enviroment variables in main folder.  
Enviroment variables includes django settings variables, which you can see in the official documentation: https://docs.djangoproject.com/en/4.2/ref/settings/  
- `ALLOWED_HOSTS` - host/domain names listed with a space (e.g. 'yourproject.pythonanywhere.com').
- `DATABASE` - name of created database.
- `DEBUG` - set False for deployment or True for development.
- `SECRET_KEY` - yours django project secret key from settings.
- `STATIC_ROOT` - folder where **collectstatic** command will save static files for serving by deploy.
- `MEDIA_ROOT` - folder for storage user uploaded files.

### Usage  

- Apply migrations:  
```python manage.py migrate```

- Create the superuser:  
```python manage.py createsuperuser```

- For development run the django server:  
```python manage.py runserver```

- Add locations to database manually:  
Use admin panel http://127.0.0.1:8000/admin

- Or use **load_place** argument to add location from json:  
```python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json```
