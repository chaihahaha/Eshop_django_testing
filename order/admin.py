from django.contrib import admin

# Register your models here.
from order.models import Product,Ptype
admin.site.register(Product)
admin.site.register(Ptype)