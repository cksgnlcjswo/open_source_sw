"""
version : 1.5.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : account 클래스 
수정사항 : pythonic-way 적용
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
        print("bank account number:{}".format(self.ID))
        print("name:{}".format(self.name))
        print("balance:{}".format(self.balance))
        return