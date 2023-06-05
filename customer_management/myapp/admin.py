from django.contrib import admin
from .models import Air_craft,Job,PartFullForm,PartNumber

# Register your models here.
admin.site.register(Air_craft)
admin.site.register(Job)
admin.site.register(PartFullForm)
admin.site.register(PartNumber)