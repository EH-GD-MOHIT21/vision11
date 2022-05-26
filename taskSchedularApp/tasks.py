from __future__ import absolute_import, unicode_literals
import ast
from celery import shared_task as task
from mainAPP.scrapper.upcoming_matches import list_today_matches
from mainAPP.scrapper.live_score import Update_Live_Score
from mainAPP.scrapper.team_scrapper import Get_Teams
from mainAPP.scrapper.players_scrapper import Get_Players
from mainAPP.repository import vision11
from mainAPP.models import Contest, UserTeam,Match,PlayersMatchData
from django.utils import timezone
from celery.utils.log import get_task_logger
from usermanagerAPP.models import VisionCurrencyDetails
logger = get_task_logger(__name__)



# time limit is expiration time if it's continuously executing after denoted time (in seconds)
@task(name='get_live_score',time_limit=25)
def EveryThreeMinutesTask():

    match_urls = vision11().Get_Live_Match_Urls()
    for url in match_urls:
        logger.info(f"updating live score for: {url} at "+str(timezone.now())+' hours!')
        try:
            Update_Live_Score(url)
            match = Match.objects.get(url=url)
            teams = UserTeam.objects.filter(match_id=match)
            for team in teams:
                team.total_team_points = 0
                all_players = team.players.all()
                playersdata = PlayersMatchData.objects.filter(match_url=team.match_id)
                for player in playersdata:
                    for team_player in all_players:
                        if (player.pid.pid) == (team_player.pid):
                            
                            if team.captain.pid == team_player.pid:
                                team.total_team_points += (player.points*2)
                            elif team.vice_captain.pid == team_player.pid:
                                team.total_team_points += (player.points*1.5)
                            else:
                                team.total_team_points += player.points
                            team.save()
                            break
            logger.info(f"successfully updated live score for: {url} at "+str(timezone.now())+' hours!')
        except Exception as e:
            logger.debug(f"failed to update live score for: {url} at "+str(timezone.now())+f' hours! due to :{e}')



# fetch next upcoming matches
@task(name='fetch_match_list',time_limit=25)
def EveryDayTask():
    try:
        list_today_matches()
        logger.debug("successfully updated upcoming matches at "+str(timezone.now())+' hours!')
    except Exception as e:
        logger.debug(f"failed to update upcoming matches at "+str(timezone.now())+f' hours! due to :{e}')




# update players/team model here to be updated
@task(name='updateteamorplayers',time_limit=25)
def EveryMondayTask():
    try:
        Get_Teams()
        logger.debug("successfully updated Teams at "+str(timezone.now())+' hours!')
    except Exception as e:
        logger.debug(f"failed to update Teams at "+str(timezone.now())+f' hours! due to :{e}')
    try:
        Get_Players()
        logger.debug("successfully updated Players at "+str(timezone.now())+' hours!')
    except Exception as e:
        logger.debug(f"failed to update Players at "+str(timezone.now())+f' hours! due to :{e}')



@task(name='providewinnerusercoins',time_limit=25)
def ProvideMoneyUser(match_obj_id):
    match_obj = Match.objects.get(id=match_obj_id)
    
    contests = Contest.objects.filter(match_id=match_obj)
    for contest in contests:
        if not contest.reward_claimed:
            teams = contest.teams.all().order_by('-total_team_points')
            price = (contest.price_fee/contest.length)*len(teams)
            stack = []
            if not(contest.price_distribution_array == '' or contest.price_distribution_array == None):
                stack = ast.literal_eval(contest.price_distribution_array)
            for _i in range(contest.no_of_winners):
                user_team = teams[_i]
                if user_team.user.currency_type == contest.fee_type:
                    if stack:
                        mystack = float(stack[_i])*price
                    elif contest.is_equal_distribute:
                        mystack = price/contest.no_of_winners
                    else:
                        mystack = price
                    user_team.user.vision_credits += round(mystack,2)
                    user_team.user.contests_won += 1
                    user_team.user.save()
                    VisionCurrencyDetails(user=user_team.user,currency_type_user=user_team.user.currency_type,payment=round(price,2),log=f'win a contest with id {contest.id}, team id {user_team.id}',currency_type_contest=contest.fee_type).save()
                else:
                    VisionCurrencyDetails(user=user_team.user,currency_type_user=user_team.user.currency_type,payment=round(price,2),log=f'win a contest with id {contest.id}, team id {user_team.id} but modified currency.',payment_add=False,currency_type_contest=contest.fee_type).save()
            contest.reward_claimed = True
            contest.save()
            logger.debug(f"successfully updated balance {round(price,2)} for {user_team.user.username} at "+str(timezone.now())+' hours!')
        else:
            teams = contest.teams.all().order_by('-total_team_points')
            price = (contest.price_fee/contest.length)/len(teams)
            user_team = teams[0]
            VisionCurrencyDetails(user=user_team.user,currency_type_user=user_team.user.currency_type,payment=round(price,2),log=f'win a contest with id {contest.id}, team id {user_team.id} but reward already collected.',payment_add=False,currency_type_contest=contest.fee_type).save()
            logger.debug(f"skip contest updated balance for {contest.id} at "+str(timezone.now())+' hours!')