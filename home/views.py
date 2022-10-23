from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request,'auth/home.html')


def signup(request):

    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request,"Your account has been successfully created.")

        return redirect('signin')

    return render(request,'auth/signup.html')

def signin(request):

    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname= user.first_name
            return render(request,"index.html",{'fname':fname})

        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')


    return render(request,'auth/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

def index(request):
    return render(request, 'index.html')

def tourism(request):
    return render(request, 'tourism.html')

def student(request):
    return render(request, 'student.html')

def jobs(request):
    return render(request, 'jobs.html')

def business(request):
    return render(request, 'business.html')

def map(request):
    return render(request, 'map.html')

def help(request):
    return render(request, 'help.html')

def news(request):
    return render(request,'news.html')