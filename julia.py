#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmath
from matplotlib import pyplot as plt
import numpy as np
 
def julia(z, c):
    return(z*z + c)
 
def juliaN(z, c, n):
    for i in range(n):
        z = julia(z, c)
    return(z)
 
def onJulia(z, c, n, margin):
    for i in range(n):
        z = julia(z, c)
    if abs(abs(z) - 1) < margin:
        return(1) 
    else:
        return(0)
 
def juliaData(pSize, c, n, margin):
    pData = np.zeros([pSize, pSize])
    hSize = pSize / 2.0
    for i in range(pSize):
        for j in range(pSize):
            z = complex((i - hSize) / hSize,(j - hSize) / hSize)
            pData[i, j] = onJulia(z, c, n, margin)
    return(pData)
 
def showData(data):
    plt.imshow(data, interpolation="nearest", origin="upper")
    plt.colorbar()
    plt.show()
 
# Settings
size = 1000
n = 5
margin = 0.25
 
# C - Change this number
c = complex(0.2, -0.3)
#0.687 + 0.312i

# Generate julia and show
data = juliaData(size, c, n, margin)
showData(data)
