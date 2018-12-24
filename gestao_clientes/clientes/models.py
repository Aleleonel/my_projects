from django.db import models

# Create your models clientes here.

class Documents(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documents, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.description
        

class Sales(models.Model):
    num_sales = models.CharField(max_length=7)
    value_sales = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.DecimalField(max_digits=5, decimal_places=2)
    taxes = models.DecimalField(max_digits=5, decimal_places=2)
    person_sales = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return self.num_sales

