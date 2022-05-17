from attr import fields
from rest_framework.serializers import ModelSerializer
from mainAPP.models import Contest, Match, Player, PlayersMatchData,User_Feature_Suggestion


class MatchListSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class FantasyScoreSerializer(ModelSerializer):
    class Meta:
        model = PlayersMatchData
        exclude = ['match_url']


class GameSquadSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class FeatureRequestSerializer(ModelSerializer):
    class Meta:
        model = User_Feature_Suggestion
        fields = "__all__"


class ContestSerializer(ModelSerializer):
    class Meta:
        model = Contest
        exclude = ["password"]