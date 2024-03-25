from django.urls import path

from .models import Todo
from . import views


    #   todo/
urlpatterns = [
    path('', views.list_todo ),
]

