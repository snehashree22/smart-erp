from django.contrib import admin

from .models import Product, Employee, Customer

admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Customer)