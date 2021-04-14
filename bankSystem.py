from enum import Enum
class Account:
    def __init__(self, ID, money, name):
        self.ID = ID #bank number
        self.balance = money #left money
        self.name = name 

    def getID(self):
        return self.ID

    def deposit(self, money):
        self.balance += money

    def withdraw(self,money):
        if(self.balance < money): 
            return 0

        self.balance -= money
        return money        

    def showAccountInfo(self):
        print("bank account number:"+self.ID)
        print("name:" + self.name)
        print("balance:" + str(self.balance))
        return

class Action(Enum):
    MAKE = 1
    DEPOSIT = 2
    WITHDRAW = 3
    INQUIRE = 4
    EXIT = 5

def switch(key):
    return {'1' : 1, '2' : 2,'3' : 3,
            '4' : 4, '5' : 5}.get(key, 6) #6은 정의되지 않은 값

class AccountHandler:
    def __init__(self):
        self.accNum = 0
        self.accList = []

    def showMenu(self):
        print("-----menu-----")
        print("1. create account")
        print("2. deposit")
        print("3. withdraw")
        print("4. show all account information")
        print("5. program exit")     
        return
    
    def makeAccount(self):
        print("[making bank account]")
        print("bank account number:",end='')
        id = input()   
        print("name:",end='')
        name = input()
        print("money:",end='')
        balance = int(input())

        print()
        self.accList.append(Account(id,balance,name))
        self.accNum+=1
        return
    
    def depositMoney(self):
        print("[deposit money]")
        print("account number :",end='')
        id = input()
        print("how many :",end='')
        money = int(input())

        for i in range(0,self.accNum):
            if(self.accList[i].getID() == id):
                self.accList[i].deposit(money)
                print("deposit successed!")
                return

        print("invalid account number")
        return

    def withdrawMoney(self):
        print("[withdraw money]")
        print("account number:",end='')
        id = input()
        print("how much money you want to withdraw:",end='')
        money = int(input())

        for i in range(0,self.accNum):
            if(self.accList[i].getID() == id):
                if(self.accList[i].withdraw(money) == 0): 
                    print("no money left")
                    return

                print("withdraw successed!")
                return

    def showAllAccountInfo(self):
        for i in range(0,self.accNum):
            self.accList[i].showAccountInfo()
            print()
        return    

    def __del__(self):
        for i in range(0,self.accNum):
            self.accList.pop()
        return

handler = AccountHandler()

while True:
    handler.showMenu()
    choice = input("선택:")
    act = switch(choice)

    if act == Action.MAKE.value:
        handler.makeAccount()
    elif act == Action.DEPOSIT.value:
        handler.depositMoney()
    elif act == Action.WITHDRAW.value:    
        handler.withdrawMoney()
    elif act == Action.INQUIRE.value:
        handler.showAllAccountInfo()
    elif act == Action.EXIT.value:
        break    
    else:
        print("Illegal selection... choose anothoer option!") 
