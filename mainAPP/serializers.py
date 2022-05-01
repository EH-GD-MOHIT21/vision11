from rest_framework.serializers import ModelSerializer
from mainAPP.models import Match, Player


class MatchListSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class LiveScoreSerializer(ModelSerializer):
    class Meta:
        model = ''


class GameSquadSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'