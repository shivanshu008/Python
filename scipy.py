# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:48:58 2024

@author: shivanshu gaurav
"""

print("shovanshuf")
from scipy import constants
print(constants.liter)
import scipy
print(scipy.__version__)
print(constants.pi)
print(dir(constants))
print(constants.yotta)
print(constants.kibi)
from scipy.optimize import root
from math import cos
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)
print(myroot)