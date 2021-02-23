from django.db import models
from .category import Category


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    categoryid=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='productimages/upload/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_images_by_id(ids):
        return Product.objects.filter(id__in=ids)  #access list using __in

#  decorator
    @staticmethod
    def get_all_products():
      return Product.objects.all()

    # filter uses id
    @staticmethod
    def get_all_products_by_cat_id(cat_id):
      if cat_id:
        return Product.objects.filter(categoryid=cat_id)
      else:
        return Product.objects.all()
