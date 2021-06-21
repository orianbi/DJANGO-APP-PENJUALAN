from django.contrib import admin
from .models import *
# Register your models here.

class CustemerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email',]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_id','date_created','status',]

admin.site.register(Custemer, CustemerAdmin)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag)