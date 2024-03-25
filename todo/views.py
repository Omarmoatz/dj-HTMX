from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Todo


def list_todo(request):
    todo = Todo.objects.all()
    context = {'todo':todo}
    return render(request , 'todo.html', context) 