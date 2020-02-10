from enum import Enum

class Sign(Enum):
    Nothing = 0
    Parentheses = 1
    Quotation = 2
    Comma = 3
class Convert():
    
    def __init__(self):
        pass
      
    def to_sign(self,data,sign):
      
        if sign == Sign.Comma:
            return "'"+data+"'"
        elif sign == Sign.Parentheses:
            return "("+data+")"
        elif sign == Sign.Quotation:
            return '"'+data+ '"'
        elif sign == Sign.Nothing:
            return data
            

    

