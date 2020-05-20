from enum import Enum

class Sign(Enum):
    Nothing = 0
    Parentheses = 1
    Quotation = 2
    Comma = 3

      
def to_sign(data,sign):
    

    """Encapuslate data"""
    if sign == Sign.Comma:
        return "'"+data+"'"
    elif sign == Sign.Parentheses:
        return "("+data+")"
    elif sign == Sign.Quotation:
        return '"'+data+ '"'
    elif sign == Sign.Nothing:
        return data
            



