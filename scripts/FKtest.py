#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:42:42 2019

@author: hafeez
"""
from FKine import *
import numpy as np
import unittest

FK1 =matrix([[ 0.7623116 , -0.44800391,  0.46709048,  9.8882595 ],
        [ 0.64475073,  0.46281563, -0.60835696, -2.01564422],
        [ 0.05636952,  0.7649145 ,  0.64166057,  1.99479527],
        [ 0.        ,  0.        ,  0.        ,  1.        ]])


FK2 = matrix([[ 0.34463624, -0.04049131, -0.93786263,  7.77967653],
        [-0.44396507,  0.87324464, -0.20084527, -3.57893238],
        [ 0.827116  ,  0.48559681,  0.28297502,  4.32739645],
        [ 0.        ,  0.        ,  0.        ,  1.        ]])

FK3 = matrix([[ 0.88545387, -0.23471525, -0.40109874,  8.58705758],
        [-0.18207973, -0.96929673,  0.16525986, -0.4920274 ],
        [-0.42757271, -0.07329803, -0.90100443, -0.04786973],
        [ 0.        ,  0.        ,  0.        ,  1.        ]])

FK4 =matrix([[ 0.88545387, -0.23471525, -0.40109874,  8.58705758],
        [-0.18207973, -0.96929673,  0.16525986, -0.4920274 ],
        [-0.42757271, -0.07329803, -0.90100443, -0.04786973],
        [ 0.        ,  0.        ,  0.        ,  1.        ]])
# test cases
q= [pi/3, pi/3, pi/4, pi/6, pi/6, pi/6]



    
    
tests= {1:{"alpha":[pi, pi/2, pi/6, pi/6, pi/6, pi/6], "a":[1,2,1,2,1,1], "d":[1,2,1,2,1,1]}, 
         2:{"alpha":[pi/3, pi/5, pi/6, pi/6, pi/6, pi], "a":[1,2,1,2,1,1], "d":[1,2,1,2,1,1]},
         3:{"alpha":[pi, pi/2, pi/6, pi/6, pi/6, pi], "a":[1,2,0,2,1,1], "d":[1,2,1,2,1,1]},
         4:{"alpha":[pi, pi/2, pi/6, pi/6, pi/6, pi], "a":[1,2,0,2,1,1], "d":[1,2,1,2,1,1]},
         5:{"alpha":[pi, pi/2, -pi/2, pi, pi/6, pi/6], "a":[1,2,1,2,1,1], "d":[1,2,1,2,1,1]}}

#np.testing.assert_allclose(test2, FK1, rtol = 0.0001, atol =0)
test1 = FK(q, tests[1], 0,6)
test2 = FK(q, tests[2], 0,6)
test3 = FK(q, tests[3], 0, 6)
test4 = FK(q, tests[4], 0, 6)

class testMat(unittest.TestCase):
 
    
    def testFK(self):
#        self.assertAlmostEquals(FK1,test1)
        np.testing.assert_allclose(test1, FK1, rtol = 0.0001, atol =0)
        np.testing.assert_allclose(test2, FK2, rtol = 0.0001, atol =0)
    def test2(self):
        np.testing.assert_allclose(test3, FK3, rtol = 0.0001, atol =0)
        np.testing.assert_allclose(test4, FK3, rtol = 0.0001, atol =0)
    def test3(self):
        self.assertNotEqual(test1.any(), 0)
        self.assertNotEqual(test2.any(), 0)
        self.assertNotEqual(test3.any(), 0)
        self.assertNotEqual(test4.any(), 0)





if __name__ == '__main__':
    unittest.main()
    
    
    
    