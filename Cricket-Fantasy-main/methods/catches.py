# Returns the players who took catches
def catches(battingInfo):
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
        if 'run out' not in b and 'lbw' not in b and 'and' not in b:
            catchesTakenBy.append(b)
            
    catchesTakenBy = [x for x in catchesTakenBy if x != '']
    catchesTakenBy = [x for x in catchesTakenBy if len(x) > 1]
    catchesTakenBy = [x.replace('(sub)', '') for x in catchesTakenBy]

    return catchesTakenBy