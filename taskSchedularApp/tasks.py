from __future__ import absolute_import, unicode_literals
from celery import shared_task as task
from mainAPP.scrapper.upcoming_matches import list_today_matches


# time limit is expiration time if it's continuously executing after denoted time (in seconds)
@task(name='get_live_score',time_limit=25)
def EveryThreeMinutesTask():
    print('live score fetching')


# fetch next upcoming matches
@task(name='fetch_match_list',time_limit=25)
def EveryDayTask():
    print("This runs every day at 0-10 AM GMT")


# update players/team model here to be updated
@task(name='updateteamorplayers',time_limit=25)
def EveryMondayTask():
    print("This runs every monday at 1-30 AM GMT")