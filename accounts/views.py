from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here
def signup(req):
    if(req.method == 'POST'):
        if(req.POST['password'] == req.POST['confirmPassword']):
            try:
                User.objects.get(username = req.POST['username'])
                return render(req,'accounts\signup.html',{'error':'Username has been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(req.POST['username'],password=req.POST['password'])
                auth.login(req,user)
                return redirect('home')
        else:
            return render(req,'accounts\signup.html',{'error':'Passowrd did not match'})


    else:    
        #User wants to enter info
        return render(req,'accounts\signup.html')

def login(req):
    if(req.method  == 'POST'):
        user=auth.authenticate(username=req.POST['username'],password=req.POST['password'])
        if(user is not None):
            auth.login(req,user)
            return redirect('home')
        else:
            return render(req,'accounts\login.html',{'error':'Username or password doenot match'})
    else:   
        return render(req,'accounts\login.html')

def logout(req):
    auth.logout(req)
    return redirect('home')