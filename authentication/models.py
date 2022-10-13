from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    location = models.CharField(max_length=100, default='Earth')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profile'

class UserDetails(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=600)
    zipcode = models.CharField(max_length=10)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.customer.user.username

    class Meta:
        verbose_name_plural = 'UserDetails'