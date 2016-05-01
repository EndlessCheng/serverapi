from django.contrib import admin

from models import *

# Register your models here.

admin.site.register([Canteen, Window, Category, Product, HeatProduct, WindowComment, Operator])