from django.db.models.signals import pre_save
from django.dispatch import receiver
from mainAPP.models import Match,Contest

@receiver(pre_save, sender=Match)
def pre_save(sender, instance, **kwargs):
    try:
        from taskSchedularApp.tasks import ProvideMoneyUser
        previous = Match.objects.get(id=instance.id)
    except:
        return
    if previous.is_match_end != instance.is_match_end and instance.is_match_end == True:
        ProvideMoneyUser.delay(instance.id)
        # do celery stuff here to give price money to winners





#     myarray = []
#     print(instance.price_distribution_array)
#     '''
#     0-0:0.4
#     1-2:0.3
#     3-5:0.2
#     6-10:0.1
#     '''
#     data = instance.price_distribution_array