from rest_framework import serializers
from .models import PaymentModel

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PaymentModel
		fields = ('orderid', 'productid','userid','paymentid')
