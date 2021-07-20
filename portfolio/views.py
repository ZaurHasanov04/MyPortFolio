from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.core.management import settings
from .forms import *
# Create your views here.

def show(request):
    about=About.objects.all()
    portfolio=Portfolio.objects.all()
    skill=Skill.objects.all()
    form=ContactForm(request.GET)
    if form.is_valid():
        print('True')
        obj=Contact.objects.create(
            full_name=request.GET['full_name'],
            email=request.GET['email'],
            subject=request.GET['subject'],
            text=request.GET['text']
        )
        # messages=str(request.GET['email']) +  " " +"size mail mesaj yazib"
        # send_mail(request.GET['subject'], messages, settings.EMAIL_HOST_USER , ['zaurqwerty@gmail.com'], fail_silently=False)
        obj.save
    
    context={
        'about':about,
        'portfolio':portfolio,
        'skill':skill,
        'form':form
    }

    return render(request, 'index.html', context)



# def sendemail(request):
    
#     form=ContactForm()

#     if form.is_valid():
#         obj=Contact.objects.create(
#             full_name=request.GET['full_name'],
#             email=request.GET['email'],
#             subject=request.GET['subject'],
#             text=request.GET['text']
#         )

#         obj.save

#     messages=str(request.GET['email']) + "size mail mesaj yazib"

#     send_mail(request.GET['subject'], messages, settings.EMAIL_HOST_USER , ['zaurqwerty@gmail.com'], fail_silently=False)

#     return redirect('show')