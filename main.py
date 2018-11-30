from graphics import *
from allotmentGarden import *
import random as r

# each garden with units width, height
gardens1={
0 : [15, 25],\
1 : [30, 15],\
2 : [25, 15],\
3 : [20, 25]
    }
gardens2={
0 : [3, 6],\
1 : [2, 2],\
2 : [3, 1],\
3 : [4, 4],\
4 : [4, 4]
    }

gardens3={
0 : [4, 4],\
1 : [3, 2],\
2 : [1, 6],\
3 : [2, 5],\
4 : [5, 3]
    }

gardens4={
0 : [25, 5],\
1 : [4, 3],\
2 : [1 ,1]
}
gardens5={
0 : [4, 4],\
1 : [3, 2],\
2 : [1, 6],\
3 : [2, 5],\
4 : [5, 3],\
5: [3,6]
    }
gardens6={}

def main(gardens, scalingFactor=1):
    win = GraphWin("Allotment Garden", 1000, 1000)
    win.setBackground(color_rgb(255,255,255))

    ## RECTANGLE
    result=fillParts(gardens, {})
    coords=arrangeWithCoords(gardens, result)
    startCoords = coords[0]
    endCoords = coords[1]
    for y in range(len(startCoords)):
        for x in range(len(startCoords[y])):
            rect = Rectangle(Point(startCoords[y][x][0]*scalingFactor, startCoords[y][x][1]*scalingFactor)\
            ,Point(endCoords[y][x][0]*scalingFactor, endCoords[y][x][1]*scalingFactor))
            rect.setOutline(color_rgb(0, 0, 0))
            rect.setFill(color_rgb(r.randint(0,255), r.randint(0,255), r.randint(0,255)))
            rect.draw(win)
    ## ------------------------------------------ ##
    win.getMouse()
    win.close()
main(gardens1, 30)
