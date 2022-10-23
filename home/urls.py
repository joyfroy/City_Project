from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('signup',views.signup,name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path("index",views.index,name='index'),
    path("business",views.business,name='business'),
    path("help",views.help,name='help'),
    path("map",views.map,name='map'),
    path("jobs",views.jobs,name='jobs'),
    path("student",views.student,name='student'),
    path("tourism",views.tourism,name='tourism'),
    path("news",views.news,name='news'),
]
