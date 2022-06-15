from typing import List
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from todos.models import TodoItem, TodoList
from django.shortcuts import render

# Create your views here.


class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_lists/list.html"
