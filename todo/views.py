from django.shortcuts import render, HttpResponse,redirect
from .models import Todolist
# Create your views here.
def home(request):
   return render(request,'home.html')

# def index(request):
#    return HttpResponse("Hello World")

def contact(request):
   persons = [
      {
      "name":"ram",
      "age":35
   },
      {
      "name":"testing",
      "age":15
   },
      {
      "name":"tester",
      "age":60
   },
      {
      "name":"shyam",
      "age":25
   },
      {
      "name":"test",
      "age":5
   }
      ]
   context = {
      "name":"Contact Page",
      "persons":persons
   }
   return render(request,'home.html',context)
   # return HttpResponse("Contanct page")
   
# contact, about ...

def task(request):
   tasks = Todolist.objects.all()
   total = tasks.count()
   completed = Todolist.objects.filter(is_completed = True).count()
   notcompleted = Todolist.objects.filter(is_completed = False).count()
   context = {
      "tasks":tasks,
      "total":total,
      "completed":completed,
      "notcompleted":notcompleted
   }
   return render(request, 'task.html',context)

def task_create(request):
   if request.method == "POST":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      if titles == '' or descriptions == '' :
         context = {
            'error':"Both fields required."
         }
         return render(request, 'create.html',context)
      Todolist.objects.create(title = titles, description = descriptions)
      return redirect('/task')
   
   return render(request, 'create.html')

def mark_complete(request,pk):
   task = Todolist.objects.get(pk = pk)
   task.is_completed = True
   task.save()
   return redirect("/task")

def edit_task(request,pk):
   task = Todolist.objects.get(pk = pk)
   context = {"task":task}
   if request.method == "POST":
      titles = request.POST.get('title')
      descriptions = request.POST.get('description')
      if titles == '' or descriptions == '' :
         context = {
            'error':"Both fields required."
         }
         return render(request, 'create.html',context)
      task.title = titles
      task.description = descriptions
      task.save()
      return redirect("/task")
   return render(request, 'edit.html',context)