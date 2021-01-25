#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:23:16 2021

@author: hilsys
"""

import cubic_spline as sp



# using cubic spline to fit the given points
# param x: the x position of the given points
# param y: the y position of the given points
# param option: the bound condition of the cubic spline, this value should be 0 or 1 or 2, default to 0
# param l_val: the value of the left bound.used together with param option, default to 0
# param r_val: the value of the right bound. used together with param option, default to 0  

# if option is 0, it means the default settings, the method will give a fitting results according to the defaults
# which is the 3_rd order derivative of the left bound and roght bound are the same

# if option is 1, it means it is in the first order mode, and the l_val is the first derivative of the left bound and 
# the r_val is the first derivative of the right bound

# if option is 2, it means it is in the second order mode, and the l_val is the second derivative of the left bound and 
# the r_val is the second derivative of the right bound

x = [27, 28, 29, 30, 32]
y = [4.1, 4.3, 4.1, 3.0, 3.4]
#x = [27, 28.5, 29, 30,33]
#y = [4.1, 4.3, 4.1, 3.0,5.1]

cl=sp.cubic_spline(x,y,option=0,l_val=0,r_val=0)
cl.show_figure()

cl.get_position(31)
cl.get_first_derivative(31)
cl.get_second_derivative(31)