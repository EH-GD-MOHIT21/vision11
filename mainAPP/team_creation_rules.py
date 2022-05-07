from mainAPP.models import Player,UserTeam


def filter_team_data(data):
    players = {}
    for key in data['players'].keys():
        try:
            players[int(key)] = data['players'][key]
        except:
            pass
    captain = {}
    for key in data['cap_data'].keys():
        try:
            captain[int(key)] = data['cap_data'][key]
            players[int(key)] = data['cap_data'][key]
        except:
            pass
    vice_captain = {}
    for key in data['vice_cap_data'].keys():
        try:
            vice_captain[int(key)] = data['vice_cap_data'][key]
            players[int(key)] = data['vice_cap_data'][key]
        except:
            pass
    return players,captain,vice_captain

def follow_base_rules(player_ids,data,players):
    # total 11 players and frontend data should equalent to backend data
    if len(data.keys()) != 11:
        return False

    for index,id in enumerate(player_ids):
        if data[id][2] != players[index].player_points or data[id][3]!= players[index].player_type or data[id][0]!=players[index].player_name:
            return False
    return True


def contain_required_batsman(players):
    ### batsman 3-6
    batsmans = 0
    for player in players:
        if player.player_type == 'BATSMEN':
            batsmans += 1
    return batsmans in range(3,7) # range searches for n-1



def contain_required_bowler(players):
    ### bowler 3-6
    bowlers = 0
    for player in players:
        if player.player_type == 'BOWLER':
            bowlers += 1
    return bowlers in range(3,7) # range searches for n-1



def contain_required_all_rounders(players):
    ### ar 1-4
    ar = 0
    for player in players:
        if player.player_type == 'ALL ROUNDER':
            ar += 1
    return ar in range(1,5) # range searches for n-1



def contain_required_wicket_keeper(players):
    ### wk 1-4
    wk = 0
    for player in players:
        if player.player_type == 'WICKET KEEPER':
            wk += 1
    return wk in range(1,5) # range searches for n-1



def validate_credits(players):
    total = 0
    for player in players:
        total += player.player_points
    return total <= 100.0



def validate_captains(data):
    return True



def finalize_team(data):
    '''
        data is dictionary contains 
    '''

    player_ids = data.keys()

    try:
        original_players = [Player.objects.get(pid=id) for id in player_ids]
    except:
        return False,'players has modified.'

    if not follow_base_rules(player_ids,data,original_players):
        return False,'base rule broken'

    if not contain_required_batsman(original_players):
        return False, 'required batsman not satisfied.'
    
    if not contain_required_bowler(original_players):
        return False, 'required bowler not satisfied.'

    if not contain_required_wicket_keeper(original_players):
        return False, 'required w/k not satisfied.'

    if not contain_required_all_rounders(original_players):
        return False ,'required A/R not satisfied.'

    if not validate_credits(original_players):
        return False, 'Over limit credits'

    if not validate_captains(data):
        return False, 'Captains not valid'

    return True,None

    # create object of userTeam
    

