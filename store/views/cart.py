from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.views import View
from store.models.productimagemodel import Product

class Cart(View):
    def get(self,request):
        ids =list(request.session.get("cart").keys())  # in templates we can access through request.session.cart
        images=Product.get_images_by_id(ids)
        print(images)
        return render(request, "cart.html",{"cart":images})

