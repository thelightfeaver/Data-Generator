import os
from sys import argv
from DataGenerator import DataGenerator as dg , TypeData
import io
from Convert import Convert as co, Sign


class Init():
    
    
    def __init__(self,arg):
        
        self.__data = Data(arg);
        self._dg = dg()
        self._co = co()
        self.__start()

    def __select_op(self,val = None):
        

        return val if type(val).__name__ == 'list' else [val]
    
    def __select_op2(self,val = None):
        return  Sign.Comma if val in Data.Options  else Sign.Nothing

    def __build_data(self):
        cnt = ""
        if self.__data.typefile == 'sql':
           
            for index,val in enumerate(self.__data.options):
                
                if len(self.__data.options) -1> index:
                    cnt+= str(self._co.to_sign(self._dg.choose_data(self.__select_op(val)),self.__select_op2(val))) +","  
                else:
                    cnt+= str(self._co.to_sign(self._dg.choose_data(self.__select_op(val)),self.__select_op2(val))) 

            return self._co.to_sign(cnt,Sign.Parentheses)
       

    def __build_file(self):

        if self.__data.typefile == 'sql':
            
            file = open('result.sql','w')
            for _ in range(0,self.__data.count):
                
                if self.__data.count -1 > _:
                    file.write(self.__build_data()+",\n")
                else:
                    file.write(self.__build_data())

            file.close()

    def __start(self):
       
        if self.__data.ready:
            try:
                self.__build_file()          
            except Exception as e:
                # print(e.args)
                self.__help()
        else:
            self.__help()
        
    def __help(self):

        print("*****************************************")
        print("*                                       *")
        print("*            Data Generator X1000       *")
        print("*                                       *")
        print("*****************************************")
        print("Note: File name can UPPER and lower!")
        print("Always the item last'll be acount records!")
        print("SQL")
        print("CVS")
        print("JSON")
        print("Options\n")
        print("1:Man Name")
        print("2:Woman Name")
        print("3:Surname")
        print("4:Country")
        print("?-?:Values Integer")
        print("6:Email")
        print("7:Product")
        print("8:Telephone\n")
        print("Example \nsql 1 2 4 1-100 10")
        
class Data():

    Files = ['json','sql','csv']
    Options = ['1','2','3','4','6','7','8']

    def __init__(self,arg = []):

        # init value
        self.__arg = arg[1:]

        # settings
        self.__typefile = ['json','sql','csv']
        self.__typeoption = ['1','2','3','4','6','7','8']
        
        # propertions
        self.typefile =  self.__get_typefile()
        self.count = self.__get_count()
        self.options = self.__get_options()
        self.ready= self.__validate()
    def __get_options(self):
        processdata = self.__arg[1:-1]
        self.__process_taginteger(dt=processdata)
        return processdata if len(processdata)  > 0 else False
    def __get_count(self):
        return int(list(filter(lambda x:self.__arg[-1:][0] is x,self.__arg))[0])
    def __get_typefile(self):
        return self.__arg[:1][0] if self.__arg[:1][0] in self.__typefile else False
    def __process_taginteger(self,dt = []):

        for index,i in enumerate(dt):
            fnt = []
            if i.find('-') and len(i.split('-')) == 2:
                fnt = ['-']+ i.split("-")
                dt[index] = fnt
                 
    def __validate(self):
        
        if bool(self.typefile) and bool(self.count) and bool(self.options) : 
            return True
        else:
            return False


if __name__ == "__main__":
    p = Init(argv)
    