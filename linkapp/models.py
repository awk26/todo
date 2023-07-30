from django.db import models

from django.db import models
from datetime import datetime
from django import forms

class LoginForm(forms.Form):
    uname=forms.CharField(max_length=30,label="username")
    pswd=forms.CharField(max_length=30,label="password")

class Profile(models.Model):
    choice=(("Complete","complete"),
            ("Pending","pending"))
    title=models.CharField(max_length=300,default='')
    date=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=choice,default=True)

    def __str__(self):
        return self.title


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="__all__"
    
        