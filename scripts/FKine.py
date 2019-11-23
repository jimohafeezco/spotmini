#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:19:09 2019

@author: hafeez
"""

from sympy import *
from numpy import *
from numpy.linalg import inv
from time import time
from mpmath import radians
import numpy as np
#from tf import transformations
#

def DHMatrix(alpha,a,d,theta):
    return np.matrix([[cos(theta), -sin(theta), 0, a],
                   [sin(theta)*cos(alpha), cos(theta)*cos(alpha), -sin(alpha), -sin(alpha)*d],
                   [sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha), cos(alpha)*d],
                   [0, 0, 0, 1]])


# Build transformation matrix given configuration vector "q" and start and end coordinate frame indices
def FK(q,params,startIdx,endIdx):

    theta = [q[0], q[1]-pi/2, q[2], q[3], q[4], q[5]]; # Includes correction to q2 (or q[1])

    # Loop through all the selected indices
    M = np.eye(4);
    for idx in range(startIdx,endIdx):
        M = M*DHMatrix(params["alpha"][idx],params["a"][idx],params["d"][idx],theta[idx])
    return M;

#startd_idx starts from 1 and ends at 6
alpha = [pi/3, pi/6, pi/6, pi, pi/6, pi/6] 
a = [1,2,1,2,1,1]
d = [1,2,1,2,1,1]
params ={"alpha": alpha, "a": a, "d" :d}
q= [pi/3, pi/3, pi/4, pi/6, pi/6, pi/6]



    
    
tests= {1:{"alpha":[pi, pi/2, pi/6, pi/6, pi/6, pi/6], "a":[1,2,1,2,1,1], "d":[1,2,1,2,1,1]}, 
         2:{"alpha":[pi/3, pi/5, pi/6, pi/6, pi/6, pi], "a":[1,2,1,2,1,1], "d":[1,2,1,2,1,1]},
         3:{"alpha":[pi, pi/2, pi/6, pi/6, pi/6, pi], "a":[1,2,0,2,1,1], "d":[1,2,1,2,1,1]},
         4:{"alpha":[pi, pi/2, pi/6, pi/6, pi/6, pi], "a":[1,2,0,2,1,1], "d":[1,2,1,2,1,1]},
         5:{"alpha":[pi, pi/2, -pi/2, pi, pi/6, pi/6], "a":[1,2,1,2,1,1], "d":[1,2,1,2,1,1]}}

#
#FK1 =FK(q, tests[1], 0,6) 
#FK2 =FK(q, tests[2], 0,6) 
#FK3 =FK(q, tests[3], 0,6) 
#FK4 =FK(q, tests[4], 0,6) 