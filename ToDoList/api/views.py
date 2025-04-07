from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

def index(request, id):
    todo_list = ToDoList.objects.get(id=id)
    return render(request, "api/list.html", {"todo_list": todo_list})
    
def home(request):
    return render(request, "api/home.html", {})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todo_list = ToDoList(name=name) 
            todo_list.save()
        return HttpResponseRedirect("/%i" % todo_list.id)
    else:    
        form = CreateNewList()
    return render(request, "api/create.html", {"form":form})