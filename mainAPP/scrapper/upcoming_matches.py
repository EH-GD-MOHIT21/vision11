#makes a request at cricbuzz per day from celery
import requests
from bs4 import BeautifulSoup
import json
from operator import *


def list_today_matches(URL="https://www.cricbuzz.com/cricket-schedule/upcoming-series/all"):
    matches = requests.get(URL).text
    soup = BeautifulSoup(matches, 'html.parser')

    allmatches = soup.find_all('div',id='all-list')[0]
    todays_match = allmatches.find_all('div',class_='cb-col-100 cb-col')[0]
    match_links = []
    match_titles = []
    match_times = []
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
            cntr += 1

        times = match.find_all('div',class_='cb-col-40 cb-col cb-mtchs-dy-tm cb-adjst-lst')
        for time in times:
            if cntr == 0:
                break
            matchtime = time.find_all('div',class_='cb-font-12 text-gray')[0]
            servertimegmt = matchtime.find_all('span')[0]
            match_times.append(servertimegmt.get_text())
            cntr -= 1
    
    print(match_links)
    print(match_titles)
    print(match_times)