from django.db import models

class ProductModel(models.Model):

    productid = models.CharField(null=False,primary_key=True,max_length=30)
    productname = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    