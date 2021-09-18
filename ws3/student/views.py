from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from .models import Application, Student, Scholarship
from django.views.generic import UpdateView

# Create your views here.
def college(request):
    scholarships = Scholarship.objects.all()
    return render(request, "student\\home.html", {'scholarship':scholarships})

def scholarship(request, myid):
    details = Scholarship.objects.filter(id=myid).first()
    
    return render(request, "student\\scholarship.html", {'details':details})


def application_form(request,id):
    if not request.user.is_authenticated:
        return redirect("/login")
    
   
    student=Student(user=request.user,branch='Ece')
    
    scholarship=Scholarship.objects.get(id=id)
    
    application=Application(user=student,scholarship=scholarship)
    
    return render(request,"student\\application_form.html")
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            email = request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('/register')
            
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request, 'student\\login.html')   
    return render(request, "student\\register.html")

def loggedin(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials")
            return render(request, 'student\\home.html')   
    return render(request, "student\\login.html")

def loggedout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')