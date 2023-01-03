from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from app1.forms import Signupform
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Has Been Created')
    else:
            form = Signupform()
    return render(request,'app1/signup.html',{'form':form})

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    messages.success(request,'Login successfullly.....!')
                    res = render(request,'app1/dashboard.html',{'msg':'Welcome to DashBoard'})
                    res.set_cookie('username',username)
                    res.set_cookie('password',password)
                    return res    
        else:
            form = AuthenticationForm()
        return render(request,'app1/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/app1/dashboard')

def set(request):
    res = render(request,'app1/set.html')
    res.set_cookie('name','Irfan')
    return res

def get(request):
    name = request.COOKIES.get('name')
    return render(request,'app1/get.html',{'name':name})

def delete(request):
    res = render(request,'app1/delete.html')
    res.delete_cookie('name')
    return res