from django.db import models

# Create your models here.

choices = (
    ('wicket_keeper_batsman','wicket_keeper_batsman'),
    ('batsman','batsman'),
    ('all_rounder','all_rounder'),
    ('bowler','bowler')
)



class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_pic = models.ImageField(null=True,blank=True)




class Player(models.Model):
    player_name = models.CharField(max_length=50)
    team = models.ManyToManyField(to=Team)
    player_pic = models.ImageField(null=True,blank=True)
    player_points = models.FloatField(default=7)
    player_type = models.CharField(choices=choices,default=choices[0],max_length=30)




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