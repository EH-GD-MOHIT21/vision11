from mainAPP.models import Player,UserTeam

def follow_base_rules(player_ids,data,players):
    # total 11 players and frontend data should equalent to backend data
    if len(data.keys()) != 11:
        return False

    for index,id in enumerate(player_ids):
        if data[id][3] != players[index].player_points or data[id][2]!= players[index].player_type or data[id][0]!=players[index].player_name:
            return False
    
    return True


def contain_required_batsman(players):
    ### batsman 3-6
    batsmans = 0
    for player in players:
        if player.player_type == 'BATSMAN':
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
    pass



def finalize_team(data):
    '''
        data is dictionary contains 
    '''
    data = {
        8842:[
            'player_name',
            'player_pic',
            'player_role',
            'player_credit',
            ],
        44654:[
            'player_name',
            'player_pic',
            'player_role',
            'player_credit',
            ]
    }

    player_ids = data.keys()

    try:
        original_players = [Player.objects.get(pid=id) for id in player_ids]
    except:
        return

    if not follow_base_rules(player_ids,data,original_players):
        return

    if not contain_required_batsman(data) or not contain_required_bowler(data) or not contain_required_wicket_keeper(data) or not contain_required_all_rounders(data):
        return

    if not validate_credits(original_players):
        return

    if not validate_captains(data):
        return

    # create object of userTeam
    

