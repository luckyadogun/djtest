from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.postgres.fields import ArrayField

from django.utils.translation import gettext as _

# import uuid

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "countries"

class Shipment(models.Model):

    SHIPMENT_STATUS = (
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('delivered', 'Delivered')
    )

    owner_fullname = models.CharField(max_length=200, blank=True)
    receiver_fullname = models.CharField(max_length=200)
    receipient_address = models.CharField(max_length=200) 
    date_of_shipment = models.DateField(auto_now_add=True)
    placement_point = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='parcel_origin')
    destination = models.ForeignKey(Countries, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=200, blank=True, null=False)
    # routes = models.ManyToManyField(Countries, related_name='fake_countries')
    route_1 = models.CharField(max_length=100, blank=True, null=True)
    route_2 = models.CharField(max_length=100, blank=True, null=True)
    route_3 = models.CharField(max_length=100, blank=True, null=True)
    route_4 = models.CharField(max_length=100, blank=True, null=True)
    shipment_status = models.CharField(choices=SHIPMENT_STATUS, max_length=200, default=1)
    tracking_code = models.CharField(max_length=200, default=get_random_string)
    client_real_name = models.CharField(max_length=200, blank=True)
    client_email = models.EmailField(blank=True)
    payment_status = models.BooleanField(default=False)
    is_dispatched = models.BooleanField(_("Dispatched"), default=False)
    is_departed = models.BooleanField(_("Departed"), default=False)
    is_arrived = models.BooleanField(_("Arrived"), default=False)
    is_delivered = models.BooleanField(_("Delivered"), default=False)


    def __str__(self):
        return str(self.tracking_code)


class Quotes(models.Model):
    service = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    length = models.CharField(max_length=200, blank=True)
    height = models.CharField(max_length=200, blank=True)
    from_country = models.CharField(max_length=200, blank=True)
    to_country = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    is_door_to_door = models.BooleanField(default=False)
    is_mailbox = models.BooleanField(default=False)
    is_pickup = models.BooleanField(default=False)
    is_warehousing = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name_plural = "quotes"





