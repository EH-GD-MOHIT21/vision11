#makes a request at cricbuzz per day from celery
import requests
from bs4 import BeautifulSoup
from operator import *
from mainAPP.models import Match
from datetime import datetime,timezone


def parseDate(date):
    date = date.split(' ')
    d = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
    return int(date[3]),int(date[2]),int(d[date[1].lower()])


def list_today_matches(URL="https://www.cricbuzz.com/cricket-schedule/upcoming-series/all"):

    matches = requests.get(URL).text
    soup = BeautifulSoup(matches, 'html.parser')

    allmatches = soup.find_all('div',id='all-list')[0]
    BASE_URL = 'https://www.cricbuzz.com'

    index = 0
    for perdaymatches in allmatches:
        if perdaymatches==' ':
            continue
        date = allmatches.find_all('div',class_='cb-lv-grn-strip text-bold')
        match_links = []
        match_titles = []
        match_names = []
        match_times = []
        for match in perdaymatches:
            soup = BeautifulSoup(str(match), 'html.parser')
            upcoming_matches = soup.find_all('div',class_='cb-ovr-flo cb-col-60 cb-col cb-mtchs-dy-vnu cb-adjst-lst')
            if upcoming_matches:
                cntr = 0
                for matches in upcoming_matches:
                    dummy_links = matches.find_all('a')
                    for dummy_link in dummy_links:
                        link = dummy_link['href']
                        useful_link = BASE_URL+link.replace('live-cricket-scores','live-cricket-scorecard')
                        match_links.append(useful_link)
                        match_titles.append(dummy_link['title'])
                        match_names.append(dummy_link.get_text())
                        cntr += 1
                        
            upcoming_matches_time = soup.find_all('div',class_='cb-col-40 cb-col cb-mtchs-dy-tm cb-adjst-lst')
            
            if upcoming_matches_time:
                for time in upcoming_matches_time:
                    if cntr == 0:
                        break
                    matchtime = time.find_all('div',class_='cb-font-12 text-gray')[0]
                    servertimegmt = matchtime.find_all('span')[0]
                    m2 = datetime.strptime(servertimegmt.get_text(), '%I:%M %p')
                    today = datetime.today()
                    year,day,month = parseDate(date[index].text)
                    m2 = m2.replace(year=year,month=month,day=day,tzinfo=timezone.utc)
                    match_times.append(m2)
                    cntr -= 1
        
        index += 1
        
        for link,title,time,name in zip(match_links,match_titles,match_times,match_names):
            if 'day ' in title or 'Day ' in title or 'test ' in title:
                continue
            team1,team2 = name.split(',')[0].split(' vs ')
            Match.objects.get_or_create(url=link,title=title,time=time,name=name,team1=team1,team2=team2)
        