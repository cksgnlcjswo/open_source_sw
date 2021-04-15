"""
version 1.3.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : Account 클래스 선언이 명시되어있다.
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
        print("balance:",self.balance)
        return