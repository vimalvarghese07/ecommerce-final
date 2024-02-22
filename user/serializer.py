from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetailsModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password' : {'write_only':True}}
        
        def create(self,validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        def put(self,validated_data):
            user = User.objects.create(
                username =validated_data['username'],
                email=validated_data['email'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

        
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailsModel
        fields = ['user_id','address','phonenumber']
        
