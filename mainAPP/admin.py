from django.contrib import admin

# Register your models here.

from .models import Match,Team,PlayersMatchData


admin.site.register(Match)
admin.site.register(Team)
admin.site.register(PlayersMatchData)