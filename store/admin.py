from django.contrib import admin
from .models.productimagemodel import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


# display data in table form in sqllite
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','categoryid']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Product file here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order)