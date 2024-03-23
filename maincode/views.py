from django.shortcuts import render,redirect
from .models import tododata

# Create your views here.

def todo_list(request):
    tododa = tododata.objects.all().order_by('-id')
    return render(request,'home.html', {'tododata':tododa})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tododata.objects.create(title=title,description=description)

    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo_item = tododata.objects.get(id=todo_id)  # Rename variable to avoid collision
    todo_item.completed = True
    todo_item.save()

    return redirect('todo_list')

# def delete_todo(request,todo_id):
#     todo = tododata.objects.get(id=todo_id)  # Rename variable to avoid collision
#     todo.delete()
#     todo.save()

#     return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = tododata.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
