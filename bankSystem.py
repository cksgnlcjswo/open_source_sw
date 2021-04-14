"""
Banking System version 1.1.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
버전 업 내용 : 이자율, 신용등급, 카드 종류 추가
"""

from enum import Enum

class Action(Enum): 
    MAKE = 1
    DEPOSIT = 2
    WITHDRAW = 3
    INQUIRE = 4
    EXIT = 5

class Credit(Enum): #신용등급
    LEVEL_A = 1
    LEVEL_B = 3
    LEVEL_C = 5
    LEVEL_D = 7
    LEVEL_E = 9

class Card(Enum):
    NORMAL = 1 #일반 카드
    CREDIT = 2 #신용 카드

def switch(key):
    return {'1' : 1, '2' : 2,'3' : 3,
            '4' : 4, '5' : 5}.get(key, 6) #6은 정의되지 않은 값

"""
class_name : Account
description : 계좌 정보를 나타내는 클래스 모든 계좌 정보의 부모 클래스가 된다.
"""

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
"""
class_name : normalAccount
description : 일반 계좌
"""

class NormalAccount(Account):
    def __init__(self,ID,money,name,rate):
        super().__init__(ID,money,name)
        self.rate = rate
    
    def deposit(self, moeny):
        super().deposit(moeny)
        super().deposit(moeny*(self.rate/100.0)) #이자 추가    
        return

    def showAccountInfo(self):
        print("normal type card")
        print("bank account number:",self.ID)
        print("name:", self.name)
        print("balance:" + str(self.balance))
        return

"""
class_name:HighLevelAccount
description:높은 신용등급을 가진 계좌
"""
class HighLevelAccount(NormalAccount):
    def __init__(self,ID,money,name,rate,specialRate):
        super().__init__(ID,money,name,rate)
        self.specialRate = specialRate

    def deposit(self,money):
        super().deposit(money)
        Account.deposit(money * (self.specialRate/100.0)) #특별 이자
        return

    def showAccountInfo(self):
        print("special card")
        print("bank account number:",self.ID)
        print("name:", self.name)
        print("balance:", str(self.balance))
        return

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
        print("choose card type.")
        print("1. normal type     2. credit card")
        print("선택:",end='')
        kind = int(input())

        if(kind == Card.NORMAL.value):
            self.makeNormalAccount()
        else:
            self.makeCreditAccount()    
        
        return
    
    def makeNormalAccount(self):
        print("making normal type card...")
        print("accout number : ",end='')
        id = input()
        print("name : ",end='')
        name = input()
        print("money : ",end='')
        money = int(input())
        print("interate : ",end='')
        interate = int(input())
        print()

        self.accList.append(NormalAccount(id,money,name,interate))
        self.accNum += 1
        return

    def makeCreditAccount(self):
        print("making credit card type...")
        print("accout number : ",end='')
        id = input()
        print("name : ",end='')
        name = input()
        print("money : ",end='')
        money = int(input())
        print("interate : ",end='')
        interate = int(input())
        print("credit level number(1등급 : A, 3등급 : B, 5등급 : C, 7등급 : D, 9등급 : E) : ",end='')
        level = int(input())
        print()
 
        self.accList.append(HighLevelAccount(id,money,name,interate,level))
        self.accNum += 1
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

"""
method name: switch
return type : int
parameter: str
문자열로 된 숫자를 int형의 숫자로 변환시켜주는 함수
"""

def switch(key):
    return {'1' : 1, '2' : 2,'3' : 3,
            '4' : 4, '5' : 5}.get(key, 6) #6은 정의되지 않은 값

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
