from django.db import models
from mainAPP.models import Player
# Create your models here.



class UserTeam(models.Model):
    player1 = models.ForeignKey(Player,on_delete=models.Case,related_name="player1")
    player2 = models.ForeignKey(Player,on_delete=models.Case,related_name="player2")
    player3 = models.ForeignKey(Player,on_delete=models.Case,related_name="player3")
    player4 = models.ForeignKey(Player,on_delete=models.Case,related_name="player4")
    player5 = models.ForeignKey(Player,on_delete=models.Case,related_name="player5")
    player6 = models.ForeignKey(Player,on_delete=models.Case,related_name="player6")
    player7 = models.ForeignKey(Player,on_delete=models.Case,related_name="player7")
    player8 = models.ForeignKey(Player,on_delete=models.Case,related_name="player8")
    player9 = models.ForeignKey(Player,on_delete=models.Case,related_name="player9")
    player10 = models.ForeignKey(Player,on_delete=models.Case,related_name="player10")
    player11 = models.ForeignKey(Player,on_delete=models.Case,related_name="player11")
    captain = models.ForeignKey(Player,on_delete=models.Case,related_name="captain")
    vice_captain = models.ForeignKey(Player,on_delete=models.Case,related_name="vice_captain")




class Contest(models.Model):
    entry_fee = models.FloatField(default=1)
    length = models.IntegerField(default=1)
    price_fee = models.FloatField(default=0)
    teams = models.ManyToManyField(to=UserTeam)



    def save(self,*args,**kwargs):
        self.price_fee = self.entry_fee * 0.7 * self.length
        super().save(self,*args,**kwargs)