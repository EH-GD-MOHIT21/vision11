from django.db import models
from usermanagerAPP.models import User1
# Create your models here.


class Team(models.Model):
    team_id = models.IntegerField(unique=True,primary_key=True)
    team_name = models.CharField(max_length=50)
    team_img = models.ImageField(upload_to = 'team_img',null=True,blank=True)
    team_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    pid = models.IntegerField(unique=True,primary_key=True)
    player_name = models.CharField(max_length=50)
    player_pic = models.ImageField(null=True,blank=True)
    player_points = models.FloatField(default=7)
    player_type = models.CharField(max_length=30)
    player_team = models.ManyToManyField(Team)



class User_Feature_Suggestion(models.Model):
    user = models.ForeignKey(User1,on_delete=models.CASCADE)
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    feature_title = models.CharField(max_length=100,null=True)
    feature_des = models.TextField(null=True,blank=True)
    is_seen = models.BooleanField(default=False)


class Match(models.Model):
    url = models.TextField(unique=True,primary_key=True)
    title = models.TextField(null=True,blank=True)
    time = models.DateTimeField()
    name = models.CharField(max_length=100,null=True,blank=True)
    team1 = models.CharField(max_length=60,null=True,blank=True)
    team2 = models.CharField(max_length=60,null=True,blank=True)
    is_match_end = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class PlayersMatchData(models.Model):
    pid = models.ForeignKey(Player,on_delete=models.CASCADE)
    match_url = models.ForeignKey(Match,on_delete=models.Case)
    runsScored = models.CharField(max_length=4)
    ballsFaced = models.CharField(max_length=4)
    fours = models.CharField(max_length=4)
    sixes = models.CharField(max_length=4)
    strikeRate = models.CharField(max_length=10)
    out = models.BooleanField()
    overs = models.CharField(max_length=4)
    maidens = models.CharField(max_length=4)
    runsGiven = models.CharField(max_length=4)
    wickets = models.CharField(max_length=4)
    wides = models.CharField(max_length=4)
    noBalls = models.CharField(max_length=4)
    economy = models.CharField(max_length=4)
    catches = models.IntegerField()
    runouts = models.IntegerField()
    stumpings = models.IntegerField()
    points = models.FloatField()


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