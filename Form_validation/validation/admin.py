from django.contrib import admin
from .models import Model

# Register your models here.

# admin.site.register(Model)

class studentAdmin(admin.ModelAdmin):
    list_display=('id','Name','Age','Email','Place')

admin.site.register(Model, studentAdmin)