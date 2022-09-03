from django.db import models
from datetime import datetime
from category.models import Category
from django.core.validators import MinValueValidator
from django.urls import reverse 

# Create your models here.

class Product(models.Model):
    tea_name = models.CharField(max_length=100, unique=True)
    tea_type = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    origin = models.CharField(max_length=100)
    color = models.CharField(max_length=50, blank=True)
    aroma = models.CharField(max_length=100, blank=True)
    taste = models.CharField(max_length=100, blank=True)
    tea_nature  = models.CharField(max_length=100, blank=True)
    is_available = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    properties = models.TextField(max_length=300, blank=True)
    weight = models.IntegerField()
    original_price = models.IntegerField()
    discounted_price = models.IntegerField()
    discount_rate = models.IntegerField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1_t = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1_z = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2_t = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2_z = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3_t = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3_z = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4_t = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4_z = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)
    stars = models.IntegerField()
    store = models.IntegerField() 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.tea_name
    
    
class VariationManger(models.Manager):
    
    def packages(self):
        return super(VariationManger, self).filter(variation_category='package', is_active=True)
    
    def sizes(self):
        return super(VariationManger, self).filter(variation_category='size', is_active=True)
    
    
variation_category_choice = {
    ('package', 'package'),
    ('size', 'size'),    
}
    
    
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)
    
    objects = VariationManger()
    
    def __str__(self):
        return self.variation_value


