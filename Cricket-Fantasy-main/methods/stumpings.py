# Returns players who effected stumpings
def stumpings(battingInfo):
    stumpingInfo = []
    for p in battingInfo:
        if p != 'not out' and p.startswith('st'):
            stumpingInfo.append(p)
    
    stumpingsDoneBy = []
    for s in stumpingInfo:
        stumpingsDoneBy.append(s.split('st ')[1].split(' b')[0])
    
    return stumpingsDoneBy