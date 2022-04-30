from random import choices
from django.db import models
from .models_manager import UserManager
from django.contrib.auth.models import AbstractUser
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from vision11.email.send_email import send_mail
from vision11.email.messages import messages
from vision11.email.subjects import subjects
from django.db.models.signals import pre_save


class Choices(models.TextChoices):
    VISION_COINS = ('vision coins', 'vision coins')
    VISION_CANDIES = ('vision candies', 'vision candies')



# django-all-auth overloaded login callback using signal
@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    # send mail here
    email = user.email
    send_mail(to=[email], subject=subjects["login-success"],
              message=messages["login-success"])


# to identify the currency 18+ have vision coins
Currency_Choices = [
    ('vision candies', 'vision candies'),
    ('vision coins', 'vision coins')
]


# gender choice
Gender_Choices = [
    ('Male', 'Male'),
    ('Female', 'Female')
]


# custom user model
class User1(AbstractUser):
    first_name = models.CharField(
        max_length=20
    )

    last_name = models.CharField(
        max_length=20
    )

    username = models.CharField(
        max_length=20,
        unique=True
    )

    age = models.IntegerField(
        null=True,
        blank=True
    )

    email = models.EmailField(
        max_length=50
    )

    vision_credits = models.FloatField(
        default=0
    )

    currency_type = models.CharField(
        choices=Currency_Choices,
        default=Choices.VISION_CANDIES,
        max_length=50
    )

    gender_type = models.CharField(
        choices=Gender_Choices,
        null=True,
        max_length=10
    )

    country = models.CharField(
        max_length=50
    )

    adult = models.BooleanField(
        'Adult_status',
        default=False
    )

    staff = models.BooleanField(
        'Staff_status',
        default=False
    )

    superuser = models.BooleanField(
        'super_user_status',
        default=False
    )

    aadhar_image = models.FileField(
        upload_to='others',
        null=True,
        blank=True
    )

    objects = UserManager()

    @property
    def is_adult(self):
        return self.adult

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser



@receiver(pre_save, sender=User1)
def pre_save(sender, instance, **kwargs):
    try:
        previous = User1.objects.get(id=instance.id)
    except:
        return
    if previous.adult and previous.currency_type == 'vision coins':
        if instance.currency_type == 'vision candies':
            print(instance.currency_type)
            instance.currency_type = Choices.VISION_COINS
        if not instance.adult:
            instance.adult = True
    if previous.adult != instance.adult and instance.adult:
        instance.currency_type = Choices.VISION_COINS
        instance.vision_credits = 0
    elif previous.currency_type != instance.currency_type:
        instance.vision_credits = 0