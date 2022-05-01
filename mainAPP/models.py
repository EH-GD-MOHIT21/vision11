from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from usermanagerAPP.models import User1
# Create your models here.

choices = (
    ('WK-Batsman','WK-Batsman'),
    ('Batsman','Batsman'),
    ('Batting Allrounder','Batting Allrounder'),
    ('Bowling Allrounder','Bowling Allrounder'),
    ('Bowler','Bowler')
)


class Player(models.Model):
    pid = models.IntegerField(unique=True,primary_key=True)
    player_name = models.CharField(max_length=50)
    player_pic = models.ImageField(null=True,blank=True)
    player_points = models.FloatField(default=7)
    player_type = models.CharField(choices=choices,default=choices[0],max_length=30)


class Team(models.Model):
    team_id = models.IntegerField(unique=True,primary_key=True)
    team_name = models.CharField(max_length=50)
    team_img = models.ImageField(upload_to = 'team_img',null=True,blank=True)
    team_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.team_name

class User_Feature_Suggestion(models.Model):
    user = models.ForeignKey(User1,on_delete=models.CASCADE)
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    feature_title = models.CharField(max_length=100,null=True)
    feature_des = models.TextField(null=True,blank=True)
    


class Match(models.Model):
    url = models.TextField(max_length=100,unique=True,primary_key=True)
    title = models.TextField(null=True,blank=True)
    time = models.DateTimeField()
    players = models.ManyToManyField(Player)

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

