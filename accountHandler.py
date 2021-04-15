"""
version 1.3.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : accountHandler 클래스 선언이 명시되어있다.
"""

import normalAccount,highCreditAccount,account
import enumClass 

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

        if(kind == enumClass.Card.NORMAL.value):
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

        self.accList.append(normalAccount.NormalAccount(id,money,name,interate))
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
 
        self.accList.append(highCreditAccount.HighLevelAccount(id,money,name,interate,level))
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

        print("invalid account number")

    def showAllAccountInfo(self):
        for i in range(0,self.accNum):
            self.accList[i].showAccountInfo()
            print()
        return    

    def __del__(self):
        for i in range(0,self.accNum):
            self.accList.pop()
        return