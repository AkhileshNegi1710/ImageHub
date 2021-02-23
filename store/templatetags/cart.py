from django import template

# custom tags and filters will live in a module inside the templatetags directory

register=template.Library()   # decorator

@register.filter(name="is_in_cart")  # this decorator is used to know that it is filter

def is_in_cart(imagename,cart):  #imagename and cart item &  This Function will be called in index.html
    keys=cart.keys()  #keys to check id

    for id in keys:  #This loop to check whether image in cart or not
     try:
         a=int(id)
     except ValueError:
        print("Value Error")
     if a==imagename.id:
            return True
    return False



@register.filter(name="cart_quantity")   #second decorator

def cart_quantity(imagename,cart):  # this function will be called in index.html
    keys=cart.keys() #keys are the id of image dictionary

    for id in keys:   #This loop to print cart id in index.html
     try:
       a = int(id)
     except ValueError:
        print("ValueError")           # print(type(id), type(image.id))

     if a==imagename.id:
            return cart.get(id)
    return 0

@register.filter(name="price_total")   #third decorator

def price_total(imagename,cart):  # this function will be called in index.html
    return imagename.price * cart_quantity(imagename,cart)

@register.filter(name="total_cart_price")
def total_cart_price(imagename,cart):
    sum=0
    for p in imagename:
        sum+=price_total(p,cart)
    return sum



