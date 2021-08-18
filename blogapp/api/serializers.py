from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User 


from .models import *



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields =['email', 'username', 'password', 'password2', 'first_name' , 'last_name']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
            
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':"passwords must match"})
        user.set_password(password)
        user.save()
        return user