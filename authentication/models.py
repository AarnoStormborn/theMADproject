from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    address1 = models.CharField(max_length=600, blank=True, null=True)
    address2 = models.CharField(max_length=600, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True,null=True)
    zipcode = models.CharField(max_length=10, blank=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profile'