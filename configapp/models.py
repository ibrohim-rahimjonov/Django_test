from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='category_pictures/', blank=True, null=True)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50, blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_per_unit = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    reorder_level = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%M/%d')
    discontinued = models.BooleanField(default=False)


    def __str__(self):
        return self.product_name