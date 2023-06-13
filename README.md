# django_no1_afisha

### Description  
Interactive map shows the most popular places added by author.  
My example:  
https://sadrus.pythonanywhere.com/  

Test ownership data from the site  
https://github.com/devmanorg/where-to-go-places  
![image](https://github.com/SadRus/django_no1_afisha/assets/79669407/ffffa3f5-ab98-4134-98db-dab16400a4f1)  

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

Example of JSON format
```JSON
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```
