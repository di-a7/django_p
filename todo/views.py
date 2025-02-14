from django.shortcuts import render, HttpResponse

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