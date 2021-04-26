"""
version : 1.5.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : highCreditAccount 클래스(normalAccount class 자식 클래스).
수정사항 pythonic-way 적용
"""

import normalAccount
import account

def switch(key):
    return {9 : 'A', 7 : 'B',5 : 'C',
            3 : 'D', 1 : 'E'}.get(key, "not_defined") #6은 정의되지 않은 값

class HighLevelAccount(normalAccount.NormalAccount):
    def __init__(self,ID,money,name,rate,specialRate):
        super().__init__(ID,money,name,rate)
        self.specialRate = specialRate

    def deposit(self,money:int):
        super().deposit(money)
        super().deposit(money * (self.specialRate/100.0)) #특별 이자
        return

    def showAccountInfo(self):
        print("--------------------")
        print("special card")
        level = switch(self.specialRate)
        
        if level == "not_defined":
            print("error!")
            return
            
        print("credit revel : {}".format(level))
        print("bank account number: {}".format(self.ID))
        print("name: {}".format(self.name))
        print("balance: {}".format(self.balance))
        print("--------------------")
        return