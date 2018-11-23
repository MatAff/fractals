# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

lines = [[0,1000,2000,1000]]

def getCenter(l):
    return([(l[0] + l[2]) / 2, 
            (l[1] + l[3]) / 2])
def getDxy(l):
    return([(l[1] - l[3]) * 0.5,
            (l[0] - l[2]) * 0.75])
def split(l):
    center = getCenter(l)
    dXY = getDxy(l)
    
    first = [center[0],
             center[1],
             center[0] + dXY[0],
             center[1] + dXY[1]]
    second = [center[0],
             center[1],
             center[0] - dXY[0],
             center[1] - dXY[1]]
    return([first,second])

def splitLines(lines):
    sLines = []
    for l in lines:
        sLines.extend(split(l))
    return(sLines)
    
def plotLines(lines):
    for l in lines:
        plt.plot([l[0],l[2]], [l[1],l[3]])
    
# Plot and split    
plt.figure(figsize=(10, 10), dpi=100)
plt.axis('off')

for level in range(12):
    plotLines(lines)
    lines = splitLines(lines)
plt.savefig("first.png", bbox_inches='tight', dpi=1000)
plt.show()    



            
