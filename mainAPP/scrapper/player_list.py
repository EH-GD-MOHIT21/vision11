# heavy task should need time atleast 1 minute.
import requests
from bs4 import BeautifulSoup
from django.utils import timezone

a = timezone.now()

URL = 'https://www.cricbuzz.com/live-cricket-scorecard/46081/gt-vs-srh-40th-match-indian-premier-league-2022'

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

# print(players)

print(timezone.now()-a)