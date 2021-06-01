'''
    description : 그래프 그리는 메소드 모음 
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com   
'''

import matplotlib.pyplot as plt

def drawCoord2D(pos):
    x, y = zip(*pos)
    plt.title("two-dimentional coordinate")
    plt.scatter(x, y)
    plt.show()

