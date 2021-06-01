'''
    description : 오픈 소스 기말 cover set problem
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com
'''

import fileRead
import draw
import calMath
import heapq

pos=[] #위치좌표
setList = [] #i번째 경찰서가 세워지면 커버되는 지역의 set
radius = 1 #반지름
heap = [] # 우선순위 큐

pos = fileRead.loadData()

#현재 점들의 위치 좌표 보여주기
draw.drawCoord2D(pos)

for i in range(len(pos)) :
  tmp = set() 
  for j in range(len(pos)) :
    if calMath.getCoveredCircleArea(pos[i],pos[j],radius) == True: #i점으로 부터 거리 r안에 j점이 들어옴. 
      tmp.add(j)

  setList.append(tmp)

print("set 구성 완료")
'''
for s in setList:
  heapq.heappush(heap, (-len(s), s))  # set의 개수가 큰 것부터 우선순위를 줄 것(그리디).

res = list() # 경찰서를 설치했을 때 커버되는 곳의 set를 포함하는 list
U = set() # 전체 집합을 나타냄

for i in range(len(pos)) :
  U.add(i)

prevU = U

"""U가 공집합이 되면 모든 곳을 다 커버했다는 의미"""
while len(U) :
    maxLenSet = heapq.heappop(heap)[1]
    U = set.difference(U,maxLenSet)
    
    if(prevU != U):
      res.append(maxLenSet)

    prevU = U

print(res)

police=[] # 실제 pos의 인덱스를 담는 리스트
'''

'''setList의 원소와 res의 원소가 같은 지점이 우리가 얻고자 하는 지점의 좌표임'''
'''
for s in res:
  for i,tmp in enumerate(setList):
    if tmp == s :
      police.append(pos[i])
      break

print(police)
print(len(police))

x, y = zip(*police)
plt.scatter(x, y)
plt.show()

import matplotlib.pyplot as plt

figure, axes = plt.subplots()

plt.axis([-15,15,-15,15])
for coord in police:
  draw_circle = plt.Circle((coord[0], coord[1]), r, fill = False)
  plt.gcf().gca().add_artist(draw_circle)

plt.title('coverage of each result')
axes.set_aspect(1)
plt.show()
'''