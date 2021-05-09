from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,auth
# Create your views her

def registration(request):

    if request.method == "POST":
        Name =  request.POST['Name']
        email =  request.POST['email']
        Gender =  request.POST['Gender']
        Therapist =  request.POST['Therapist']
        Phone_no =  request.POST['Phone_no']
        password1 =  request.POST['password1']
        password2 =  request.POST['password2']

        user = User.objects.create_user(name=Name,email=email,gender=Gender, therapist=Therapist,phone_number=Phone_no, password=password1, age=age)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request,'register.html')

def register(request):
    return render(request, login.html)