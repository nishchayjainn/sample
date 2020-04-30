from django.db import models
import uuid
from django.contrib.auth.models import User

class AccountModel(models.Model):
    id= models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.OnetoOneField(User,on_delete=models.CASCADE)
    domain =models.CharField(max_length=50)
    registeration_number =models.CharField(max_length=50)
    phone =models.CharField(max_length=20)
    test = models.BooleanField(default=False)