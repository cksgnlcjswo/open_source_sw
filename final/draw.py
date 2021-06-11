'''
    description : 그래프 그리는 함수 모음 
    author : 김찬휘
    e-mail : cksgnlcjswoo@naver.com   
'''

import matplotlib.pyplot as plt

def drawCoord2D(pos:list):
    x, y = zip(*pos)
    plt.title("two-dimentional coordinate")
    plt.scatter(x, y)
    plt.show()
    return

def drawCircle2D(pos:list,police:list,r:int):
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
    return

def resultGraph(radius:list,selectedNumber:list):
    plt.plot(radius,selectedNumber)
    plt.xlabel('radius')
    plt.ylabel('number of selected Area')
    plt.title('result graph')
    plt.show()
    return