# heavy task should need time atleast 5 minute.
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from mainAPP.models import Match,Player


def find_players_list():

    matches = Match.objects.filter(time__gt=timezone.now())

    for index,match in enumerate(matches):
        URL = match.url

        data = requests.get(URL).text
        soup = BeautifulSoup(data, 'html.parser')

        BASE_URL = 'https://www.cricbuzz.com'
        players = {}
        player_data = soup.find_all('a',class_='margin0 text-black text-hvr-underline')
        for player in player_data:
            player_id = player['href'].split('/')[2]
            link = BASE_URL + player['href']
            name = player.get_text().split(' (')[0]
            players[player_id] = [name,link,'','']


        # cb-col cb-col-20 cb-col-rt , cb-col cb-col-60 cb-lst-itm-sm
        # updating image of player
        for id in players.keys():
            URL = players[id][1]
            data = requests.get(URL).text
            soup = BeautifulSoup(data, 'html.parser')
            img = soup.find_all('div','cb-col cb-col-20 cb-col-rt')[0].find_all('img')[0]
            players[id][2] = (BASE_URL+img['src'])

            # updating player role
            roles = soup.find_all('div',class_='cb-col cb-col-60 cb-lst-itm-sm')[2]
            players[id][3] = roles.get_text().lstrip().rstrip()

        for key in players.keys():
            obj,_ = Player.objects.get_or_create(pid=key,player_name=players[key][0],player_pic=players[key][2],player_type=players[key][3])
            print(obj)
            # append the player to match
            match.players.add(obj)
            match.save()