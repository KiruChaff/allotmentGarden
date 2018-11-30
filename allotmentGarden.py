import sys
import copy as c
from timeThis import *
counter = int(0)
## return area
def getArea(width, height):
    return width*height

## arranges an set of gardens in the most optimal way
def arrange(gardens, tempGardens):
    if tempGardens[0][0]<0: return sys.maxsize, sys.maxsize
    totalWidth = int()
    totalHeight = int()
    matrix = [list() for row in range(len(tempGardens))]
    # for each row and column get the measure where a garden can be placed
    for row in range(len(tempGardens)):
        width=0
        for col in range(len(tempGardens[row])):
            height=0
            startHeight=0
            addedWidth=width+gardens[tempGardens[row][col]][0]
            if row>0:
                for prevRow in range(row-1, -1, -1):
                    aboveCol=0
                    ##gets upper boundry
                    if addedWidth>matrix[prevRow][len(matrix[prevRow])-1][0]:
                        aboveCol = len(matrix[prevRow])-1
                    else:
                        while addedWidth>matrix[prevRow][aboveCol][0] and  aboveCol<len(matrix[prevRow])-1:
                            aboveCol+=1
                    ## gets lower boudry + sets starting height
                    while width<matrix[prevRow][aboveCol][0] and aboveCol>0:
                        aboveHeight=matrix[prevRow][aboveCol][1]
                        startHeight = aboveHeight if(aboveHeight>startHeight) else startHeight
                        aboveCol-=1
                    aboveHeight = matrix[prevRow][aboveCol][1]
                    startHeight = aboveHeight if(aboveHeight>startHeight) else startHeight
            ## update
            height=startHeight+gardens[tempGardens[row][col]][1]
            width=addedWidth
            matrix[row].append([width, height])
            totalWidth = width if(width>totalWidth) else totalWidth
            totalHeight = height if(height>totalHeight) else totalHeight
    return totalWidth, totalHeight

## out of a possible number of sets picks smallest area
def compare(initialGardens, memo, *temps):
    optimal=[[-1]]
    optArea=sys.maxsize
    ## memoization -> computation for all of the gardens is linear
    for gardens in temps:
        if str(gardens) in memo:
            gardensArea = memo[str(gardens)]
        else:
            bestGardensArrangement = arrange(initialGardens, gardens)
            gardensArea = getArea(bestGardensArrangement[0], bestGardensArrangement[1])
            memo[str(gardens)] = gardensArea
        # update
        optimal = gardens if (gardensArea < optArea) else optimal
        optArea = gardensArea if (gardensArea < optArea) else optArea
    return optimal
## create a four-branched tree i.e. goes each time in four timelines and picks best one
@timer
def fillParts(gardens, memo, gardenIndex=-1, curRow=0, usedGardens=list(), skip=True, arrangement=list() ):
    if len(usedGardens)>=len(gardens):
        return arrangement
    temp1,temp2,temp3,temp4=[[-1]],[[-1]],[[-1]],[[-1]]
    used=False
    if curRow>len(arrangement)-1:
        arrangement.append(list())
    if not skip:
        if gardenIndex not in usedGardens:
            usedGardens.append(gardenIndex)
            arrangement[curRow].append(gardenIndex)
            used=True
    if used:
        temp1 = fillParts(gardens, memo, 0, curRow, c.deepcopy(usedGardens), False, c.deepcopy(arrangement))
        temp2 = fillParts(gardens, memo, 0, curRow+1, c.deepcopy(usedGardens), False, c.deepcopy(arrangement))
    else:
        gardenIndex += 1
        if gardenIndex<len(gardens)-1:
            temp3 = fillParts(gardens, memo, gardenIndex, curRow, c.deepcopy(usedGardens), True, c.deepcopy(arrangement))
        if gardenIndex in gardens and gardenIndex not in usedGardens:
            temp4 = fillParts(gardens, memo, gardenIndex, curRow, c.deepcopy(usedGardens), False, c.deepcopy(arrangement))
    return compare(gardens, memo, temp1, temp2, temp3, temp4)

## same method as arrange above, but this one returns the coordinates of the arrangement
def arrangeWithCoords(gardens, tempGardens):
    if not gardens:
        return (list(),list())
    if tempGardens[0][0]<0: return None
    totalWidth=int()
    totalHeight=int()
    ## for each garden it fills a pair with coordinates (starting- end coordinates)
    startCoords = [list() for row in range(len(tempGardens))]
    endCoords = [list() for row in range(len(tempGardens))]
    measure = [[gardens[tempGardens[y][x]] for x in range(len(tempGardens[y]))] for y in range(len(tempGardens))]
    for row in range(len(tempGardens)):
        width=0
        for col in range(len(tempGardens[row])):
            height=0
            startHeight=0
            addedWidth=width+gardens[tempGardens[row][col]][0]
            if row>0:
                for prevRow in range(row-1, -1, -1):
                    aboveCol=0
                    ##gets upper boundry
                    if addedWidth>endCoords[prevRow][len(endCoords[prevRow])-1][0]:
                        aboveCol = len(endCoords[prevRow])-1
                    else:
                        while addedWidth>endCoords[prevRow][aboveCol][0] and  aboveCol<len(endCoords[prevRow])-1:
                            aboveCol+=1
                    ## gets lower boundry + sets starting height
                    while width<endCoords[prevRow][aboveCol][0] and aboveCol>0:
                        aboveHeight=endCoords[prevRow][aboveCol][1]
                        startHeight = aboveHeight if(aboveHeight>startHeight) else startHeight
                        aboveCol-=1
                    aboveHeight = endCoords[prevRow][aboveCol][1]
                    startHeight = aboveHeight if(aboveHeight>startHeight) else startHeight
            ## update
            startCoords[row].append([width, startHeight])
            height=startHeight+gardens[tempGardens[row][col]][1]
            width=addedWidth
            endCoords[row].append([width, height])
            totalWidth = width if(width>totalWidth) else totalWidth
            totalHeight = height if(height>totalHeight) else totalHeight
    return (startCoords, endCoords)
