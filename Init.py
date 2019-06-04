import os
import logging
from DataGenerator import DataGenerator
from Convert import Convert

class Init():

   
    def __init__(self):
        self.__column = []
        self.__type = 0
        self.__count = 0


    def menuMain(self):
        print("1-Sql")
        print("2-CVS")
        print("3-Exit")
        try:
            rs = int(input("Select you option:"))
            if rs == 1:
                self.__type =1
                self.__clear()
                self.addColumns()
            elif rs == 2:
                self.__type = 2
                self.__clear()
                self.addColumns()
            elif rs == 3:
                self.__type = 3
                self.__clear()
            else:
                self.__clear()
                self.menuMain()
        except:
            print("Write correct")
            self.__clear()
            self.menuMain()
            

    def addColumns(self):
        rs = ""
        print("1-Name Boy")
        print("2-Name Girl")
        print("3-Surname")
        print("4-Country")
        print("5-Values Integer")
        print("6-Email")
        print("7-Product")
        print("8-Telephone")
        print("0-Count")
        print("99-Build")
        print("100-Back")
        try:
            rs = int(input("\nSelect the data:"))
            if rs <= 8 and 8 >= rs and rs != 0:
                self.__clear()
                self.__column.append(int(rs))
                self.addColumns()
            elif rs == 0:
                ans = int(input("\nTo type count:"))
                self.__count = ans
                self.addColumns()
            elif rs == 100:
                self.__clear()
                self.menuMain()
            elif rs == 99:
                if len(self.__column) > 0 and self.__count > 0:
                    self.__build()
                else:
                    print("Error")
                    print(len(self.__column) + "" + len(self.__count))
                    self.addColumns()
            else:
                self.__clear()
                print("Error")
                self.addColumns()
        except Exception as e:
            self.__clear()
            print(e)
            self.addColumns()
       
    def __build(self):
        data = []
        cv = Convert()
        for l in range(0,self.__count):
            temp = ""
            valor =0
            for x in self.__column:
                
                if valor == len(self.__column):
                    valor += 1
                    temp += str(self.__selectOption(x))+""
                else:
                    temp += str(self.__selectOption(x))+","
            
            data.append(cv.paratheis(temp))
        
        
        self.__buildFile(data)



    def __selectOption(self,data):
        ans = None
        dg = DataGenerator()
        cv = Convert()
        if data == 1 :
            if self.__type == 1:
                ans = cv.marks(dg.getNameBoy())
        elif data == 2:
            if self.__type == 1:
                ans = cv.marks(dg.getNameGirl())
        elif data == 3:
            if self.__type == 1:
                ans = cv.marks(dg.getSurname())
        elif data == 4:
            if self.__type == 1:
                ans = cv.marks(dg.getCity())
        elif data == 5:
            if self.__type == 1:
                ans = dg.getAge(1,23)
        elif data == 6:
            if self.__type == 1:
                ans = cv.marks(dg.getEmail())
        elif data == 7:
            if self.__type == 1:
                ans = cv.marks(dg.getProduct())
        elif data == 8:
            if self.__type == 1:
                ans = cv.marks(dg.getTelephone())
        return ans
        
    
    def __buildFile(self,data):
        file = open("final.txt",'w')
        for x in data:
            file.write(x+"\n")
        file.close()
        self.__clear()
        self.menuMain()
    

    def __clear(self):
        if os.name == "nt":
            os.system("cls")
        elif os.name =="posix":
            os.system("clear")
    
       
if __name__ == "__main__":
    p = Init()
    p.menuMain()