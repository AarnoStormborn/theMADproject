import uuid
from django.db import models
from authentication.models import Profile
from products.models import Mobile

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.customer.user.username}:  {self.order_id}"

    class Meta:
        verbose_name_plural = 'Order'

class OrderItem(models.Model):
    product = models.ForeignKey(Mobile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True, default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.brand} {self.product.name}"

    class Meta:
        verbose_name_plural = 'OrderItem'
class UserCart(models.Model):
    pass