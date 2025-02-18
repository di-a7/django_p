from django.urls import path
from .views import *

urlpatterns = [
   path('home/',home),
   path('contact/',contact),
   path('task/',task),
   path('task/create/',task_create),
   path('task/<pk>/',mark_complete),
   path('task/<pk>/edit',edit_task),
]
