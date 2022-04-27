# Returns the bowlers who took the wickets
def innOutBy(innBat):
    outBy = []
    for f in innBat:
        try:
            outBy.append(f.find('span', class_='text-gray').get_text().strip())
        except AttributeError:
            pass
    
    return outBy