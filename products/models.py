from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class AvailableColors(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name_plural = "Available Colors"

    def __str__(self):
        return self.name

class AvailableSizes(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Available Sizes"

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image', default="", null=True, blank=True)
    is_thumbnail = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Product Image Upload"

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255, null=True)
    long_description = models.TextField(max_length=380, null=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)  
    is_at_discount = models.BooleanField(default=False)
    discounted_percent = models.IntegerField(null=True, default=0, blank=True)
    slug = models.SlugField(unique=True, default=None, blank=True, null=True)
    available_sizes = models.ManyToManyField('AvailableSizes')
    available_colors = models.ManyToManyField('AvailableColors') 
    category = models.ManyToManyField('Category')

    class Meta:
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
