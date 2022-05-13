from __future__ import absolute_import, unicode_literals
from celery import shared_task as task
from mainAPP.scrapper.upcoming_matches import list_today_matches
from mainAPP.scrapper.live_score import Update_Live_Score
from mainAPP.scrapper.team_scrapper import Get_Teams
from mainAPP.scrapper.players_scrapper import Get_Players
from mainAPP.repository import vision11
from mainAPP.models import UserTeam,Match



# time limit is expiration time if it's continuously executing after denoted time (in seconds)
@task(name='get_live_score',time_limit=25)
def EveryThreeMinutesTask():

    match_urls = vision11().Get_Live_Match_Urls()
    for url in match_urls:
        print(f"updating live score for: {url}")
        try:
            Update_Live_Score(url)
            match = Match.objects.get(url=url)
            teams = UserTeam.objects.filter(match_id=match)
            for team in teams:
                team.save()
            print(f"successfully updated live score for: {url}")
        except Exception as e:
            print(f"failed to update live score due to: {e}")



# fetch next upcoming matches
@task(name='fetch_match_list',time_limit=25)
def EveryDayTask():
    list_today_matches()




# update players/team model here to be updated
@task(name='updateteamorplayers',time_limit=25)
def EveryMondayTask():
    Get_Teams()
    Get_Players()