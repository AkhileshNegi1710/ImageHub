from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        fname = postData.get("fname")
        lname = postData.get("lname")
        phone = postData.get("phone")
        email = postData.get("email")
        password = postData.get("password")

        # after Validation of form, typed data in input text are remain as it is, not removed
        value = {
            'fname': fname,
            'lname': lname,
            'phone': phone,
            'email': email

            # Above password has not been used  so that user has to type after validation
        }

        customer = Customer(fname=fname, lname=lname, phone=phone, email=email, password=password)

        # Validaiton Functions

        error_msg = self.validateCustomer(customer)

        # saving data fo form
        if not error_msg:
            print(fname, lname, phone, email, password)
            customer.password = make_password(customer.password)

            # we can also do customer.save() and registered
            customer.register()

            return redirect("homepage")
        else:
            data = {
                "error": error_msg,
                "values": value
            }

            # HttpResponse has request = post method = has get which can access fields
            return render(request, "signup.html", data)

    def validateCustomer(self, customer):
        # Validation Check
        error_msg = None

        if not customer.fname:
            error_msg = "First Name required"
        elif len(customer.fname) < 4:
            error_msg = "First Name must be 4 Char long"
        if not customer.lname:
            error_msg = "Last Name required"
        elif len(customer.lname) < 4:
            error_msg = "Last Name must be 4 Char long"
        if not customer.phone:
            error_msg = "Phone required"
        elif len(customer.phone) < 4:
            error_msg = "Phone Number must be 10 Char long"
        elif len(customer.password) < 6:
            error_msg = "Password must be 6 char long"
        elif len(customer.email) < 5:
            error_msg = "Email must be 5 Char long"
        elif customer.isExits():
            error_msg = "Email Address Already Registered.."
        elif customer.isExitsPhone():
            error_msg = "Phone Number Already Registered.."
        return error_msg
