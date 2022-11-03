



from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Linklist(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, null = True)
    link = models.CharField(max_length=200)
    
   
    def __str__(self):
        return self.title
