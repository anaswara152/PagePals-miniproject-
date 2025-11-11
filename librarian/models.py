from django.db import models

# Create your models here.
class library(models.Model):
    username=models.CharField(max_length=13)
    password=models.CharField(max_length=13)

    def __str__(self):
        return self.username
    
class category(models.Model):
    name=models.CharField(max_length=12)
    def __str__(self):
        return self.name
class book(models.Model):
    name=models.CharField(max_length=12)
    author=models.CharField(max_length=15)
    coverphoto=models.FileField(upload_to='meadia')
    numberof_copies=models.IntegerField()
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name