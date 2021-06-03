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

def drawCircle2D(pos,police,r):
    figure, axes = plt.subplots()

    plt.axis([-15,15,-15,15])

    for point in pos:
        plt.scatter(point[0],point[1])

    for coord in police:
        draw_circle = plt.Circle((coord[0], coord[1]), r, fill = False)
        plt.scatter(coord[0],coord[1])
        plt.gcf().gca().add_artist(draw_circle)

    plt.title('coverage of each result')
    axes.set_aspect(1)
    plt.show()
