import uuid
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from packs.models import Pack
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=32, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=True, blank=False)
    # Street Address is not required
    street_address2 = models.CharField(max_length=80,
                                       null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    # Street Address is not required
    county = models.CharField(max_length=40, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False,
                           blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    # New fields to ensure that the order is not duplicated
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        # Generates a random number to assign to each order using UUID
        return uuid.uuid4().hex.upper()

    def update_total(self):
        # Updates the order total every time a new line item is added
        self.order_total = self.lineitems.\
            aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        # Override the original save method, allowing an order number to be
        # set if one hasn't been done previously
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False,
                              blank=False, on_delete=models.CASCADE,
                              related_name='lineitems')
    pack = models.ForeignKey(Pack, null=False,
                             blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2, null=False,
                                         blank=False, editable=False)

    def save(self, *args, **kwargs):
        # Overrides the original save method to set the lineitem total and
        # update the order total
        if self.pack.on_sale:
            self.lineitem_total = self.pack.reduced_price
        else:
            self.lineitem_total = self.pack.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.pack.sku} on order {self.order.order_number}'
