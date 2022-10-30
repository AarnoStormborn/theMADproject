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

    @property
    def get_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_item_total for item in orderitems])
        return total

    @property
    def shipping_price(self):
        price = self.get_total*0.05
        return price

    @property 
    def total_price(self):
        total = self.get_total + self.shipping_price
        return round(total)

    class Meta:
        verbose_name_plural = 'Order'

class OrderItem(models.Model):
    product = models.ForeignKey(Mobile, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True, default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.brand} {self.product.name}"

    @property
    def get_item_total(self):
        total = self.product.price * self.quantity
        return total

    class Meta:
        verbose_name_plural = 'OrderItem'