import matplotlib.pyplot as plt


data = [(1.1,2.5),(3.4,1.9),(5.5,4.6),(6.5,3.5),(5,3),(6.6,4.4),(2,2)]


def drawpoint(list):
    for x,y in list:
        print (x,y)
        #plt.scatter(x, y, marker="x", color='r')
        plt.text(x,y, "{}, {}".format(x,y), color='red')


def drawcentral(list):
    cenX = 0
    cenY = 0
    for x,y in list:
        cenX = (cenX + x ) / 2
        cenY = (cenY + y ) / 2

    print('K-Mean is :{}, {}'.format(cenX,cenY))
    plt.scatter(cenX, cenY, marker="*", color='b')
    plt.text(cenX, cenY, "{}, {}".format(x, y), color='blue')

def main():
    drawpoint(data)
    drawcentral(data)
    plt.show()

if __name__ == '__main__':
    main()






