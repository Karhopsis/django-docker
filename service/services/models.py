from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()



class Plan(models.Model):
    PLAN_TYPES = (
        ('full','Full'),
        ('student','Student'),
        ('discount','Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=100)
    discount_percent = models.PositiveIntegerField(validators=[
        MaxValueValidator(100),
    ])



class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscription',on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscription', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscription', on_delete=models.PROTECT)