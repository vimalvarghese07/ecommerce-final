from rest_framework import serializers
from .models import OrderModel

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = OrderModel
		fields = ('userid', 'productid','orderid')
