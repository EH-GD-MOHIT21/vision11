from attr import fields
from rest_framework.serializers import ModelSerializer
from mainAPP.models import Match, Player, PlayersMatchData


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