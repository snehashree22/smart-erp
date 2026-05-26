from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),
    
    path(
    'products/',
    views.products,
    name='products'
),
    
    path(
    'employees/',
    views.employees,
    name='employees'
),
    
    path(
    'customers/',
    views.customers,
    name='customers'
),
    
    path(
    'orders/',
    views.orders,
    name='orders'
),
    
    path(
    'delete-product/<int:id>/',
    views.delete_product,
    name='delete_product'
),
    path(
    'update-product/<int:id>/',
    views.update_product,
    name='update_product'
),

path(
    'delete-employee/<int:id>/',
    views.delete_employee,
    name='delete_employee'
),
path(
    'update-employee/<int:id>/',
    views.update_employee,
    name='update_employee'
),
path(
    'delete-customer/<int:id>/',
    views.delete_customer,
    name='delete_customer'
),
path(
    'update-customer/<int:id>/',
    views.update_customer,
    name='update_customer'
),
path(
    'delete-order/<int:id>/',
    views.delete_order,
    name='delete_order'
),

path(
    'update-order/<int:id>/',
    views.update_order,
    name='update_order'
),
path(
    'login/',
    views.login_page,
    name='login'
),

path(
    'logout/',
    views.logout_page,
    name='logout'
),
path(
    'export-products-pdf/',
    views.export_products_pdf,
    name='export_products_pdf'
),
path(
    'register/',
    views.register_page,
    name='register'
),
]