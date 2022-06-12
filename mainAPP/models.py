import ast
from datetime import datetime
from django.db import models
from mainAPP.Exceptions import InvalidWinnerListParser, InvalidWinnerStringParser
from usermanagerAPP.models import User1

# Create your models here.


class Team(models.Model):
    team_id = models.IntegerField(
        unique=True,
        primary_key=True
    )

    team_name = models.CharField(
        max_length=50
    )

    team_img = models.ImageField(
        upload_to='team_img',
        null=True,
        blank=True
    )

    team_url = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.team_name


class Player(models.Model):
    pid = models.IntegerField(
        unique=True,
        primary_key=True
    )

    player_name = models.CharField(
        max_length=50
    )

    player_pic = models.ImageField(
        null=True,
        blank=True,
        default='https://www.cricbuzz.com/a/img/v1/152x152/i1/c182026/rajat-patidar.jpg'
    )

    player_points = models.FloatField(
        default=7
    )

    player_type = models.CharField(
        max_length=30
    )

    player_team = models.ManyToManyField(
        Team
    )

    def __str__(self):
        return self.player_name


class User_Feature_Suggestion(models.Model):
    user = models.ForeignKey(
        User1,
        on_delete=models.CASCADE
    )

    user_first_name = models.CharField(
        max_length=20
    )

    user_last_name = models.CharField(
        max_length=20
    )

    user_email = models.CharField(
        max_length=50
    )

    feature_title = models.CharField(
        max_length=100,
        null=True
    )

    feature_des = models.TextField(
        null=True,
        blank=True
    )

    is_seen = models.BooleanField(
        default=False
    )


class Match(models.Model):
    url = models.TextField(
        unique=True
    )

    title = models.TextField(
        null=True,
        blank=True
    )

    time = models.DateTimeField()

    # for specific test matches
    match_pause_time = models.DateTimeField(
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    team1 = models.CharField(
        max_length=60,
        null=True,
        blank=True
    )

    team2 = models.CharField(
        max_length=60,
        null=True,
        blank=True
    )

    is_test_match = models.BooleanField(
        default=False
    )

    is_match_end = models.BooleanField(
        default=False
    )

    team1_img = models.TextField(
        null=True,
        blank=True
    )

    team2_img = models.TextField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.is_test_match and not isinstance(self.match_pause_time, datetime):
            self.match_pause_time = self.time
            # 8 hour support till next round value, hour 19:30 pause time means it'll pause at 20:00
            # continue till next 4 days and same process work
            self.match_pause_time = self.match_pause_time.replace(
                hour=self.time.hour + 8,
                day=self.time.day + 4
            )
        try:
            if self.team1_img == '' or self.team1_img == None or self.team2_img == None or self.team2_img == '':
                self.team1_img = Team.objects.get(
                    team_name=self.team1).team_img
                self.team2_img = Team.objects.get(
                    team_name=self.team2).team_img
        except:
            pass

        super(Match, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + ". " + self.title


class PlayersMatchData(models.Model):
    pid = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )

    match_url = models.ForeignKey(
        Match,
        on_delete=models.Case
    )

    runsScored = models.IntegerField(default=0)

    ballsFaced = models.IntegerField(default=0)

    fours = models.IntegerField(default=0)

    sixes = models.IntegerField(default=0)

    strikeRate = models.FloatField(default=0)

    out = models.BooleanField(
        default=False
    )

    overs = models.FloatField(default=0)

    maidens = models.IntegerField(default=0)

    runsGiven = models.IntegerField(default=0)

    wickets = models.IntegerField(default=0)

    wides = models.IntegerField(default=0)

    noBalls = models.IntegerField(default=0)

    economy = models.FloatField(default=0)

    catches = models.IntegerField(
        default=0
    )

    runouts = models.IntegerField(
        default=0
    )

    stumpings = models.IntegerField(
        default=0
    )

    points = models.FloatField(
        default=0
    )

    additional_points = models.FloatField(
        default=0
    )

    def __str__(self) -> str:
        return str(self.pid.pid) + " " + str(self.pid.player_name)

    def save(self, *args, **kwargs):
        self.points += self.additional_points
        super(PlayersMatchData, self).save(*args, **kwargs)


class UserTeam(models.Model):
    match_id = models.ForeignKey(
        Match,
        on_delete=models.Case
    )

    user = models.ForeignKey(
        User1,
        on_delete=models.CASCADE
    )

    players = models.ManyToManyField(
        Player
    )

    captain = models.ForeignKey(
        Player,
        on_delete=models.Case,
        related_name="captain"
    )

    vice_captain = models.ForeignKey(
        Player,
        on_delete=models.Case,
        related_name="vice_captain"
    )

    total_team_points = models.FloatField(
        default=0
    )


class Contest(models.Model):
    match_id = models.ForeignKey(
        Match,
        on_delete=models.CASCADE
    )

    user = models.ManyToManyField(
        User1,
        blank=True
    )

    entry_fee = models.FloatField(
        default=1
    )

    fee_type = models.CharField(
        max_length=20,
        default='vision candies'
    )

    length = models.IntegerField(
        default=1
    )

    price_fee = models.FloatField(
        default=0
    )

    teams = models.ManyToManyField(
        to=UserTeam,
        blank=True
    )

    reward_claimed = models.BooleanField(
        default=False
    )

    contest_type = models.CharField(
        default="public",
        max_length=25
    )

    password = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    # admin accessessable fields
    no_of_winners = models.IntegerField(
        default=1
    )

    # internal working [0.5,0.3,0.2] -> 3 winners 1 will get 0.5 times of price_fee, 2 will get 0.3 times of,3 will 0.2 total should be one (0.5+0.3+0.2)

    price_distribution_array = models.TextField(
        null=True,
        blank=True
    )

    is_equal_distribute = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        self.price_fee = round(self.entry_fee * 0.7 * self.length, 2)
        if self.price_distribution_array == '' or self.price_distribution_array == None:
            pass
        else:
            if '-' in self.price_distribution_array and ':' in self.price_distribution_array:
                try:
                    pz = 0
                    array = [0 for i in range(self.length)]
                    for line in self.price_distribution_array.split('\n'):
                        playerrange, value = line.split(':')
                        start, end = map(int, playerrange.split('-'))
                        for i in range(start, end+1):
                            array[i] = float(value)/(end+1-start)
                        pz += float(value)
                    self.no_of_winners = self.length - array.count(0)
                    self.price_distribution_array = array
                    self.is_equal_distribute = False
                    if pz > 1.02:
                        print(pz)
                        raise InvalidWinnerStringParser(
                            message="Total stackper should be less than 1.")
                except Exception as e:
                    raise InvalidWinnerStringParser()
            elif self.price_distribution_array == '' or self.price_distribution_array == None:
                pass

            else:
                try:
                    array = ast.literal_eval(self.price_distribution_array)
                    if not isinstance(array, list):
                        raise InvalidWinnerStringParser(
                            message="Unexpected DataType: Expected List of elements or string")
                    if sum(array) > 1.02:
                        raise InvalidWinnerStringParser(
                            message="Total stackper should be less than 1.")
                    if self.length != len(array):
                        raise InvalidWinnerListParser(
                            message="Expected equal attributes as length of contests.")
                    zeros = array.count(0)
                    self.no_of_winners = self.length - zeros
                    self.price_distribution_array = array
                    self.is_equal_distribute = False
                except Exception as e:
                    raise(e)

        if self.no_of_winners > 1 and (not self.is_equal_distribute) and (self.price_distribution_array == '' or self.price_distribution_array == None):
            raise AttributeError(
                'please set atleast one attribute is_equal_distribute or price_distribution_array if winner > 1.')

        if self.no_of_winners > self.length:
            raise ValueError(
                "no of winners should be less or equal to length of contest.")

        if self.no_of_winners <= 0:
            raise ValueError('Why are you making contest dude?')
        super(Contest, self).save(*args, **kwargs)
