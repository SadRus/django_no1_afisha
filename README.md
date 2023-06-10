# django_no1_afisha

### Description  
Interactive map shows the most popular places added by author.

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
- `STATIC_ROOT` - folder where **collectstatic** will save files before deploy.
- `MEDIA_ROOT` - folder for storage user uploaded files.

### Usage  

### Development

- Apply migrations:  
```python manage.py migrate```

- Create the superuser:  
```python manage.py createsuperuser```

- Run the server:  
```python manage.py runserver```

- For adding new locations go to http://127.0.0.1:8000/admin to places http://127.0.0.1:8000/admin/places/place/ 
