from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField
import string
import uuid
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


class Order(models.Model):
    order_id= models.CharField(max_length=6, editable=False)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    def save(self,*args,**kwargs):
        if not self.order_id:
            # Generate ID once, then check the db. If exists, keep trying.
            self.order_id = id_generator()

            while Order.objects.filter(order_id=self.order_id).exists():
                self.order_id = id_generator()
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

