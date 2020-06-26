from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields

    portfolio_site = models.URLField(blank=True) # blank allow the user to leave the field blank with no error

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) 
    # You need to create the profile_pics folder under media
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"

    def __str__(self):
        return self.user.username