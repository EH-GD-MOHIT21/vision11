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

    def __str__(self):
        return self.player_name



class User_Feature_Suggestion(models.Model):
    user = models.ForeignKey(User1,on_delete=models.CASCADE)
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    feature_title = models.CharField(max_length=100,null=True)
    feature_des = models.TextField(null=True,blank=True)
    is_seen = models.BooleanField(default=False)


class Match(models.Model):
    url = models.TextField(unique=True)
    title = models.TextField(null=True,blank=True)
    time = models.DateTimeField()
    name = models.CharField(max_length=100,null=True,blank=True)
    team1 = models.CharField(max_length=60,null=True,blank=True)
    team2 = models.CharField(max_length=60,null=True,blank=True)
    is_match_end = models.BooleanField(default=False)
    team1_img = models.TextField(null=True,blank=True)
    team2_img = models.TextField(null=True,blank=True)

    def save(self,*args,**kwargs):
        try:
            self.team1_img = Team.objects.get(team_name=self.team1).team_img
            self.team2_img = Team.objects.get(team_name=self.team2).team_img
        except:
            pass

        super(Match, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ". " + self.title



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
    match_id = models.ForeignKey(Match,on_delete=models.Case)
    user = models.ForeignKey(User1,on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    captain = models.ForeignKey(Player,on_delete=models.Case,related_name="captain")
    vice_captain = models.ForeignKey(Player,on_delete=models.Case,related_name="vice_captain")
    total_team_points = models.FloatField(default=0)


    def save(self,*args,**kwargs):
        try:
            all_players = self.players.all()
            playersdata = PlayersMatchData.objects.filter(match_url=self.match_id)
            for player in playersdata:
                for team_player in all_players:
                    if player.pid == team_player.pid:
                        self.total_team_points += player.points
                        break
        except:
            pass
        super(UserTeam, self).save(*args,**kwargs)




class Contest(models.Model):
    match_id = models.ForeignKey(Match,on_delete=models.CASCADE)
    user = models.ManyToManyField(User1)
    entry_fee = models.FloatField(default=1)
    fee_type = models.CharField(max_length=20,default='vision candies')
    length = models.IntegerField(default=1)
    price_fee = models.FloatField(default=0)
    teams = models.ManyToManyField(to=UserTeam)
    reward_claimed = models.BooleanField(default=False)
    contest_type = models.CharField(default="public",max_length=25)
    password = models.CharField(max_length=128,null=True,blank=True)


    def save(self,*args,**kwargs):
        self.price_fee = round(self.entry_fee * 0.7 * self.length,2)
        super(Contest, self).save(*args, **kwargs)