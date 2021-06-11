'''
    description : 오픈 소스 기말 cover set problem 
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com
'''

import fileRead
import draw
import calMath
import heapq
import Check
import sys

pos=[] #위치좌표
setList = [] #i번째 경찰서가 세워지면 커버되는 지역의 set
radius = 5.1 #반지름
heap = [] # 우선순위 큐

#csv파일로부터 읽어오기
pos = fileRead.loadData()

#현재 점들의 위치 좌표 보여주기
draw.drawCoord2D(pos)

#setList[i]는 i번째 점이 커버할 수 있는 점들을 set로 저장하고 있음(자신 포함)
for i in range(len(pos)) :
  tmp = set() 
  for j in range(len(pos)) :
    if calMath.getCoveredCircleArea(pos[i],pos[j],radius) == True: #i점으로 부터 거리 r안에 j점이 들어옴. 
      tmp.add(j)

  setList.append(tmp)

print("setList 구성 완료")

for s in setList:
  heapq.heappush(heap, (-len(s), s))  # set의 개수가 큰 것부터 우선순위를 줄 것.

res = list() # 경찰서를 설치했을 때 커버되는 곳의 set를 포함하는 list
U = set() # 전체 집합(모든 점)을 나타냄

for i in range(len(pos)) :
  U.add(i)

visited = [ False for _ in range(len(pos))] #모든 위치가 방문되었는지 확인할 용도
prevU = U

"""U가 공집합이 되면 모든 곳을 다 커버했다는 의미"""
while len(U) != 0 :
  maxLenSet = heapq.heappop(heap)[1]
  U = set.difference(U,maxLenSet)
  
  #방문한 점은 true
  for s in maxLenSet : 
    visited[s] = True

  if(prevU != U): #변화가 있었다면 결과에 넣음
    res.append(maxLenSet)

  prevU = U

'''모든점을 다 방문했는지?'''
if (Check.visitedAll(visited,len(pos))) :
  print("every area is coverd!")
else:
  sys.exit("all areas are not coverd!")

police=[] # 실제 pos의 인덱스를 담는 리스트

'''res안의 좌표가 setList의 몇번째 인덱스인지 찾으면 그 인덱스가 우리가 찾는 좌표가 됨'''

for s in res:
  for i,tmp in enumerate(setList):
    if tmp == s :
      police.append(pos[i])
      break

print("number of chosen police: ",len(police))

#경찰서 위치를 점으로 찍기
draw.drawCoord2D(police)

#모든점을 포함하는지 그림으로 확인
draw.drawCircle2D(pos,police,radius)


''' 이번에는 반지름에 따른 선택 개수를 보려고함. '''

radius = [ 0.3, 0.5, 0.8, 1.3, 1.9 , 2.5, 2.9, 3.4, 4.1, 4.7, 5.1]
selectedNumber = [] #선택된 개수

for r in radius: #모든 r에 대해서 실행
  
  heap = []
  setList = []

  for i in range(len(pos)) :
    tmp = set() 
    for j in range(len(pos)) :
      if calMath.getCoveredCircleArea(pos[i],pos[j],r) == True: #i점으로 부터 거리 r안에 j점이 들어옴. 
        tmp.add(j)

    setList.append(tmp)


  for s in setList:
    heapq.heappush(heap, (-len(s), s))  # set의 개수가 큰 것부터 우선순위를 줄 것.

  res = list() # 경찰서를 설치했을 때 커버되는 곳의 set를 포함하는 list
  U = set() # 전체 집합(모든 점)을 나타냄

  for i in range(len(pos)) :
    U.add(i)

  visited = [ False for _ in range(len(pos))] #모든 위치가 방문되었는지 확인할 용도
  prevU = U

  while len(U) != 0 :
    maxLenSet = heapq.heappop(heap)[1]
    U = set.difference(U,maxLenSet)
  
  #방문한 점은 true
    for s in maxLenSet : 
      visited[s] = True

    if(prevU != U): #변화가 있었다면 결과에 넣음
      res.append(maxLenSet)

    prevU = U

  '''모든점을 다 방문했는지?'''
  if (Check.visitedAll(visited,len(pos))) :
    print("now r is ",r,"and every area is coverd!")
  else:
    sys.exit("all areas are not coverd!")

  police=[]

  for s in res:
    for i,tmp in enumerate(setList):
      if tmp == s :
        police.append(pos[i])
        break    

  selectedNumber.append(len(police))

draw.resultGraph(radius,selectedNumber)
