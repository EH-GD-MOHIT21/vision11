# Returns the bonus points for bowlers
def bowlersBonusPoints(wickets, maidens, overs, economy):
    # Bonus points for number of wickets taken
    wicketsPoints = 0
    if wickets == 3:
        wicketsPoints = 10
    elif wickets == 5:
        wicketsPoints = 20
    
    # Bonus points for the economy of the bowler
    economyPoints = 0
    if overs >= 2:
        if economy <= 4:
            economyPoints = 15
        elif economy > 4 and economy <= 4.99:
            economyPoints = 10
        elif economy >= 5 and economy <= 6:
            economyPoints = 5
        elif economy >= 9 and economy <= 10:
            economyPoints = -5
        elif economy >= 10.01 and economy <= 11:
            economyPoints = -10
        elif economy > 11:
            economyPoints = -15

    return wicketsPoints + economyPoints + (maidens * 10)