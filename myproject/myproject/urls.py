"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangolab.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', open_base, name='base'),
    path('login/', open_login, name='login'),
    path('/', open_login, name='login'),
    path('open_profile/', open_profile, name='open_profile'),
    path('insert/', insert, name='insert'),
    path('register/', open_register, name='register'),
    path('handle_login/', handle_login, name='handle_login'),
    path('list/', list_users, name='list'),
    path('delete/<id>', delete, name='delete'),
    path('open_update_page', open_update_page, name='open_update_page'),
    path('update_db', update_db, name='update_db'),
    path('search', search, name='search'),
    path('insert_forms', insert_forms, name='insert_forms'),
    path('insert_model_forms', insert_model_forms, name='insert_model_forms'),
    path('update_forms', update_forms, name='update_forms'),
    path('User_List', User_List.as_view(), name='User_List'),
]


