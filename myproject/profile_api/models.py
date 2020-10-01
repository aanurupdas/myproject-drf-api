from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,)   
from datetime import date,timedelta,datetime

class UserProfileManager(BaseUserManager):
    def create_user(self, email, contact, password=None):
        '''
        Creates and saves a User with the given email,contact and password.
        '''
        if not email:
            raise ValueError('User must have an valid email address')

        user = self.model(
            email=email,
            contact=contact,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contact, password=None):
        '''
        Creates and saves a User with the given email,contact and password.
        '''
        user = self.create_user(
            email,
            contact=contact,
            password=password,
        )
       
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
        unique=True,
    )
    contact = models.CharField(max_length=15, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
       return self.is_superuser

    def has_module_perms(self, app_label):
       return self.is_superuser

    class Meta:
        db_table = 'login'         

class UserProfileData(models.Model):
     
    user = models.OneToOneField(UserProfile,related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=40)
    age = models.IntegerField()
    
    def _str_(self):
        return self.user.name 

    class Meta:
        db_table = 'user_data' 

class UserAddress(models.Model):

    profile = models.OneToOneField(UserProfileData,related_name='address',on_delete=models.CASCADE) 
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pin_code = models.CharField(max_length=40)

    class Meta:
        db_table = 'user_address'      