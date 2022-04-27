# Returns the players who effected runouts
def runouts(battingInfo):
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
            runoutsDoneBy.append(((x.split('(')[1]).split('/')[1]).split(')')[0])
        except IndexError:
            runoutsDoneBy.append((x.split('(')[1]).split(')')[0])
    runoutsDoneBy = [x for x in runoutsDoneBy if ')' not in x]

    return runoutsDoneBy