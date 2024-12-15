from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from .models import Restaurants,TrainingData,MoodData
import math
import numpy as np

class HomePage(TemplateView):
    template_name = "index.html"

def resultpage(request):
    form=forms.Feedback()
    if request.method=='POST':
        form=forms.Feedback(request.POST)
        if form.is_valid():
            a=form.cleaned_data['Restaurant']
            b=form.cleaned_data['Food']
            c=form.cleaned_data['Mood']
            d=form.cleaned_data['Rating']
            print(a)
            print(b)
            print(c)
            print(d)
            v=Restaurants.objects.filter(name=a).values_list()
            print(v[0])
            f=v[0][4]
            g=v[0][6]
            nv= ((f*g)+d)/(g+1)
            Restaurants.objects.filter(name=a).update(rating=nv)
            Restaurants.objects.filter(name=a).update(count=g+1)
        return render(request,'test.html',{'form':form})
    return render(request,'foody_1/result.html',{'form':form})

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "foody_1/signup.html"