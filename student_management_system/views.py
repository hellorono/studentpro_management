from django.shortcuts import render,redirect
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

def BASE(request):
    return render (request,'base.html')

def Index(request):
    return render (request,'index.html')

def loginuser(request):
    return render (request,'login.html')

def dologin(request):
    if request.method == "POST":
        user = EmailBackend.authenticate(request,
                                         username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse('This is hod panel')
            elif user_type == '2':
                return HttpResponse('This is staff panel')
            elif user_type == '3':
                return HttpResponse('This is student panel')
            else:
                messages.error(request,"invalid credentials")
                return redirect ('login')
            
        else:
            messages.error(request,"email and password are incorrect ")
            return redirect ('login')
    


