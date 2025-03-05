from django.contrib import admin
from addtask.models import TaskAddModel
class addtask_model(admin.ModelAdmin):
    list_display=("name","description","date","priority")
admin.site.register(TaskAddModel,addtask_model)
# Register your models here.
