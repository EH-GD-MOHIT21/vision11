import requests
from bs4 import BeautifulSoup
import json
from operator import *
import os
from mainAPP.models import Player,Match,PlayersMatchData


def catches(battingInfo):
    '''
    This method takes battingInfo as required parameter and returns
    list of data related to catches taken or an empty list.
    '''
    outInfo = []
    for p in battingInfo:
        if p != 'not out':
            outInfo.append(p)

    removedC = []
    for o in outInfo:
        try:
            removedC.append(o.split('c ')[1])
        except IndexError:
            removedC.append(o.split('c ')[0])

    removedB = []
    for c in removedC:
        removedB.append(c.split('b ')[0])
    removedB = [b.strip(' ') for b in removedB]

    catchesTakenBy = []
    for b in removedB:
        if 'run out' not in b:
            catchesTakenBy.append(b)

    catchesTakenBy = [x for x in catchesTakenBy if x != '']
    catchesTakenBy = [x for x in catchesTakenBy if len(x) > 1]
    catchesTakenBy = [x.replace('(sub)', '') for x in catchesTakenBy]

    return catchesTakenBy


def runouts(battingInfo):
    '''
    This method takes battingInfo as required parameter and returns
    list of data related to runouts or an empty list.
    '''
    outInfo = []
    for p in battingInfo:
        if p != 'not out':
            outInfo.append(p)

    removedC = []
    for o in outInfo:
        try:
            removedC.append(o.split('c ')[1])
        except IndexError:
            removedC.append(o.split('c ')[0])

    removedB = []
    for c in removedC:
        removedB.append(c.split('b ')[0])
    removedB = [b.strip(' ') for b in removedB]

    r = []
    for b in removedB:
        if 'run out' in b and 'sub' not in b:
            r.append(b)

    runoutsDoneBy = []
    for x in r:
        try:
            runoutsDoneBy.append((x.split('(')[1]).split('/')[0])
            runoutsDoneBy.append(
                ((x.split('(')[1]).split('/')[1]).split(')')[0])
        except IndexError:
            runoutsDoneBy.append((x.split('(')[1]).split(')')[0])
    runoutsDoneBy = [x for x in runoutsDoneBy if ')' not in x]

    return runoutsDoneBy


def stumpings(battingInfo):
    '''
    This method takes battingInfo as required parameter and returns
    list of data related to stumping or an empty list.
    '''
    stumpingInfo = []
    for p in battingInfo:
        if p != 'not out' and p.startswith('st'):
            stumpingInfo.append(p)

    stumpingsDoneBy = []
    for s in stumpingInfo:
        stumpingsDoneBy.append(s.split('st ')[1].split(' b')[0])

    return stumpingsDoneBy


def innOutBy(innBat):
    '''
    This method takes innBat as required parameter and returns
    list of data related to wicket taken or an empty list.
    '''
    outBy = []
    for f in innBat:
        try:
            outBy.append(f.find('span', class_='text-gray').get_text().strip())
        except AttributeError:
            pass

    return outBy


def getBattingInfo(bat, firstInnCatches, secondInnCatches, firstInnRunouts, secondInnRunouts, firstInnStumpings, secondInnStumpings):
    '''
        This method is used in order to find detail of each batsman
        and their contribution in order to game.
        returns a list of all batsman in form of batsman template.
    '''
    batsmanInfo = []
    remove = 'Did not Bat'
    for b in bat:
        if remove not in b.get_text():
            batsman = {}
            name = b.find('a', class_='cb-text-link')
            if name:
                pid = name['href'][10:]
                batsman['pid'] = str(pid[:pid.find('/')])
                batsman['name'] = str(name.get_text().strip())
                if '(' in batsman['name']:
                    batsman['name'] = batsman['name'][:batsman['name'].find(
                        '(')].strip()
                batsman['catches'] = 0
                batsman['runouts'] = 0
                batsman['stumpings'] = 0

                for key in firstInnCatches.keys():
                    if key in batsman['name']:
                        batsman['catches'] = firstInnCatches[key]
                for key in secondInnCatches.keys():
                    if key in batsman['name']:
                        batsman['catches'] = secondInnCatches[key]
                for key in firstInnRunouts.keys():
                    if key in batsman['name']:
                        batsman['runouts'] = firstInnRunouts[key]
                for key in secondInnRunouts.keys():
                    if key in batsman['name']:
                        batsman['runouts'] = secondInnRunouts[key]
                for key in firstInnStumpings.keys():
                    if key in batsman['name']:
                        batsman['stumpings'] = firstInnStumpings[key]
                for key in secondInnStumpings.keys():
                    if key in batsman['name']:
                        batsman['stumpings'] = secondInnStumpings[key]
                try:
                    fake_text = b.find(
                        'span', class_='text-gray').get_text().strip()
                    if fake_text == 'batting':
                        batsman['out'] = 'not out'
                    else:
                        batsman['out'] = 'out'
                except:
                    batsman['out'] = 'not out'
                try:
                    batsman['runsScored'] = b.find(
                        'div', class_='cb-col cb-col-8 text-right text-bold').get_text()
                except:
                    batsman['runsScored'] = 0
                try:
                    batsman['balls'] = b.find_all(
                        'div', class_='cb-col cb-col-8 text-right')[0].get_text()
                except:
                    batsman['balls'] = 0
                try:
                    batsman['fours'] = b.find_all(
                        'div', class_='cb-col cb-col-8 text-right')[1].get_text()
                except:
                    batsman['fours'] = 0
                try:
                    batsman['sixes'] = b.find_all(
                        'div', class_='cb-col cb-col-8 text-right')[2].get_text()
                except:
                    batsman['sixes'] = 0
                try:
                    batsman['sr'] = b.find_all(
                        'div', class_='cb-col cb-col-8 text-right')[3].get_text()
                except:
                    batsman['sr'] = 0

        if batsman:
            batsmanInfo.append(batsman)

    return batsmanInfo


def getBowlingInfo(bowl, firstInnCatches, secondInnCatches, firstInnRunouts, secondInnRunouts):
    '''
        This method is used in order to find detail of each bowler
        and their contribution in order to game.
        returns a list of all bowler in form of bowler template.
    '''
    bowlerInfo = []
    for b in bowl:
        bowler = {}
        name = b.find('a', class_='cb-text-link')
        if name:
            pid = name['href'][10:]
            bowler['pid'] = str(pid[:pid.find('/')])
            bowler['name'] = str(name.get_text().strip())
            if '(' in bowler['name']:
                bowler['name'] = bowler['name'][:bowler['name'].find(
                    '(')].strip()
            bowler['catches'] = 0
            bowler['runouts'] = 0
            bowler['stumpings'] = 0

            for key in firstInnCatches.keys():
                if key in bowler['name']:
                    bowler['catches'] = firstInnCatches[key]
            for key in secondInnCatches.keys():
                if key in bowler['name']:
                    bowler['catches'] = secondInnCatches[key]
            for key in firstInnRunouts.keys():
                if key in bowler['name']:
                    bowler['runouts'] = firstInnRunouts[key]
            for key in secondInnRunouts.keys():
                if key in bowler['name']:
                    bowler['runouts'] = secondInnRunouts[key]

            bowler['overs'] = b.find_all(
                'div', class_='cb-col cb-col-8 text-right')[0].get_text()
            bowler['maidens'] = b.find_all(
                'div', class_='cb-col cb-col-8 text-right')[1].get_text()
            bowler['runsGiven'] = b.find_all(
                'div', class_='cb-col cb-col-10 text-right')[0].get_text()
            bowler['wickets'] = b.find(
                'div', class_='cb-col cb-col-8 text-right text-bold').get_text()
            bowler['no_balls'] = b.find_all(
                'div', class_='cb-col cb-col-8 text-right')[2].get_text()
            bowler['wides'] = b.find_all(
                'div', class_='cb-col cb-col-8 text-right')[3].get_text()
            bowler['economy'] = b.find_all(
                'div', class_='cb-col cb-col-10 text-right')[1].get_text()

        if bowler:
            bowlerInfo.append(bowler)

    return bowlerInfo


def allPlayers(team, playerTemplate):
    players = {}
    for p in team:
        player = playerTemplate.copy()
        pid = p['href'][10:]
        pid = str(pid[:pid.find('/')])
        players[pid] = player

    return players


def batsmanBonusPoints(runs, out, balls, sRate):
    '''
        This method only calculates the bonus points for
        each batsman in case of good strike rate or an
        acheivement

        returns only bonus points
    '''
    runsPoints = 0
    if runs >= 50 and runs < 100:
        runsPoints = 8
    elif runs >= 100:
        runsPoints = 16
    elif runs == 0 and out != 'not out':
        runsPoints = -2
    else:
        runsPoints = 0

    srPoints = 0
    if balls >= 10:
        if sRate >= 60 and sRate <= 70:
            srPoints = -2
        elif sRate >= 50 and sRate <= 59.99:
            srPoints = -4
        elif sRate < 50:
            srPoints = -6

    return runsPoints + srPoints


def dataToBatsman(batsmanInfo, players):
    '''
        This method calculate the total fantasy score
        of each batsman.
        return list of players in form of player
        template along with new field points.
    '''
    for p in batsmanInfo:
        if p['pid'] in players:
            players[p['pid']]['pid'] = p['pid']
            players[p['pid']]['name'] = p['name']
            players[p['pid']]['runsScored'] = p['runsScored']
            players[p['pid']]['out'] = False if p['out'] == 'not out' else True
            players[p['pid']]['ballsFaced'] = p['balls']
            players[p['pid']]['fours'] = p['fours']
            players[p['pid']]['sixes'] = p['sixes']
            players[p['pid']]['strikeRate'] = p['sr']
            players[p['pid']]['catches'] = p['catches']
            players[p['pid']]['runouts'] = p['runouts']
            players[p['pid']]['stumpings'] = p['stumpings']

            players[p['pid']]['points'] = int(p['runsScored']) + int(p['fours']) + (int(p['sixes']) * 2) + batsmanBonusPoints(int(
                p['runsScored']), p['out'], int(p['balls']), float(p['sr'])) + (p['catches'] * 8) + (p['runouts'] * 8) + (p['stumpings'] * 12)

    return players


def bowlersBonusPoints(wickets, maidens, overs, economy):
    '''
        This method only calculates the bonus
        points for bowler.
        bonus points related to economy or
        acheivements.
    '''
    wicketsPoints = 0
    if wickets == 3:
        wicketsPoints = 8
    elif wickets == 5:
        wicketsPoints = 16

    economyPoints = 0
    if overs >= 2:
        if economy <= 4:
            economyPoints = 6
        elif economy > 4 and economy <= 4.99:
            economyPoints = 4
        elif economy >= 5 and economy <= 6:
            economyPoints = 2
        elif economy >= 9 and economy <= 10:
            economyPoints = -2
        elif economy >= 10.01 and economy <= 11:
            economyPoints = -4
        elif economy > 11:
            economyPoints = -6

    return wicketsPoints + economyPoints + (maidens * 8)


def dataToBowlers(bowlersInfo, players):
    '''
        This method calculate the total fantasy score
        of each bowler.
        return list of players in form of player
        template along with new field points.
    '''
    for p in bowlersInfo:
        if p['pid'] in players:
            players[p['pid']]['pid'] = p['pid']
            players[p['pid']]['name'] = p['name']
            players[p['pid']]['overs'] = p['overs']
            players[p['pid']]['maidens'] = p['maidens']
            players[p['pid']]['runsGiven'] = p['runsGiven']
            players[p['pid']]['wickets'] = p['wickets']
            players[p['pid']]['noBalls'] = p['no_balls']
            players[p['pid']]['wides'] = p['wides']
            players[p['pid']]['economy'] = p['economy']
            players[p['pid']]['catches'] = p['catches']
            players[p['pid']]['runouts'] = p['runouts']

            try:
                players[p['pid']]['points'] = players[p['pid']]['points'] + (int(p['wickets']) * 25) + bowlersBonusPoints(int(
                    p['wickets']), int(p['maidens']), float(p['overs']), float(p['economy'])) + (p['catches'] * 8) + (p['runouts'] * 8)
            except KeyError:
                players[p['pid']]['points'] = (int(p['wickets']) * 25) + bowlersBonusPoints(int(p['wickets']), int(
                    p['maidens']), float(p['overs']), float(p['economy'])) + (p['catches'] * 8) + (p['runouts'] * 8)

    return players










def Update_Live_Score(URL):
    '''
    This method will make a get request to provided
    cricbuzz.com url with livescore board link of the 
    match and generate a json file which contains player's
    fantasy points along with other game details like runs,
    wickets etc.
    '''
    scoreCard = requests.get(URL).text
    soup = BeautifulSoup(scoreCard, 'html.parser')
    first_half_player_data = {}
    second_half_player_data = {}
    playerTemplate = {
        "pid": "0",
        "name": "",
        "runsScored": "0",
        "ballsFaced": "0",
        "fours": "0",
        "sixes": "0",
        "strikeRate": "0",
        "out": False,
        "overs": "0",
        "maidens": "0",
        "runsGiven": "0",
        "wickets": "0",
        "noBalls": "0",
        "wides": "0",
        "economy": "0",
        "catches": 0,
        "runouts": 0,
        "stumpings": 0
    }
    
    for i in range(1,4,2):
        try:
            firstInn = soup.find_all('div', id=f'innings_{i}')[0]
            firstInnBat = firstInn.find_all(
                'div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr')[0]
            firstInnBat = firstInnBat.find_all(
                'div', class_='cb-col cb-col-100 cb-scrd-itms')
            firstInnBowl = firstInn.find_all(
                'div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr')[1]
            firstInnBowl = firstInnBowl.find_all(
                'div', class_='cb-col cb-col-100 cb-scrd-itms')
            firstInnScore = firstInn.find(
                'span', class_='pull-right').get_text().split(' ')[0]
            firstInnTeam = firstInn.find('span').get_text()
            firstInnTeam = firstInnTeam[:firstInnTeam.find(' Innings')]

        except:
            firstInnBat = []
            firstInnBowl = []


        try:
            secondInn = soup.find_all('div', id=f'innings_{i+1}')[0]
            secondInnBat = secondInn.find_all(
                'div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr')[0]
            secondInnBat = secondInnBat.find_all(
                'div', class_='cb-col cb-col-100 cb-scrd-itms')
            secondInnBowl = secondInn.find_all(
                'div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr')[1]
            secondInnBowl = secondInnBowl.find_all(
                'div', class_='cb-col cb-col-100 cb-scrd-itms')
            secondInnScore = secondInn.find(
                'span', class_='pull-right').get_text().split(' ')[0]
            secondInnTeam = secondInn.find('span').get_text()
            secondInnTeam = secondInnTeam[:secondInnTeam.find(' Innings')]

        except:
            secondInnBat = []
            secondInnBowl = []

        try:
            firstInnCatches = catches(innOutBy(firstInnBat))
            firstInnCatches = {x: firstInnCatches.count(x) for x in firstInnCatches}
        except:
            firstInnCatches = {}

        try:
            secondInnCatches = catches(innOutBy(secondInnBat))
            secondInnCatches = {x: secondInnCatches.count(x) for x in secondInnCatches}
        except:
            secondInnCatches = {}

        try:
            firstInnRunouts = runouts(innOutBy(firstInnBat))
            firstInnRunouts = {x: firstInnRunouts.count(x) for x in firstInnRunouts}
        except:
            firstInnRunouts = {}

        try:
            secondInnRunouts = runouts(innOutBy(secondInnBat))
            secondInnRunouts = {x: secondInnRunouts.count(x) for x in secondInnRunouts}
        except:
            secondInnRunouts = {}

        try:
            firstInnStumpings = stumpings(innOutBy(firstInnBat))
            firstInnStumpings = {x: firstInnStumpings.count(
                x) for x in firstInnStumpings}
        except:
            firstInnStumpings = {}

        try:
            secondInnStumpings = stumpings(innOutBy(secondInnBat))
            secondInnStumpings = {x: secondInnStumpings.count(
                x) for x in secondInnStumpings}
        except:
            secondInnStumpings = {}


        firstInnBatInfo = getBattingInfo(firstInnBat, firstInnCatches, secondInnCatches,
                                         firstInnRunouts, secondInnRunouts, firstInnStumpings, secondInnStumpings)
        secondInnBatInfo = getBattingInfo(secondInnBat, firstInnCatches, secondInnCatches,
                                          firstInnRunouts, secondInnRunouts, firstInnStumpings, secondInnStumpings)

        firstInnBowlInfo = getBowlingInfo(
            firstInnBowl, firstInnCatches, secondInnCatches, firstInnRunouts, secondInnRunouts)
        secondInnBowlInfo = getBowlingInfo(
            secondInnBowl, firstInnCatches, secondInnCatches, firstInnRunouts, secondInnRunouts)

        playingXI = soup.find_all('div', class_='cb-col cb-col-100 cb-minfo-tm-nm')
        team = playingXI[1].find_all('a') + playingXI[3].find_all('a')
        players = allPlayers(team, playerTemplate)

        players = dataToBatsman(firstInnBatInfo, players)
        players = dataToBatsman(secondInnBatInfo, players)
        players = dataToBowlers(firstInnBowlInfo, players)
        players = dataToBowlers(secondInnBowlInfo, players)

        if i==1:
            first_half_player_data = dict(players)
        else:
            second_half_player_data = dict(players)
    
    
    # saving the data

    # for 1st inng of both teams
    for player in first_half_player_data.keys():
        data = first_half_player_data[player]
        try:
            pts = data['points']
        except:
            pts = 0
        try:
            match = Match.objects.get(url=URL)
            playerscore = Player.objects.get(pid=int(player))
            try:
                player_dtaa = PlayersMatchData.objects.get(pid=playerscore,match_url=match)
            except:
                player_dtaa = PlayersMatchData.objects.create(pid=playerscore,match_url=match)
            player_dtaa.runsScored=data['runsScored']
            player_dtaa.ballsFaced=data['ballsFaced']
            player_dtaa.fours=data['fours']
            player_dtaa.sixes=data['sixes']
            player_dtaa.strikeRate=data['strikeRate']
            player_dtaa.out=data['out']
            player_dtaa.overs=data['overs']
            player_dtaa.maidens=data['maidens']
            player_dtaa.runsGiven=data['runsGiven']
            player_dtaa.wickets=data['wickets']
            player_dtaa.noBalls=data['noBalls']
            player_dtaa.wides=data['wides']
            player_dtaa.economy=data['economy']
            player_dtaa.catches=data['catches']
            player_dtaa.runouts=data['runouts']
            player_dtaa.stumpings=data['stumpings']
            player_dtaa.points=pts
            player_dtaa.save()
        except Exception as e:
            print(data['out'])
            print(f"error {e} inside updating player. {player} inng 1")


    # inng 2 match data update
    for player in second_half_player_data.keys():
        data = second_half_player_data[player]
        try:
            pts = data['points']
        except:
            pts = 0
        try:
            match = Match.objects.get(url=URL)
            playerscore = Player.objects.get(pid=int(player))
            try:
                player_dtaa = PlayersMatchData.objects.get(pid=playerscore,match_url=match)
            except:
                player_dtaa = PlayersMatchData.objects.create(pid=playerscore,match_url=match)
            player_dtaa.runsScored+=int(data['runsScored'])
            player_dtaa.ballsFaced+=int(data['ballsFaced'])
            player_dtaa.fours+=int(data['fours'])
            player_dtaa.sixes+=int(data['sixes'])
            player_dtaa.strikeRate=max(float(data['strikeRate']),player_dtaa.strikeRate)
            if data['out'] == True:
                # might contain string data['out'] for catch/bowled purpose or a boolean field so this check.
                player_dtaa.out=True
            player_dtaa.overs+=float(data['overs'])
            intpart,floatpart = str(player_dtaa.overs).split('.')
            intpart = str(int(intpart) + int(floatpart)//6)
            floatpart = str(int(floatpart) -  (int(floatpart)//6)*6 )
            player_dtaa.overs = float(intpart+"."+floatpart)
            player_dtaa.maidens+=int(data['maidens'])
            player_dtaa.runsGiven+=int(data['runsGiven'])
            player_dtaa.wickets+=int(data['wickets'])
            player_dtaa.noBalls+=int(data['noBalls'])
            player_dtaa.wides+=int(data['wides'])
            player_dtaa.economy=max(float(data['economy']),player_dtaa.economy)
            player_dtaa.catches+=int(data['catches'])
            player_dtaa.runouts+=int(data['runouts'])
            player_dtaa.stumpings+=int(data['stumpings'])
            player_dtaa.points+=float(pts)
            player_dtaa.save()
        except Exception as e:
            print(data['out'])
            print(f"error {e} inside updating player. {player}")
    