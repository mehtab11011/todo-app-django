# from django.db import models
# class taskaddmodel(models.Model):
#     name=models.CharField(max_length=20)
#     Description=models.CharField(max_length=500)
#     date=models.CharField(max_length=30)
#     Priority=models.CharField(max_length=30)

# # Create your models here.
from django.db import models

class TaskAddModel(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)  # Required field
    description = models.CharField(max_length=500, blank=True, null=True)  # Optional
    date = models.CharField(max_length=30, blank=True, null=True)  # Optional
    priority = models.CharField(max_length=30, blank=True, null=True)  # Optional
