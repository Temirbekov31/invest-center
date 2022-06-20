from operator import mod
from django.db import models
from distutils.command.upload import upload
from turtle import title
from django.contrib.auth import admin
from django.db import models
from django.urls import reverse

# Create your models here.

class Addproject(models.Model):
    IT = 'it'
    COMMERCE = 'commerce'
    ENERGY = 'energy'
    PRODUCTION = 'production'
    PLACEOFBIRTH = 'placeofbirth'

    EN = 'en'
    RU = 'ru'
    
 
    CHUY = 'Chuy'
    TALAS = 'Talas'
    ISSYK_KUL = 'Issyk-kul'
    JALAL_ABAD = 'Jalal-abad'
    NARYN = 'Naryn'
    OSH = 'Osh'
    BATKEN = 'Batken'

    CHOICE_REG = {
        (CHUY, 'Chuy'),
        (TALAS, 'Talas'),
        (ISSYK_KUL, 'Issyk-kul'),
        (JALAL_ABAD, 'Jalal-abad'),
        (NARYN, 'Naryn'),
        (OSH, 'Osh'),
        (BATKEN, 'Batken'),
    }

    CHOICE_LANG = {
        (EN,'en'),
        (RU,'ru')
    }



    CHOICE_GROUP = {
        (IT,'it'),
        (COMMERCE,'commerce'),
        (ENERGY,'energy'),
        (PRODUCTION,'production'),
        (PLACEOFBIRTH,'placeofbirth'),
    }

    title = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(upload_to = 'image/', blank = True)
    date = models.DateTimeField(auto_now_add=True)
    prices = models.ForeignKey('Price',on_delete=models.SET_NULL, verbose_name="Цена",null=True)
    group = models.CharField(max_length=20 ,choices=CHOICE_GROUP)
    lang = models.CharField(max_length=20 , choices=CHOICE_LANG, default='ru')
    region = models.CharField(max_length=20, choices=CHOICE_REG)
    def __str__(self):
        return self.title


        

class Price(models.Model):
    name = models.CharField("Цена", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"




from django.db import models



class Form(models.Model):
    company = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    add1 = models.CharField(max_length=300)
    add2 = models.CharField(max_length=300)
    zipC = models.IntegerField()
    state = models.CharField(max_length=150, default=None)

    first_name = models.CharField(max_length=123, default=None)
    last_name = models.CharField(max_length=123, default=None)
    email = models.EmailField(max_length=123, default=None)
    phone = models.IntegerField(default=None)    
    image = models.ImageField(upload_to='images', default=None)


    def __str__(self):
        return self.company
