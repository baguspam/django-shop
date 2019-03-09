from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'category'
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image =  models.ImageField(upload_to = 'product/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'product'
    def __str__(self):
        return self.name



    