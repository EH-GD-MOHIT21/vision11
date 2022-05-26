class InvalidWinnerStringParser(Exception):
    def __init__(self,message="Should be a valid parsing string each line consist of type start-end:stack%"):
        self.message = message
        super().__init__(self.message)



class InvalidWinnerListParser(Exception):
    def __init__(self,message="Should be a valid parsing list each element represents a players winning credits"):
        self.message = message
        super().__init__(self.message)