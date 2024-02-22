from django.db import models

class PaymentModel(models.Model):

    paymentid = models.CharField(null=False,primary_key=True,max_length=30)
    productid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    orderid = models.CharField(max_length=100)
    