# Returns data as dictionary
def formDict(data):
    return {x:data.count(x) for x in data}