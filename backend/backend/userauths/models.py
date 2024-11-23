from django.db import models
# Importing abstract user that will be made the use of(?)
from django.contrib.auth.models import AbstractUser

# Django framework provides default user models, but there are many limitations to them, Trying to add different features 
# or/and parameters to the default Django user model Later in the development, will likely result in bugs that cost developers both time AND money,
# That's why it it recommended to start off the project by creating a custom user model; 
# Dont forget to tell Django to use it by adding it to the settings.py 

# For FUTURE: Add function, allowing user to authenticate their login using an OTP



