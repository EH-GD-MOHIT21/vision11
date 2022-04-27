# Extract batsman data from the response and returns the information
def getBattingInfo(bat, firstInnCatches, firstInnRunouts, firstInnStumpings, secondInnCatches, secondInnRunouts, secondInnStumpings):
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
                    batsman['name'] = batsman['name'][:batsman['name'].find('(')].strip()
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
                    batsman['out'] = b.find('span', class_='text-gray').get_text().strip()
                    batsman['runsScored'] = b.find('div', class_='cb-col cb-col-8 text-right text-bold').get_text()
                    batsman['balls'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[0].get_text()
                    batsman['fours'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[1].get_text()
                    batsman['sixes'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[2].get_text()
                    batsman['sr'] = b.find_all('div', class_='cb-col cb-col-8 text-right')[3].get_text()
                except AttributeError:
                    pass
        
        if batsman:
            batsmanInfo.append(batsman)
                    
    return batsmanInfo