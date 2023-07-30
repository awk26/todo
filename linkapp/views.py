from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")


def register(request):
    if request.method=="POST":
        obj=UserCreationForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={"form":UserCreationForm}
        return render(request,'forms.html ',d)
    

def loginn(request):
    if request.method=='POST':
        uname=request.POST.get("uname")
        pswd=request.POST.get("pswd")
        user=authenticate(request,username=uname,password=pswd)
        if user is not None:
            request.session["id"]=user.id
            print(request.session.get("id"))
            login(request,user)
            return redirect("/linkedin-dashboard")
        else:
            d={'form':LoginForm}
            return render(request,'forms.html',d)

    else:
        d={'form':LoginForm}
        return render(request,'forms.html',d)
    
def dash(request):
       obj1=Profile.objects.all()
       if request.method=="POST":
        obj=ProfileForm(request.POST)
        obj.save()
        
        
        return redirect("/linkedin-dashboard")
       else:
        d={"form":ProfileForm,"data":obj1}
        return render(request,'dashboard.html ',d)
       
def details(request):
    obj=Profile.objects.all()
    d={"data":obj}
    return render(request,"sample.html",d)

def delete(request,pk):
    obj=Profile.objects.get(id=pk)
    obj.delete()
    return redirect("/linkedin-dashboard")

def edits(request,pk):
  data=Profile.objects.get(id=pk)
  if request.method=='POST':
    obj=ProfileForm(request.POST,instance=data)
    obj.save()
    return redirect("/linkedin-dashboard")
  else:
    d={'form':ProfileForm(instance=data)}
    return render(request,'dashboard.html',d)
    

def logoutt(request):
    logout(request)
    return redirect("/")    