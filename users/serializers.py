from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User
class useSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','name','email','password']
    
        def create(self, validated_data):
          password = validated_data['password']
          instance = self.Meta.model(**validated_data)
          if password is not None:
            instance.set_password(password)
            instance.save()
            
            return instance 
          
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email')            