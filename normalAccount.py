"""
version : 1.5.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : normalAccount 클래스(account class 자식 클래스)
수정 사항 : pythonic-way 적용
"""

import account

class NormalAccount(account.Account):
    def __init__(self,ID,money,name,rate):
        super().__init__(ID,money,name)
        self.rate = rate
    
    def deposit(self, moeny:int):
        super().deposit(moeny)
        super().deposit(moeny*(self.rate/100.0)) #이자 추가    
        return

    def showAccountInfo(self):
        print("--------------------")
        print("normal type card")
        print("bank account number: {}".format(self.ID))
        print("name: {}".format(self.name))
        print("balance: {}".format(self.balance))
        print("--------------------")
        return