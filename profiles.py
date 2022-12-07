import csv
import numpy as np


def computeShape(currentShape, size=1080):
    x,y,z,height,width,depth=0,0,0,0,0,0
    #print(f'length: {len(currentShape)}')
    for side in currentShape:
        #print(currentShape[0][0],side)
        if side[1] == 'circle':
            #change height
            if height != 0: height = (height + int(side[5]))/2 
            else: height = int(side[5])
            #chang width
            if width != 0: width = (width + int(side[4]))/2
            else: width = int(side[4])
            #change x
            if x != 0: x = (x+int(side[3]))/2
            else: x = int(side[3])
            #change y
            if y != 0: y = (y+int(side[3]))/2
            else: y = int(side[3])
        elif side[1] == 'triangle':
            #change height
            if height != 0: height = (height + int(side[5]))/2 
            else: height = side[5]
            #change depth
            if depth != 0: depth = (depth + int(side[4]))/2
            else: depth = int(side[4])
            #change y
            
            if y != 0: y = (y+int(side[3]))/2
            else: y = int(side[3])
            #change z
            if z != 0: z = (z+(int(int(side[3]))+depth))/2
            else: z = (int(side[3])+depth)
        elif side[1] == 'semi':
            #change height
            if height != 0: height = (height + int(side[5]))/2 
            else: height = side[5]
            #change depth
            if depth != 0: depth = (depth + int(side[4]))/2
            else: depth = int(side[4])
            #change y
            if y != 0: y = (y+int(side[3]))/2
            else: y = int(side[3])
            #change z
            if z != 0: z = (z+int(side[3]))/2
            else: z = (int(side[3]))
        elif side[1] == 'trapezoid':
            #change height
            if height != 0: height = (height + int(side[5]))/2 
            else: height = int(side[5])
            #chang width
            if width != 0: width = (width + int(side[4]))/2
            else: width = int(side[4])
            #change x
            if x != 0: x = (x+(int(side[3])+width))/2
            else: x = (int(side[3])+width)
            #change y
            if y != 0: y = (y+int(side[3]))/2
            else: y = int(side[3])
    return [currentShape[0][0],x,y,size-z,height,width,depth]

def directionalOrientationalAllignment(coordsFile='coords.csv', size=1080):
    coords = open(coordsFile, 'r')
    coordsList = np.array(list(csv.reader(coords, delimiter=","))) #takes it in as objectName, side, x, y, height, width

    
    profileList = []
    currentShape = [coordsList[0]]

    for i,coord in enumerate(coordsList):
        if coord[0] == currentShape[0][0] and coord[1] != currentShape[0][1]:
            currentShape.append(coord)
            if i == len(coordsList)-1:
                profileList.append(computeShape(currentShape,size))
        else:
            if i != 0:
                #print(currentShape)
                profileList.append(computeShape(currentShape,size))
            #reset to next one
            currentShape = [coord]

    #print(profileList)
    return profileList

#directionalOrientationalAllignment()
