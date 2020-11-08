from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Company(models.Model):
   CompanyName = models.CharField(max_length = 50,primary_key=True)
   CompanyTitle = models.CharField(max_length = 50)
class registration(models.Model):
   users=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True)

   class Meta:
      unique_together = (("users", "company"),)