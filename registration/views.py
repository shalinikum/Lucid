from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
# Create your views her
from django.db import models
from practice.models import User
import datetime
from django.utils import timezone
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
    
        user = User(name=name,email=email,gender=gender, therapist_id=therapist,phone_number=phone_number, password=password1, age=age, user_name=user_name,joining_date=timezone.now())
        user.save();
        print('user created')
        return redirect('/practice')
    else:
        return render(request,'register.html')

