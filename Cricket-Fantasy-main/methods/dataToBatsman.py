# Returns players (Batsmans) with data for the match
import methods.batsmanBonusPoints as bpBatsman

def dataToBatsman(batsmanInfo, players):
    for p in batsmanInfo:
        if p['pid'] in players:
            players[p['pid']]['pid'] = p['pid']
            players[p['pid']]['name'] = p['name']
            try:
                players[p['pid']]['runsScored'] = p['runsScored']
                players[p['pid']]['out'] = False if p['out'] == 'not out' else True
                players[p['pid']]['ballsFaced'] = p['balls']
                players[p['pid']]['fours'] = p['fours']
                players[p['pid']]['sixes'] = p['sixes']
                players[p['pid']]['strikeRate'] = p['sr']
                players[p['pid']]['catches'] = p['catches']
                players[p['pid']]['runouts'] = p['runouts']
                players[p['pid']]['stumpings'] = p['stumpings']
                
                players[p['pid']]['points'] = int(p['runsScored']) + int(p['fours']) + (int(p['sixes']) * 2) + bpBatsman.batsmanBonusPoints(int(p['runsScored']), p['out'], int(p['balls']), float(p['sr'])) + (p['catches'] * 10) + (p['runouts'] * 10) + (p['stumpings'] * 10)
            except KeyError:
                pass
    
    return players