from django.db import models

class CategoryModel(models.Model):

    categoryid = models.CharField(null=False,primary_key=True,max_length=30)
    category = models.CharField(max_length=30)
    productid = models.CharField(max_length=100)
    