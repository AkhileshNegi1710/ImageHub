from django import template

# custom tags and filters will live in a module inside the templatetags directory

register=template.Library()   # decorator

@register.filter(name="currency")  # this decorator is used to know that it is filter
def currency(number):
    return "₹ "+str(number)



@register.filter(name="multiply")  # this decorator is used to know that it is filter
def multiply(number,number1):
    return number * number1


