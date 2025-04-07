from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request, id):
    todo_list = ToDoList.objects.get(id=id)
    return render(request, "api/list.html", {"todo_list": todo_list})
    
def home(request):
    return render(request, "api/home.html", {})

def create(request):
    return render(request, "api/create.html", {})
