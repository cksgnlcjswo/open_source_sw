'''
    description : 두 점의 거리 게산 및 범위 표현 하는 함수 모음    
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com
'''

from math import sqrt

'''getDistance(pos[i],pos[j]) <= r*r 과 같이 쓸 때 사용'''
def getDistance(a,b):
  dist = (a[0]-b[0])*(a[0]-b[0]) + (a[1] - b[1]) * (a[1] - b[1])
  return dist

'''getDistance(pos[i],pos[j]) <= r과 같이 사용할 때 사용 '''
def getDistance2(a,b):
    dist = (a[0]-b[0])*(a[0]-b[0]) + (a[1] - b[1]) * (a[1] - b[1])
    return sqrt(dist)

'''중심이 pos1이고 반지름이 r인 원 안에 pos2가 있는지 여부'''
def getCoveredCircleArea(pos1, pos2,r):
    if getDistance(pos1,pos2) <= r*r:
        return True
    return False

'''중심이 pos1이고 길이가 2r인 정사각형 안에 pos2가 있는지 여부'''
def getCoveredRecArea(pos1,pos2,r):
    minPosX = pos[0] - r # 정사각형 좌상단 꼭지점
    maxPosY = pos[0] + r # 정사각형 우상단 꼭지점
    minPosY = pos[1] - r # 정사각형 좌하단 꼭지점
    maxPosY = pos[1] + r # 정사각형 우하단 꼭지점
    
    if pos[0] >= minPosX and pos[0] <= maxPosX : #pos[j]의 x좌표가 정사각형 좌우범위 안에
        if pos[1] >= minPosY and pos[1] <= maxPosY : #pos[j]의 y좌표가 정사각형 상하범위 안에
            return True  

    return False        