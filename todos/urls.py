from django.contrib import admin
from django.urls import path, include

from todos.views import (
    TodoListListView,
)

urlpatterns = [
    path("", TodoListListView.as_view(), name="todo_list_list"),
]
