from django.contrib import admin
from registration.models import register
class register_model(admin.ModelAdmin):
    list_display=("username","email","password")
admin.site.register(register,register_model)

# Register your models here.
