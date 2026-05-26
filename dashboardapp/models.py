from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=100)

    quantity = models.IntegerField()

    price = models.IntegerField()

    category = models.CharField(max_length=100)

    def __str__(self):

        return self.name
    
class Employee(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    department = models.CharField(max_length=100)

    salary = models.IntegerField()

    def __str__(self):

        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    city = models.CharField(max_length=100)

    def __str__(self):

        return self.name
    
class Order(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField()

    total_price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.id)