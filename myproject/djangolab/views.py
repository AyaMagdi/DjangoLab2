from django.shortcuts import render
from .models import Myusers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def open_base(request):
    return render(request, "base.html")


def open_login(request):
    logout(request)
    return render(request, "login.html")

def open_profile(request):
    return render(request, "profile.html")

def insert(request):
    name= request.POST['username']
    password= request.POST['password']

    Myusers.objects.create(name=name, password=password)
    User.objects.create_user(username=name, password=password, is_staff=True)
    return render(request, "login.html")

def open_register(request):
    return render(request, "register.html")

def handle_login(request):
    users= Myusers.objects.all()
    name = request.GET['username']
    password = request.GET['password']
    for user in users:
        if user.name==name and user.password== password:
            request.session['username'] = name

            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
            return render(request, "profile.html")
        else:
            pass
    erorr={'erorr': "Wrong name or password"}

    return render(request, "login.html",erorr)


def list_users(request):
    all_users = Myusers.objects.all()
    users= {'users': all_users}
    return render(request, "all_users.html", users)


def delete(request, id):
    Myusers.objects.filter(id=id).delete()
    all_users = Myusers.objects.all()
    users = {'users': all_users}
    return render(request, "all_users.html", users)

def open_update_page(request):
    return render(request, "update.html")

def update_db(request):
    name = request.GET['username']
    new_name = request.GET['new_username']
    Myusers.objects.filter(name=name).update(name=new_name)

    all_users = Myusers.objects.all()
    users = {'users': all_users}
    return render(request, "all_users.html", users)

def search(request):
    name= request.GET['username']
    users_found= Myusers.objects.filter(name=name)
    users = {'users': users_found}
    return render(request, "all_users.html", users)








