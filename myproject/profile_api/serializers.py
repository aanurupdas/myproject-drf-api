from rest_framework import serializers
from profile_api.models import (UserProfile,UserProfileData,UserAddress,UserProject)
from django.contrib.auth import authenticate
import django.contrib.auth.password_validation as validators
from datetime import date,timedelta,datetime

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('street','city','state','pin_code',)

class UserProfileDataSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer()
    class Meta:
        model = UserProfileData
        fields = ('name','company_name','address','age',)

class UserRegisterSerializer(serializers.ModelSerializer):
    profile = UserProfileDataSerializer()
    class Meta:
        model = UserProfile
        fields = ('email','contact','password','profile',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = UserProfile.objects.create_user(validated_data['email'],validated_data['contact'],validated_data['password'])
        profile=UserProfileData.objects.create(
            user = user,
            name = profile_data['name'],
            company_name = profile_data['company_name'],
            age = profile_data['age'],
        )
        UserAddress.objects.create(
            profile = profile,
            street = profile_data['address']['street'],
            city = profile_data['address']['city'],
            state = profile_data['address']['state'],
            pin_code = profile_data['address']['pin_code'],
        )
        return user  

    def validate_password(self, data):
        validators.validate_password(password=data,user=UserProfile)
        return data       

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Email or Password Incorrect")

class UserDetailUpdateSerializer(serializers.ModelSerializer):
    profile = UserProfileDataSerializer()
    class Meta:
        model = UserProfile
        fields = ('email','contact','profile',) 
        read_only_fields = ('email','contact')
   
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        profile.name = profile_data.get('name', profile.name)
        profile.company_name = profile_data.get('company_name', profile.company_name)
        profile.age = profile_data.get('age', profile.age)
        profile.save()

        address_data=profile_data.get('address',profile.address)
        profile.address.street = address_data.get('street',profile.address.street)
        profile.address.city =  address_data.get('city',profile.address.city)
        profile.address.state =  address_data.get('state',profile.address.state)
        profile.address.pin_code =  address_data.get('pin_code',profile.address.pin_code)
        profile.address.save()
        return instance
        
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProject
        fields = ('id','project_name','start_date','duration','end_date',)
        read_only_fields = ('end_date',)