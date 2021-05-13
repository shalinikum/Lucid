from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
# Create your views her
from django.db import models
from practice.models import User
import datetime
from django.contrib import messages
from django.utils import timezone
def login(request):
    if request.method== 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        try:
            user = User.objects.get(user_name= user_name)
            if user.password == password:
                return redirect("/practice")
            else:
                messages.info(request,'invalid credentials')
                return redirect('login')
        except User.DoesNotExist:
            messages.info(request,'invalid user_name')
            return redirect('login')

    

    else:
        return render(request,'login.html')

def register(request):

    if request.method == "POST":
        name =  request.POST["name"]
        email =  request.POST['email']
        gender =  request.POST['gender']
        therapist =  request.POST['therapist']
        phone_number =  request.POST['phone_number']
        password1 =  request.POST['password1']
        password2 =  request.POST['password2']
        age = int(request.POST['age'])
        user_name = request.POST['user_name']


        if password1==password2:
            if User.objects.filter(user_name=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User(name=name,email=email,gender=gender, therapist_id=therapist,phone_number=phone_number, password=password1, age=age, user_name=user_name,joining_date=timezone.now())
                user.save()
                print('user created')
                return redirect('/practice')
                

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')

    else:
        return render(request,'register.html')

