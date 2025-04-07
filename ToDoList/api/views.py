from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request, name):
    todo_list = ToDoList.objects.get(name=name)
    item = todo_list.item_set.get(id=1)
    return HttpResponse("%s</br>%s" % (todo_list.name, item.text))
