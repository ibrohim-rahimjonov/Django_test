from django.contrib import admin
from configapp.models import Product, Supplier, Category


# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_name','category','unit_price')
    list_display_links = ['product_id','product_name']
    search_fields = ['product_id']

class NewSupplier(admin.ModelAdmin):
    list_display = ('supplier_id','company_name','contact_name','city','country')
    list_display_links = ['supplier_id','company_name','contact_name']
    search_fields = ['supplier_id']




admin.site.register(Product,NewAdmin)
admin.site.register(Supplier,NewSupplier)
admin.site.register(Category)

