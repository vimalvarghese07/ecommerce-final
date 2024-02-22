from django.db import models

class UserDetailsModel(models.Model):

    user_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    