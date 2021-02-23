from django.db import models


# null=true if no validation for input empty text
class Customer(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=50,default="")
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def register(self):
        self.save()


    def isExits(self):
        # Checking email and self email is current email in input text comparing with already email in db
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    def isExitsPhone(self):
            # Checking email and self email is current email in input text comparing with already email in db
        if Customer.objects.filter(phone=self.phone):
            return True
        else:
            return False

    @staticmethod
    def getCustomerEmail(email):
        try:
            # get is used to get single record
            return Customer.objects.get(email=email)
        except:
            return False


