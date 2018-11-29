#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cmath
from matplotlib import pyplot as plt
import numpy as np
 
z = complex(1.0,1.0)
c = complex(0.1,0.8)
n = 5
 
def julia(z, c):
    return(z*z + c)
 
def juliaN(z, c, n):
    for i in range(n):
        z = julia(z, c)
    return(z)
 
#print(julia(z, c))
#print(juliaN(z, c, 10))
 
size = 1000
hSize = size / 2.0
minVal = 0.75
maxVal = 1.25
 
def getData(c):
    data = np.zeros([size, size])
 
    for i in range(size):
        for j in range(size):
            l = abs(juliaN(complex((i - hSize) / hSize , (j - hSize) / hSize ), c, n))
            if l > minVal and l < maxVal:
                data[i,j] = 1
    return(data)
 
def showData(data):
    plt.imshow(data, interpolation="nearest", origin="upper")
    plt.colorbar()
    plt.show()
 
data = getData(complex(0.2, 0.2))
showData(data)

