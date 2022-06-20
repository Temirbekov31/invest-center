import imp
from operator import index
from . import views
from django.urls import path
from .views import AddprojectListView, IT_ru, PlaceOfBirth_ru, Production, Production_ru, allProjects,IT,PlaceOfBirth, allProjects_ru,commerce, commerce_ru,energy, energy_ru
urlpatterns = [
    path('' ,AddprojectListView.as_view(), name= 'home'),
    path('about/', views.about, name='about'),
    path('about_copy/', views.about_copy, name='about_copy'),
    path('contact/', views.contact, name='contact'),
    path('Project/', views.Project, name='project'),

    

    #РУССКИЙ ЯЗЫК
    path('Главная/', views.Default_Rus, name='home_ru'),
    path('О нас/', views.About_RU, name='about_ru'),
    path('Контакты/',views.Contact_RU, name='contact_ru'),
    path('Главное/',views.Default_Rus, name='default_ru'),



    #ПРОЕКТЫ 
    path('Производство/', Production_ru.as_view(), name='production_ru'),
    path('IT_РУ/', IT_ru.as_view(), name='IT_ru'),
    path('Коммерция/', commerce_ru.as_view(), name='commerce_ru'),
    path('Энергетика/', energy_ru.as_view(), name='energy_ru'),
    path('Месторождения/', PlaceOfBirth_ru.as_view(), name='place_ru'),
    path('Все/', allProjects_ru.as_view(), name='all_ru'),


    #PRODUCTIONS
    path('IT/', IT.as_view(), name='IT'),
    path('commerce/', commerce.as_view(), name='commerce'),
    path('energy/', energy.as_view(), name='energy'),
    path('PlaceOfBirth/', PlaceOfBirth.as_view(), name='place'),
    path('production/', Production.as_view(), name='production'),
    path('All/projects/',allProjects.as_view(), name='all'),



    path('applicants', views.applicants, name='applicants'),
    path('applicants/ru', views.applicants_RU, name='applicants_ru'),

    path('kr', views.aboutKR, name='kr'),
    
]
