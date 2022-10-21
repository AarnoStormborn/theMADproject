from django.db import models
from PIL import Image

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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 280 or img.width > 280:
            output_size = (280,280)
            img.thumbnail(output_size)
            img.save(self.image.path)


    class Meta:
        verbose_name_plural = 'Mobile'

# class Sellers(models.Model):

#     product = models.ForeignKey(Mobile, on_delete=models.SET_NULL, null=False)
#     seller = models.ForeignKey(UserDetails, on_delete=models.SET_NULL, null=False)

