class InvalidCurrencyType(Exception):
    def __init__(self,message="User Can Switch Currency Only Once that on age verification"):
        self.message = message
        super().__init__(self.message)