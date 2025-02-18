from django.db import models
# Create your models here.
class Todolist(models.Model):
   title = models.CharField(max_length=30)
   description = models.TextField()
   is_completed = models.BooleanField(default = False)