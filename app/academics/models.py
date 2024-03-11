from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    ident_number=models.CharField(max_length=12,blank=True)
    created_at=models.DateTimeField(default=datetime.datetime.now())    
    updated_at=models.DateTimeField(default=datetime.datetime.now())
    delete_at=models.DateTimeField(null=True,blank=True)