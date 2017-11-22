from django.contrib import admin
from shop import models


# Register your models here.
class SonAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'id']

admin.site.register(models.Product, SonAdmin)
