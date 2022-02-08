from django.shortcuts import render
from .models import Myusers, Intake
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import Insert_forms, Insert_model_forms, Update_forms
from django.views.generic import ListView


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

    intake_obj = Intake.objects.get(id=request.POST['ID'])
    Myusers.objects.create(name=request.POST['username'], password=request.POST['password'], intake_id=intake_obj)
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

#############################################################################

def insert_forms(request):
    my_form= {}
    form = Insert_forms()
    if request.method == 'GET':
        my_form['form'] = form
        return render(request, 'insert_forms.html',    my_form)
    else:
        intake_obj = Intake.objects.get(id=request.POST['intake_id'])
        Myusers.objects.create(name=request.POST['name'], password=request.POST['password'], intake_id=intake_obj)
        my_users = Myusers.objects.all()
        users = {'users': my_users}
        return render(request, "all_users.html", users)


def insert_model_forms(request):
    my_form= {}
    form = Insert_model_forms()
    if request.method == 'GET':
        my_form['form'] = form
        return render(request, 'insert_model_forms.html',    my_form)
    else:
        form_data = Insert_model_forms(request.POST)
        form_data.save()
        my_users = Myusers.objects.all()
        users = {'users': my_users}
        return render(request, "all_users.html", users)

def update_forms(request):
    my_form= {}
    form = Update_forms()
    if request.method == 'GET':
        my_form['form'] = form
        return render(request, 'update_form.html',    my_form)
    else:

        name = request.POST['name']
        new_name = request.POST['new_name']
        Myusers.objects.filter(name=name).update(name=new_name)

        all_users = Myusers.objects.all()
        users = {'users': all_users}
        return render(request, "all_users.html", users)

class User_List(ListView):
    model = Myusers
