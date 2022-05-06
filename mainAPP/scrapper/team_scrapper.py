from bs4 import BeautifulSoup
import requests
from mainAPP.models import Team

URL = 'https://www.cricbuzz.com/cricket-team'
URL1 = 'https://www.cricbuzz.com/cricket-team/domestic'
URL2 = 'https://www.cricbuzz.com/cricket-team/league'
URL3 = 'https://www.cricbuzz.com/cricket-team/women'

urls = [URL,URL1,URL2,URL3]

for url in urls:
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    all_teams = soup.find_all('a',class_='cb-teams-flag-img')
    BASE_URL = 'https://www.cricbuzz.com'
    for teams in all_teams:
        img = teams.find('img')['src']
        title,href,id = teams['title'],teams['href'],teams['href'].split('/')[-1]
        Team.objects.update_or_create(team_id=int(id),team_name=title,team_img=BASE_URL+img,team_url=BASE_URL+href)
