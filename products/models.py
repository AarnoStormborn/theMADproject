from django.db import models

class Mobile(models.Model):

    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    price = models.CharField(max_length=10)
    storage = models.CharField(max_length=10)
    ram = models.CharField(max_length=10)
    display_type = models.CharField(max_length=40)
    display_size = models.CharField(max_length=10)
    processor = models.CharField(max_length=40)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = 'Mobile'
