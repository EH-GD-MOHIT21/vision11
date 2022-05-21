from locale import currency
from django.db import models
from django.utils import timezone

from usermanagerAPP.exception import InvalidCurrencyType
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

    contests_won = models.IntegerField(
        default=0
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
        previous = User1.objects.get(
            id=instance.id
    )

    except:
        return

    if previous.currency_type == instance.currency_type and previous.adult == instance.adult:
        return
    if previous.currency_type == 'vision candies' and instance.currency_type == 'vision coins' and not previous.adult and instance.adult:
        instance.vision_credits = 0
    elif previous.adult and instance.adult:
        raise InvalidCurrencyType("You are probably demoting the Currency That is Not allowed.")
    elif not previous.adult and instance.adult:
        raise InvalidCurrencyType('Please specify vision coins as your currency.')
    else:
        raise InvalidCurrencyType()



class VisionCurrencyDetails(models.Model):
    user = models.ForeignKey(
        User1,
        on_delete=models.Case
    )

    log = models.TextField()

    currency_type_user = models.CharField(
        max_length=20,
        default='vision candies'
    )

    currency_type_contest = models.CharField(
        max_length=20,
        default='vision candies'
    )

    payment = models.FloatField(
        default=0
    )

    payment_add = models.BooleanField(
        default=True
    )

    save_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def save(self,*args,**kwargs):
        self.save_at = timezone.now()
        super(VisionCurrencyDetails, self).save(*args, **kwargs)