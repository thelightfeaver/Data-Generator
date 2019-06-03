import os
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
                self.addColumns()
            elif rs == 2:
                self.__type = 2
                self.addColumns()
            elif rs == 3:
                self.__type = 3
                self.addColumns()
            else:
                self.menuMain()
        except:
            print("Write correct")
            os.system("cls")
            self.menuMain()
            

    def addColumns(self):
        print("1-Name Boy")
        print("2-Name Girl")
        print("3-Surname")
        print("4-Country")
        print("5-Values Integer")
        print("6-Email")
        print("7-Product")
        print("8-Telephone")
        print("0-Count")
        print("99-Back")
        try:
            rs = int(input("Select the data:"))
            if rs <= 8 and 8 >= rs:
                self.__column.append(rs)
                self.addColumns()
            elif rs == 0:
                rs = int(input("To type count"))
                self.__count = rs
            elif rs == 99:
                self.menuMain()
            else:
                print("Error")
                self.addColumns()
        except:
            os.system("cls")
            print("Error!")
       
        
       
if __name__ == "__main__":
    p = Init()
    p.menuMain()