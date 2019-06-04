class Convert():
    def __init__(self):
        self.__rs = ""
    def marks(self,data):
        self.__rs = "'"+data+"'"
        return self.__rs
    def paratheis(self,data):
        self.__rs = "("+data+")"
        return self.__rs
    def marksDouble(self,data):
        self.__rs = '"'+data+ '"'
        return self.__rs
