import matplotlib.pyplot as plt

def drawCoord2D(pos):
    x, y = zip(*pos)
    plt.title("two-dimentional coordinate")
    plt.scatter(x, y)
    plt.show()

