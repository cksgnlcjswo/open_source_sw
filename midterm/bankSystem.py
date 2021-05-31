"""
Banking System version : 1.5.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : main함수의 역할을 하며 계정 생성,삭제, 조회가 가능.
수정 내용 : pythonic-way 적용
"""
import sys
import account,normalAccount,highCreditAccount,accountHandler
import enumClass

print("-----version information-----")
print(sys.version_info)
print(sys.version)
print("-----------------------------")
print()

def switch(key:str) -> int:
    return {'1' : 1, '2' : 2,'3' : 3,
            '4' : 4, '5' : 5,'6' : 6}.get(key, 7) #7은 정의되지 않은 값

handler = accountHandler.AccountHandler()

while True:
    handler.showMenu()
    choice = input("선택:")
    act = switch(choice)

    if act == enumClass.Action.MAKE.value:
        handler.makeAccount()
    elif act == enumClass.Action.DEPOSIT.value:
        handler.depositMoney()
    elif act == enumClass.Action.WITHDRAW.value:    
        handler.withdrawMoney()
    elif act == enumClass.Action.INQUIRE.value:
        handler.showAllAccountInfo()
    elif act == enumClass.Action.REMOVE.value:
        handler.removeAccount()    
    elif act == enumClass.Action.EXIT.value:
        break 
    else:
        print("Illegal selection... choose anothoer option!") 
