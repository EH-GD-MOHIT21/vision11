#makes a request at cricbuzz per day from celery
import requests
from bs4 import BeautifulSoup
from operator import *
from mainAPP.models import Match
from datetime import datetime,timezone


def list_today_matches(URL="https://www.cricbuzz.com/cricket-schedule/upcoming-series/all"):
    matches = requests.get(URL).text
    soup = BeautifulSoup(matches, 'html.parser')

    allmatches = soup.find_all('div',id='all-list')[0]
    todays_match = allmatches.find_all('div',class_='cb-col-100 cb-col')[0]
    match_links = []
    match_titles = []
    match_times = []
    match_names = []
    BASE_URL = 'https://www.cricbuzz.com'

    matchlist = todays_match.find_all('div',class_='cb-col-100 cb-col')

    cntr = 0
    for match in matchlist:
        allmatches = match.find_all('div',class_='cb-ovr-flo cb-col-60 cb-col cb-mtchs-dy-vnu cb-adjst-lst')
        for matches in allmatches: 
            dummy_link = matches.find_all('a')[0]
            link = dummy_link['href']
            useful_link = BASE_URL+link.replace('live-cricket-scores','live-cricket-scorecard')
            match_links.append(useful_link)
            match_titles.append(dummy_link['title'])
            match_names.append(dummy_link.get_text())
            cntr += 1

        times = match.find_all('div',class_='cb-col-40 cb-col cb-mtchs-dy-tm cb-adjst-lst')
        for time in times:
            if cntr == 0:
                break
            matchtime = time.find_all('div',class_='cb-font-12 text-gray')[0]
            servertimegmt = matchtime.find_all('span')[0]
            m2 = datetime.strptime(servertimegmt.get_text(), '%I:%M %p')
            today = datetime.today()
            m2 = m2.replace(year=today.year,month=today.month,day=today.day,tzinfo=timezone.utc)
            match_times.append(m2)
            cntr -= 1

    for link,title,time,name in zip(match_links,match_titles,match_times,match_names):
        team1,team2 = name.split(',')[0].split(' vs ')
        Match.objects.get_or_create(url=link,title=title,time=time,name=name,team1=team1,team2=team2)