from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import stock

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(stock, MyModelAdmin)