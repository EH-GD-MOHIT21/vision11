from locale import currency
from django.db import models
from django.utils import timezone
from usermanagerAPP.models import User1
# Create your models here.

class Plan(models.Model):
    plan_price = models.FloatField(default=0)
    vision_coins = models.FloatField(default=0)
    bonus_coins = models.FloatField(default=0)
    offer_start_date = models.DateTimeField(default=timezone.now)
    offer_end_date = models.DateTimeField(null=True,blank=True)

    @property
    def set_vision_coins(self):
        self.vision_coins = round(((self.plan_price/20)+self.bonus_coins),3)

    def save(self, *args, **kwargs):
        self.set_vision_coins
        super(Plan, self).save(*args, **kwargs)


mychoice = (
    ("Pending","pending"),
    ("Success","success")
)

class Choices(models.TextChoices):
    PENDING = ("Pending","pending")
    SUCCESS = ("Success","success")


class Order(models.Model):
    user = models.ForeignKey(User1,on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    order_id = models.SlugField()
    currency = models.CharField(max_length=5,default="INR")
    payment_capture = models.FloatField(default=0)
    order_status = models.CharField(choices=mychoice,default=Choices.PENDING,max_length=25)


    @property
    def update_status(self):
        self.order_status = Choices.SUCCESS