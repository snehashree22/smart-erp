from django.shortcuts import render, redirect

from .models import Product, Employee, Customer, Order

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

import openpyxl
from reportlab.pdfgen import canvas

def register_page(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists'
            )

            return redirect('/register/')

        User.objects.create_user(

            username=username,

            email=email,

            password=password

        )

        messages.success(
            request,
            'Account Created Successfully'
        )

        return redirect('/login/')

    return render(
        request,
        'register.html'
    )

def login_page(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user:

            login(request, user)

            return redirect('/')

    return render(
        request,
        'login.html'
    )


def logout_page(request):

    logout(request)

    return redirect('/login/')


@login_required(login_url='/login/')
def dashboard(request):

    total_products = Product.objects.count()

    total_employees = Employee.objects.count()

    total_customers = Customer.objects.count()

    total_orders = Order.objects.count()

    return render(

        request,

        'dashboard.html',

        {

            'total_products': total_products,

            'total_employees': total_employees,

            'total_customers': total_customers,

            'total_orders': total_orders

        }

    )


@login_required(login_url='/login/')
def products(request):

    if request.method == 'POST':

        Product.objects.create(

            name=request.POST['name'],
            quantity=request.POST['quantity'],
            price=request.POST['price'],
            category=request.POST['category']

        )

        messages.success(
            request,
            'Product Added Successfully'
        )

        return redirect('/products/')

    search = request.GET.get('search')

    if search:

        products = Product.objects.filter(
            name__icontains=search
        )

    else:

        products = Product.objects.all()

    return render(

        request,

        'products.html',

        {
            'products': products
        }

    )


@login_required(login_url='/login/')
def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    messages.success(
        request,
        'Product Deleted Successfully'
    )

    return redirect('/products/')


@login_required(login_url='/login/')
def update_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':

        product.name = request.POST['name']

        product.quantity = request.POST['quantity']

        product.price = request.POST['price']

        product.category = request.POST['category']

        product.save()

        messages.success(
            request,
            'Product Updated Successfully'
        )

        return redirect('/products/')

    return render(

        request,

        'update_product.html',

        {
            'product': product
        }

    )
    
@login_required(login_url='/login/')
def export_products_excel(request):

    workbook = openpyxl.Workbook()

    sheet = workbook.active

    sheet.title = 'Products'

    headers = [

        'ID',
        'Name',
        'Quantity',
        'Price',
        'Category'

    ]

    sheet.append(headers)

    products = Product.objects.all()

    for product in products:

        sheet.append([

            product.id,
            product.name,
            product.quantity,
            product.price,
            product.category

        ])

    response = HttpResponse(

        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    )

    response['Content-Disposition'] = 'attachment; filename=products.xlsx'

    workbook.save(response)

    return response

@login_required(login_url='/login/')
def export_products_pdf(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = 'attachment; filename=products.pdf'

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 16)

    p.drawString(200, 800, "Products Report")

    y = 750

    products = Product.objects.all()

    for product in products:

        text = f"{product.id} | {product.name} | {product.quantity} | ₹{product.price} | {product.category}"

        p.drawString(50, y, text)

        y -= 30

    p.save()

    return response


@login_required(login_url='/login/')
def employees(request):

    if request.method == 'POST':

        Employee.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            salary=request.POST['salary']

        )

        messages.success(
            request,
            'Employee Added Successfully'
        )

        return redirect('/employees/')

    search = request.GET.get('search')

    if search:

        employees = Employee.objects.filter(
            name__icontains=search
        )

    else:

        employees = Employee.objects.all()

    return render(

        request,

        'employees.html',

        {
            'employees': employees
        }

    )


@login_required(login_url='/login/')
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    messages.success(
        request,
        'Employee Deleted Successfully'
    )

    return redirect('/employees/')


@login_required(login_url='/login/')
def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        employee.name = request.POST['name']

        employee.email = request.POST['email']

        employee.phone = request.POST['phone']

        employee.department = request.POST['department']

        employee.salary = request.POST['salary']

        employee.save()

        messages.success(
            request,
            'Employee Updated Successfully'
        )

        return redirect('/employees/')

    return render(

        request,

        'update_employee.html',

        {
            'employee': employee
        }

    )


@login_required(login_url='/login/')
def customers(request):

    if request.method == 'POST':

        Customer.objects.create(

            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            city=request.POST['city']

        )

        messages.success(
            request,
            'Customer Added Successfully'
        )

        return redirect('/customers/')

    search = request.GET.get('search')

    if search:

        customers = Customer.objects.filter(
            name__icontains=search
        )

    else:

        customers = Customer.objects.all()

    return render(

        request,

        'customers.html',

        {
            'customers': customers
        }

    )


@login_required(login_url='/login/')
def delete_customer(request, id):

    customer = Customer.objects.get(id=id)

    customer.delete()

    messages.success(
        request,
        'Customer Deleted Successfully'
    )

    return redirect('/customers/')


@login_required(login_url='/login/')
def update_customer(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == 'POST':

        customer.name = request.POST['name']

        customer.email = request.POST['email']

        customer.phone = request.POST['phone']

        customer.city = request.POST['city']

        customer.save()

        messages.success(
            request,
            'Customer Updated Successfully'
        )

        return redirect('/customers/')

    return render(

        request,

        'update_customer.html',

        {
            'customer': customer
        }

    )


@login_required(login_url='/login/')
def orders(request):

    if request.method == 'POST':

        product = Product.objects.get(
            id=request.POST['product']
        )

        customer = Customer.objects.get(
            id=request.POST['customer']
        )

        quantity = int(request.POST['quantity'])

        total_price = product.price * quantity

        Order.objects.create(

            product=product,

            customer=customer,

            quantity=quantity,

            total_price=total_price

        )

        messages.success(
            request,
            'Order Created Successfully'
        )

        return redirect('/orders/')

    products = Product.objects.all()

    customers = Customer.objects.all()

    orders = Order.objects.all()

    return render(

        request,

        'orders.html',

        {
            'products': products,
            'customers': customers,
            'orders': orders
        }

    )


@login_required(login_url='/login/')
def delete_order(request, id):

    order = Order.objects.get(id=id)

    order.delete()

    messages.success(
        request,
        'Order Deleted Successfully'
    )

    return redirect('/orders/')


@login_required(login_url='/login/')
def update_order(request, id):

    order = Order.objects.get(id=id)

    if request.method == 'POST':

        product = Product.objects.get(
            id=request.POST['product']
        )

        customer = Customer.objects.get(
            id=request.POST['customer']
        )

        quantity = int(request.POST['quantity'])

        total_price = product.price * quantity

        order.product = product

        order.customer = customer

        order.quantity = quantity

        order.total_price = total_price

        order.save()

        messages.success(
            request,
            'Order Updated Successfully'
        )

        return redirect('/orders/')

    products = Product.objects.all()

    customers = Customer.objects.all()

    return render(

        request,

        'update_order.html',

        {
            'order': order,
            'products': products,
            'customers': customers
        }

    )