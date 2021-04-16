"""
version 1.3.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : normalAccount 클래스 선언이 명시되어있다.
"""

import account

class NormalAccount(account.Account):
    def __init__(self,ID,money,name,rate):
        super().__init__(ID,money,name)
        self.rate = rate
    
    def deposit(self, moeny):
        super().deposit(moeny)
        super().deposit(moeny*(self.rate/100.0)) #이자 추가    
        return

    def showAccountInfo(self):
        print("--------------------")
        print("normal type card")
        print("bank account number:",self.ID)
        print("name:", self.name)
        print("balance:", self.balance)
        print("--------------------")
        return