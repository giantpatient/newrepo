from django.db import models

# Create your models here.

class file(models.Model):
    name=models.CharField(max_length=100)
    subject=models.TextField()
    url=models.TextField()
    def __str__(self):
         return self.name
    
    

class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    issue=models.TextField()
    time=models.TimeField(auto_now=True)
    def __str__(self):
         return self.name