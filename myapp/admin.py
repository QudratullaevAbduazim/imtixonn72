from django.contrib import admin

# Register your models here.
from .models import Category, Phones
admin.site.register(Category)
admin.site.register(Phones)