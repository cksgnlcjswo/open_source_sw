"""
version : 1.5.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : accountHandler 클래스 
수정사항: pythonic-way 적용
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
        print("5. remove account")
        print("6. program exit")     
        return
    
    def makeAccount(self):
        print()
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
        print()
        print("making normal type card...")
        print("accout number : ",end='')
        _id = input()
        print("name : ",end='')
        _name = input()
        print("money : ",end='')
        _money = int(input())
        print("interate(0~10% 사이) : ",end='')
        _interate = int(input())
        print()

        #잘못된 유저 아이디 형식
        if False == self.checkValidAccount(_id,_name,_money,_interate): return
            
        self.accList.append(normalAccount.NormalAccount(_id,_money,_name,_interate))
        self.accNum += 1
        return

    def checkValidAccount(self,id:str, name:str, money:int, interate:int) -> bool:
        #id가 입력되지 않은 경우
        if(len(id) == 0):
            print("id is not defined.")
            return False

        #이름이 입력되지 않은 경우
        if(len(name) == 0):
            print("please input your name")    
            return False

        #돈이 -인경우
        if(money < 0):
            print("money cannot be minus")
            return False

        #이율은 10%를 넘길 수 없다.
        if interate >= 11 or interate < 0 :
            print("interate shoud be in 0~10%")
            return False

        return True    

    def makeCreditAccount(self):
        print("making credit card type...")
        print("accout number : ",end='')
        _id = input()
        print("name : ",end='')
        _name = input()
        print("money : ",end='')
        _money = int(input())
        print("interate(0~10% 사이) : ",end='')
        _interate = int(input())
        print("credit level number(숫자로 입력하세요: Ato9, Bto7, Cto5, Dto3, Eto1) : ",end='')
        _level = int(input())
        print()

        if False == self.checkValidAccount(_id,_name,_money,_interate): return

        #1등급
        if _level == enumClass.Credit.LEVEL_A.value:
            self.accList.append(highCreditAccount.HighLevelAccount(_id,_money,_name,_interate,enumClass.Credit.LEVEL_A.value))
            self.accNum += 1

        #2등급
        elif _level == enumClass.Credit.LEVEL_B.value:
            self.accList.append(highCreditAccount.HighLevelAccount(_id,_money,_name,_interate,enumClass.Credit.LEVEL_B.value))
            self.accNum += 1

        #3등급
        elif _level == enumClass.Credit.LEVEL_C.value:
            self.accList.append(highCreditAccount.HighLevelAccount(_id,_money,_name,_interate,enumClass.Credit.LEVEL_C.value))
            self.accNum += 1

        #4등급
        elif _level == enumClass.Credit.LEVEL_D.value:
            self.accList.append(highCreditAccount.HighLevelAccount(_id,_money,_name,_interate,enumClass.Credit.LEVEL_D.value))
            self.accNum += 1
        
        #5등급
        else :
            self.accList.append(highCreditAccount.HighLevelAccount(_id,_money,_name,_interate,enumClass.Credit.LEVEL_E.value))
            self.accNum += 1

        return

    def depositMoney(self):
        print("[deposit money]")
        print("account number :",end='')
        _id = input()
        print("how many :",end='')
        _money = int(input())

        for i in range(0,self.accNum):
            if(self.accList[i].getID() == _id):
                self.accList[i].deposit(_money)
                print("deposit successed!")
                return

        print("invalid account number")
        return

    def withdrawMoney(self):
        print("[withdraw money]")
        print("account number:",end='')
        _id = input()
        print("how much money you want to withdraw:",end='')
        _money = int(input())

        for i in range(0,self.accNum):
            if(self.accList[i].getID() == _id):
                if(self.accList[i].withdraw(_money) == 0): 
                    print("no money left")
                    return

                print("withdraw successed!")
                return

        print("invalid account number")

    def showAllAccountInfo(self):
        if self.accNum == 0:
            print("no information of any account number... please create id...")
        
        print("you want to see money decreasing order?(Yes or y / No or n):",end='')
        ans = input()

        if ans == 'y':
            tmp = self.accList[:]
            tmp.sort(key = lambda x: x.balance, reverse=True)
            for i, acc in enumerate(tmp,1):
                print("user {}.".format(i))
                acc.showAccountInfo()
                print() 
        else :
            for i, acc in enumerate(self.accList,1):
                print("user {}.".format(i))
                acc.showAccountInfo()
                print()    
            return    

    def removeAccount(self):
        if self.accNum == 0:
            print("there is no account information, please create id....")
            print()
            return

        print("[remove account]")
        print("account number:",end='')
        _id = input()

        for i in range(0,self.accNum):
            if(self.accList[i].getID() == _id):
                self.accList.pop(i)
                self.accNum -= 1 
                print("{} account deleted!".format(id))
                return

        print("invalid account number")
        return

    def __del__(self):
        for _ in range(0,self.accNum):
            self.accList.pop()
        return

