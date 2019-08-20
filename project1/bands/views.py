from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Band, Member

def home(request):
    return render(request, 'home.html')


# Create your views here.
