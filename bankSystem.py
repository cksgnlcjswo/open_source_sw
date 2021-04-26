"""
Banking System version 1.4.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
버전 업 내용 : 삭제 기능 추가
"""
import account,normalAccount,highCreditAccount,accountHandler
import enumClass

def switch(key):
    return {'1' : 1, '2' : 2,'3' : 3,
            '4' : 4, '5' : 5,'6' : 6}.get(key, 7) #6은 정의되지 않은 값

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
