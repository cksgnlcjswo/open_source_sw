'''
    description : 특정 조건이 맞지 않으면 프로그램 종료
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com
'''

'''방문 안한 점이 1개라도 있을 시 False 리턴'''
def visitedAll(visited,size):
    for i in range(size):
        if visited[i] == False:
            print(i,"is not visited!")
            return False

    return True        