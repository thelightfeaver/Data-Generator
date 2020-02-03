import os
from sys import argv
from DataGenerator import DataGenerator
from Convert import Convert


class Init():
    
    
    def __init__(self,arg):
        
        self.__typefile = ['json','sql','csv']
        self.__typeoption = ['1','2']
        self.__arg = arg[1:]
        
        self.__type =  self.__arg[:1][0] if self.__arg[:1][0] in self.__typefile else ""
        self.__count = self.__arg[-1:][0] if str(self.__arg[-1:][0]) in self.__typeoption else 0 
        self.__options = self.__arg[1:-1] 

        self.Init()

    def Init(self):
        
        print(self.__type)
        print(self.__count)
        print(self.__options)
        # if len(self.__arg) >= 3 :
            
        #     try:
        #         if self.__count and self.__aptions and self.__type:
        #             file = open("data.{}".format(self.__type),"w+")
        #             for i in range(self.__count):
        #                 file.write("231231","\n")
                    
        #     except:
        #         Help
        # else:
        #     Help()
   
    def Help():

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
        print("9:Telephone\n")
        print("Example \nsql 1 2 4 1-100 10")
        
if __name__ == "__main__":
    p = Init(argv)
    