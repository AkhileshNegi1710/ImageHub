from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.productimagemodel import Product
from store.models.category import Category
from django.views import View



# print(make_password("1224"))
# print(check_password("1224","pbkdf2_sha256$216000$hWgfycHFQVAt$QK2VCIqWc55ogYL3bS8Iq45AKgILaigMBYjmX5XSNSU="))

class Index(View):

    def post(self,request):
        imageid=request.POST.get("imageid")# access imageid name from index.html
        cart =request.session.get('cart') #if session has cart
        remove=request.POST.get('remove')#access remove name from index.html


        if cart:          # if session has cart dictionary
            # get is used for particular data and value will be starting point
            quantity=cart.get(imageid) # added imageid in 1 ,2,3,4 to quantity using get

            if quantity:
                if remove:
                    if quantity<=1:
                        # pop for removing item from dictionary so that no 0 will not shown in add to cart
                        cart.pop(imageid)
                    else:
                        cart[imageid]=quantity-1
                else:
                    cart[imageid]=quantity+1
            else:
                cart[imageid] = 1 # like image[4]=1
        else:

            cart={} # no dict in cart
            cart[imageid] = 1

        request.session["cart"]=cart #update cart if session has cart
        #print(list(request.session.get("cart").keys()))    #for keys use keys() and list for [1,2,3,4],
        return redirect("homepage")




    def get(self,request):
        # check, cart present in session
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}


        var_product = None
        var_categories = Category.get_all_categories()
        cateid = request.GET.get('categoryid')

        if cateid:
            var_product = Product.get_all_products_by_cat_id(cateid)
        else:
            var_product = Product.get_all_products()

        data = {}
        data['prodict'] = var_product
        data['catdict'] = var_categories

        # get session
        print("You are :", request.session.get('email'))

        # print(var_product)
        return render(request, "index.html", data)

