"""
version 1.3.0
작성자 : 김찬휘
이메일 : cksgnlcjswoo@naver.com
description : enumClass 모음
"""

from enum import Enum

# 프로그램 선택 메뉴
class Action(Enum): 
    MAKE = 1
    DEPOSIT = 2
    WITHDRAW = 3
    INQUIRE = 4
    EXIT = 5

# 선택 메뉴
class Credit(Enum):
    LEVEL_A = 1
    LEVEL_B = 3
    LEVEL_C = 5
    LEVEL_D = 7
    LEVEL_E = 9

# 계좌 종류
class Card(Enum):
    NORMAL = 1 # 일반 카드
    CREDIT = 2 # 신용 카드