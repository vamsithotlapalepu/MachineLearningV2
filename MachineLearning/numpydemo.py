# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from scipy.misc import imread
import numpy

#im = imread("example.jpg")

#to coonvert a 2-d array into csv file
a = numpy.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
numpy.savetxt("foo.csv", a, delimiter=",")

