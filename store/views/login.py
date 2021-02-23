from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# make_password and check_password in password hashing



class Login(View):

    def get(self,request):
        return render(request, "login.html")

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.getCustomerEmail(email)
        if customer:
            flag=check_password(password,customer.password)  # comparing password
            if flag:
                # session are used with help of id and emailid
                request.session['customer_id']=customer.id #customer id is saved in session
                # request.session['email']=customer.email  #email id saved in session
                return redirect("homepage")
            else:
                error_msg = "Email or Password Invalid !!"
        else:
            error_msg="Email or Password Invalid !!"


        print(email,password)
        return render(request,"login.html",{"error":error_msg})




def logout(request):
        request.session.clear()
        return redirect("login")