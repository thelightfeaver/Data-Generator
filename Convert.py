from enum import Enum

class Sign(Enum):
    Sign1 = 0
    Sign2 = 1
    Sign3 = 2
    Sign4 = 3
class Convert():
    




    def __init__(self):
        pass
    
    
    def to_sign(self,data,sign = 0):
        if sign == Sign.Sign1:
            return "'"+data+"'"
        elif sign == Sign.Sign2:
            return "("+data+")"
        elif sign == Sign.Sign3:
            return '"'+data+ '"'
        else:
            return data
            