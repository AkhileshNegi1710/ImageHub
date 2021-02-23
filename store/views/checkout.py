from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from store.models.productimagemodel import Product
from store.models.orders import Order


class Checkout(View):

    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer_id")
        cart = request.session.get("cart")
        products = Product.get_images_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer), productname=product, price=product.price,
                          quantity=cart.get(str(product.id)), phone=phone, address=address)
            # print(order.placeOrder())
            order.save()
        request.session["cart"] = {}
        return redirect("cart")
