# Returns players (Bowlers) with data for the match
import methods.bowlersBonusPoints as bpBowlers

def dataToBowlers(bowlersInfo, players):
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
                players[p['pid']]['points'] = players[p['pid']]['points'] + (int(p['wickets']) * 25) + bpBowlers.bowlersBonusPoints(int(p['wickets']), int(p['maidens']), float(p['overs']), float(p['economy'])) + (p['catches'] * 10) + (p['runouts'] * 10)
            except KeyError:
                players[p['pid']]['points'] = (int(p['wickets']) * 25) + bpBowlers.bowlersBonusPoints(int(p['wickets']), int(p['maidens']), float(p['overs']), float(p['economy'])) + (p['catches'] * 10) + (p['runouts'] * 10)

    return players