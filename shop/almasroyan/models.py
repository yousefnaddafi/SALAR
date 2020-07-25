import uuid
from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75,help_text='the main field of a product')
    
    def __str__(self):
        return self.title



class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=75, help_text="the brand of the company")

    def __str__(self):
        return self.title



class Product(models.Model):
    id =  models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,help_text="enter the product name")
    description = models.TextField(max_length= 1000,)
    enable = models.BooleanField(default=True,)
    price = models.CharField(max_length=15)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to= 'static/img/')
    def __str__(self):
        return self.name


class Product_Instance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for this product')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    Due_back = models.DateField(null= True, blank= True)

    def __str__(self):
        return '{0} ({1})'.format(self.id , self.product)


