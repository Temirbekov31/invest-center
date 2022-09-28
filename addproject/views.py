from ast import Add
from multiprocessing import context
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import ListView
from requests import request


from addproject.forms import SendCommentForm
from .models import Addproject
from django.db.models import Q
# Create your views here.

class AddprojectListView(ListView):
     model = Addproject
     template_name = 'index.html'
     context_object_name = "projects"

     def get_queryset(self):
          queryset = Addproject.objects.all()
          search = self.request.GET.get('search')
          if search:
               queryset = Addproject.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
          print(search)
          return queryset

# def send_comment(request):
#      form = SendCommentForm(data = request.POST)
#      if form.is_valid():
#           data = request.POST
#           email = data['email']
#           comment = data['comment']
#           number = data['number']
#           fio = data['FIO']
#           address = ['address']
#           date = data['date']
#           pasport = data['pasport']
#           comment2 = ['comment2']
#           contribution = data['contribution']
#           sum = data['sum']
#           assets = data['assets']
#           document = data['document']
#           sphere = data['sphere']
#           payback = data['payback']
#           Yield = data['Yield']
#           actualPlace = data['actualPlace']
#           nameProject = data['nameProject']


#           send_mail('A cool subject', f'{comment}', email, number, fio, address, date, pasport, comment, comment2, 
#           contribution,  sum, assets, document, sphere, payback, Yield, actualPlace,nameProject, [settings.RECIPIENT_ADDRESS])

#           messages.success(request,'Отправлено успешно !!!')
#           return redirect('index')
#      context = {
#           'send_form':SendCommentForm()
#      }
#      return render (request, 'applicants.html',context)


def about(request):
     if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       contact = {
           'name' : name,
           'email' : email,
           'phone' : phone,
       }
       curs = "\n".join(contact.values())
       send_mail('Регестрация на курсы: EN', curs,settings.EMAIL_HOST_USER, ['investcenter.info@gmail.com'],  fail_silently=False)
     return render(request, 'about.html', {})

def about_copy(request):
     return render(request, 'about_copy.html')

def logistic(request):
     return render(request, 'logistic.html')


def contact(request):
     if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       subject = request.POST.get('subject')
       comment = request.POST.get('comment')
       contact = {
           'name' : name,
           'email' : email,
           'phone' : phone,
           'subject' : subject,
           'comment' : comment,
       }
       message = "\n".join(contact.values())
       send_mail('Контактная форма: EN', message,settings.EMAIL_HOST_USER, ['investcenter.info@gmail.com'],  fail_silently=False)
     return render(request, 'contact.html', {})

def Project(request):
     return render(request, 'Project.html')

def index(request):
     return render(request, 'index.html')



#РУССКИЯ ЯЗЫК

def Default_Rus(request):
     return render(request, 'Default_Rus.html')


def About_RU(request):
     return render(request, 'About_RU.html')

def Contact_RU(request):
     if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       subject = request.POST.get('subject')
       comment = request.POST.get('comment')
       contact_ru = {
           'name' : name,
           'email' : email,
           'phone' : phone,
           'subject' : subject,
           'comment' : comment,
       }
       message = "\n".join(contact_ru.values())
       send_mail('Контактная форма', message, settings.EMAIL_HOST_USER, ['investcenter.info@gmail.com'],  fail_silently=False)
     return render(request, 'Contact_RU.html', {})

#Projects



class IT(ListView):
     model = Addproject
     template_name = 'IT.html'

class Production(ListView):
     model = Addproject
     template_name = 'production.html'

class PlaceOfBirth(ListView):
     model = Addproject
     template_name = 'PlaceOfBirth.html'


class commerce(ListView):
     model = Addproject
     template_name = 'commerce.html'

class energy(ListView):
     model = Addproject
     template_name = 'energy.html'

class allProjects(ListView):
     model = Addproject
     template_name = 'allProjects.html'
     context_object_name = "projects"

     def get_queryset(self):
          queryset = Addproject.objects.all()
          search = self.request.GET.get('search')
          if search:
               queryset = Addproject.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
          print(search)
          return queryset



#Проекты
class IT_ru(ListView):
     model = Addproject
     template_name = 'IT_RU.html'

class Production_ru(ListView):
     model = Addproject
     template_name = 'Production_RU.html'

class PlaceOfBirth_ru(ListView):
     model = Addproject
     template_name = 'PlaceOfBirth_RU.html'


class commerce_ru(ListView):
     model = Addproject
     template_name = 'commerce_RU.html'

class energy_ru(ListView):
     model = Addproject
     template_name = 'energy_RU.html'

class allProjects_ru(ListView):
     model = Addproject
     template_name = 'allProjects_RU.html'
     context_object_name = "projects"

     def get_queryset(self):
          queryset = Addproject.objects.all()
          search = self.request.GET.get('search')
          if search:
               queryset = Addproject.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
          print(search)
          return queryset

def applicants_RU(request):
     if request.method == 'POST':
       name = request.POST.get('name')
       number = request.POST.get('number')
       email = request.POST.get('email')
       projectName = request.POST.get('projectName')
       file = request.POST.get('file')
       essences = request.POST.get('essences')
       activities = request.POST.get('activities')
       date = request.POST.get('date')
       adress = request.POST.get('adress')
       actual = request.POST.get('actual')
       sums = request.POST.get('sums')
       payback = request.POST.get('payback')
       yields = request.POST.get('yields')
       documents = request.POST.get('documents')
       availableAssets = request.POST.get('availableAssets')
       ownContribution = request.POST.get('ownContribution')
       comment = request.POST.get('comment')
       ctx_ru = {
           'name' : name,
           'number' : number,
           'email' : email,
           'projectName' : projectName,
           'file' : file,
           'essences' : essences,
           'activities' : activities,
           'date' : date,
           'adress' : adress,
           'actual' : actual,
           'sums' : sums,
           'payback' : payback,
           'yields' : yields,
           'documents' : documents,
           'availableAssets' : availableAssets,
           'ownContribution' : ownContribution,
           'comment' : comment
       }
       message = "\n".join(ctx_ru.values())
       send_mail('Форма заявки', message, settings.EMAIL_HOST_USER, ['investcenter.info@gmail.com'],  fail_silently=True)
     return render(request, 'applicants_RU.html')

def applicants(request):

     if request.method == 'POST':
       name = request.POST.get('name')
       number = request.POST.get('number')
       email = request.POST.get('email')
       projectName = request.POST.get('projectName')
       file = request.POST.get('file')
       essences = request.POST.get('essences')
       activities = request.POST.get('activities')
       date = request.POST.get('date')
       adress = request.POST.get('adress')
       actual = request.POST.get('actual')
       sums = request.POST.get('sums')
       payback = request.POST.get('payback')
       yields = request.POST.get('yields')
       documents = request.POST.get('documents')
       availableAssets = request.POST.get('availableAssets')
       ownContribution = request.POST.get('ownContribution')
       comment = request.POST.get('comment')
       ctx = {
           'name' : name,
           'number' : number,
           'email' : email,
           'projectName' : projectName,
           'file' : file,
           'essences' : essences,
           'activities' : activities,
           'date' : date,
           'adress' : adress,
           'actual' : actual,
           'sums' : sums,
           'payback' : payback,
           'yields' : yields,
           'documents' : documents,
           'availableAssets' : availableAssets,
           'ownContribution' : ownContribution,
           'comment' : comment
       }
       message = "\n".join(ctx.values())
       send_mail('Application form', message, settings.EMAIL_HOST_USER, ['investcenter.info@gmail.com'],  fail_silently=False)
     return render(request, 'applicants.html', {})


def aboutKR(request):
     return render(request, 'aboutKR.html')