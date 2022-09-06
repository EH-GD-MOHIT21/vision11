from django.contrib import admin
# Register your models here.

from .models import Match,Team,PlayersMatchData, User_Feature_Suggestion,Player,UserTeam,Contest
from django import forms

class CustomMatch(admin.ModelAdmin):
    list_display = ["title","team1", "team2", "time", "is_match_end"]
    search_fields = ["title","team1", "team2", "time", "is_match_end"]


class CustomContest(admin.ModelAdmin):
    list_display = ["match_id","entry_fee","fee_type","reward_claimed","length","price_fee"]
    search_fields = ["match_id__title","entry_fee","fee_type","reward_claimed","length","price_fee"]

    def get_form(self,request,obj=None,**kwargs):
        kwargs['widgets']={
            'price_distribution_array':forms.Textarea(attrs={'placeholder':'An array of like [0.3,0.2,0.2,0.2,0.1,0] for a contest of length 6 or pass strings seprated by enter in forms of 0-1:0.2   for 1st and 2nd player stack will be 0.1 each total 0.2 of total price money'})
        }
        return super().get_form(request,obj,**kwargs)


class CustomPlayer(admin.ModelAdmin):
    list_display = ["pid","player_name","player_points","player_type"]
    search_fields = ["pid","player_name","player_points","player_type"]



class CustomTeam(admin.ModelAdmin):
    list_display = ["team_id","team_name"]
    search_fields = ["team_id","team_name"]


# error
class CustomPlayerMatchData(admin.ModelAdmin):
    list_display = ["match_url","pid","points"]
    search_fields = ["match_url__title","pid__player_name","points"]



class CustomUserTeam(admin.ModelAdmin):
    list_display = ["match_id","user","total_team_points"]
    search_fields = ["match_id__title","user__username","user__email"]



class CustomUserFeatureSuggestion(admin.ModelAdmin):
    list_display = ["user","feature_title","is_seen"]
    search_fields = ["user__username","feature_title","user__email"]



admin.site.register(Match,CustomMatch)
admin.site.register(Contest,CustomContest)
admin.site.register(Team,CustomTeam)
admin.site.register(PlayersMatchData,CustomPlayerMatchData)
admin.site.register(Player,CustomPlayer)
admin.site.register(User_Feature_Suggestion,CustomUserFeatureSuggestion)
admin.site.register(UserTeam,CustomUserTeam)