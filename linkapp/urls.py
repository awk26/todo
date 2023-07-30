from django.urls import path
from .import views as v
urlpatterns = [
    path("",v.index,name="index"),
    path("reg",v.register,name="register"),
    path("login",v.loginn,name="login"),
    path("logout",v.logoutt,name="logout"),
    path("dashboard",v.dash,name="dashb"),
    path("details",v.details,name="details1"),
    path("deletes/<int:pk>",v.delete,name="delete1"),
    path("edit/<int:pk>",v.edits,name="edit1"),
    
]