# Extract bowler data from the response and returns the information
def getBowlingInfo(bowl, firstInnCatches, firstInnRunouts, secondInnCatches, secondInnRunouts):
    bowlerInfo = []
    for b in bowl:
        bowler = {}
        name = b.find('a', class_='cb-text-link')
        if name:
            pid = name['href'][10:]
            bowler['pid'] = str(pid[:pid.find('/')])
            bowler['name'] = str(name.get_text().strip())
            if '(' in bowler['name']:
                bowler['name'] = bowler['name'][:bowler['name'].find('(')].strip()
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

            bowler['overs'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[0].get_text()
            bowler['maidens'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[1].get_text()
            bowler['runsGiven'] = b.find_all('div', class_='cb-col cb-col-10 text-right')[0].get_text()
            bowler['wickets'] = b.find('div', class_='cb-col cb-col-8 text-right text-bold').get_text()
            bowler['no_balls'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[2].get_text()
            bowler['wides'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[3].get_text()
            bowler['economy'] = b.find_all('div', class_='cb-col cb-col-10 text-right')[1].get_text()
        
        if bowler:
            bowlerInfo.append(bowler)

    return bowlerInfo