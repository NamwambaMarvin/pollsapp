# Register your models here.
#registering the polls app here
#including admin interface
from django.contrib import admin
#importing the Question class
from .models import *
#register
admin.site.register(Question)
admin.site.register(Choice)