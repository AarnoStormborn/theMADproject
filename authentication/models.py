from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    location = models.CharField(max_length=100, default='Earth')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profile'