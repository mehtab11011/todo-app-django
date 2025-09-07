from django.db import models

class TaskAddModel(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)  
    description = models.CharField(max_length=500, blank=True, null=True) 
    date = models.DateField(blank=True, null=True)  
    priority = models.CharField(max_length=30, blank=True, null=True) 
