from django.db import models
# Importing abstract user that will be made the use of(?)
from django.contrib.auth.models import AbstractUser

# Django framework provides default user models, but there are many limitations to them, Trying to add different features 
# or/and parameters to the default Django user model Later in the development, will likely result in bugs that cost developers both time AND money,
# That's why it it recommended to start off the project by creating a custom user model; 
# Dont forget to tell Django to use it by adding it to the settings.py 

# For FUTURE: Add function, allowing user to authenticate their login using an OTP

# 'unique=True' parameter ensures that a specific user name can be used only ONCE
# The email is added as one of the parameters, so users can log in into an account 
# using email instead of the username
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150)
    # May be OTP to reset a password(?)
    otp = models.CharField(unique=True, max_length=100)
    
    USERNAME_FIELD = 'email'
    USERNAME_FIELD = ['username']
    
    def __str__(self):
        return self.email
