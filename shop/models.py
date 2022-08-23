from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    tea_name = models.CharField(max_length=100, unique=True)
    tea_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50, blank=True)
    aroma = models.TextField(max_length=100, blank=True)
    taste = models.TextField(max_length=100, blank=True)
    tea_nature  = models.TextField(max_length=200, blank=True)
    properties = models.TextField(max_length=200, blank=True)
    package = models.TextField(max_length=200, blank=True)
    size = models.CharField(max_length=50, blank=True)
    is_available = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    price = models.IntegerField()
    store = models.IntegerField()
    image = models.ImageField(upload_to="photos/products")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    stars = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

def __str__(self):
    return self.product_name


