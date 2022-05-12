import requests
from bs4 import BeautifulSoup
import bs4
from mainAPP.models import Team,Player

def Get_Players():

    BASE_URL = 'https://www.cricbuzz.com/cricket-team/'
    all_teams = Team.objects.all()

    for indexmota,team in enumerate(all_teams):
        TeamName = team.team_name
        TeamId = str(team.team_id)
        Dynamic_URL = f'{TeamName}/{TeamId}'
        URL = BASE_URL + Dynamic_URL + '/players'
        data = requests.get(URL).text
        soup = BeautifulSoup(data, 'html.parser')
        scrap_data = soup.find('div', 'cb-col-67 cb-col cb-left cb-top-zero')
        roles = ['BATSMEN', 'ALL ROUNDER', 'WICKET KEEPER', 'BOWLER']
        index = -1
        players = {}
        for html_tag in scrap_data:
            if(type(html_tag) == bs4.element.NavigableString):
                continue
            else:
                if str(html_tag['class'][0]) == 'cb-sqd-rol':
                    index += 1
                elif html_tag['class'] == ['cb-col', 'cb-col-50']:
                    id = html_tag['href'].split('/')[2]
                    name = html_tag['title']
                    try:
                        role = roles[index]
                    except:
                        role = roles[1]
                    image = 'https://www.cricbuzz.com' + html_tag.find('img')['src']
                    players[id] = [name, role, image]
        for xxx in players.keys():
            obj,_ = Player.objects.get_or_create(pid=int(xxx),player_name=players[xxx][0],player_pic=players[xxx][2],player_type=players[xxx][1])
            obj.player_team.add(team)
            obj.save()