#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:25:19 2021

@author: hilsys
"""

import function as F
import math
import matplotlib.pyplot as plt

class cubic_spline():
    def __init__(self,x,y,option=0,l_val=0,r_val=0):
        '''
        the input x should be increasing! 
        '''
        if len(x)==0 or len(y)==0:
            print('empty input')
        if option == 0 and (l_val!=0 or r_val!=0):
            print('invaid input parameters for cubic spline')
            exit(0)
        if option != 0 and option !=1 and option!=2 :
            print('invalid input for parameter option, this value should be 0 or 1 or 2')
            
        for i in range(len(x)):
            x[i]*=1.0
            y[i]*=1.0
        
        if option ==0:
            print('using default settings for the cubic spline fitting')
            self.parameters = F.solution_of_equation(F.spline3_Parameters(x), x, y)
        elif option == 1:
            print('using first derivative mode, the left value is '+str(l_val)+'and the right value is ' +str(r_val))
            self.parameters = F.solution_of_equation(F.spline3_Parameters(x, 1), x, y, opt = 1, lval = l_val, rval = r_val)
        elif option == 2:
            print('using second derivative mode, the left value is '+str(l_val)+'and the right value is ' +str(r_val))
            self.parameters = F.solution_of_equation(F.spline3_Parameters(x, 2), x, y, opt = 2, lval = l_val, rval = r_val)
        self.minx=x[0]
        self.maxx=x[-1]
        self.datax=x
        self.datay=y
        #print(self.parameters)
        
    def get_position(self,x):
        '''
        compute the value at the x position in the current cubic spline
        '''
        if x < self.minx:
            print('the input x is to small for the current cubic spline')
            return
        elif x>self.maxx:
            print('the input x is to large for the current cubic spline')
            return
        else:
            count = 0
            while x > self.datax[count]:
                count+=1
            c_p=[self.parameters[4 * (count-1)], self.parameters[1 + 4 * (count-1)], 
                                              self.parameters[2 + 4 * (count-1)], self.parameters[3 + 4 * (count-1)]]
            
            return c_p[0]*math.pow(x,3) + c_p[1]*math.pow(x,2) + c_p[2] * x + c_p[3]
        
    def get_first_derivative(self,x):
        '''
        compute the first derivative at the x position in the current cubic spline
        '''
        if x < self.minx:
            print('the input x is to small for the current cubic spline')
            return
        elif x>self.maxx:
            print('the input x is to large for the current cubic spline')
            return
        else:
            count = 0
            while x > self.datax[count]:
                count+=1
            c_p=[self.parameters[4 * (count-1)], self.parameters[1 + 4 * (count-1)], 
                                              self.parameters[2 + 4 * (count-1)], self.parameters[3 + 4 * (count-1)]]
            
            return 3*c_p[0]*math.pow(x,2) + 2*c_p[1]*x + c_p[2]
        
    def get_second_derivative(self,x):
        '''
        compute the second derivative at the x position in the current cubic spline
        '''
        if x < self.minx:
            print('the input x is to small for the current cubic spline')
            return
        elif x>self.maxx:
            print('the input x is to large for the current cubic spline')
            return
        else:
            count = 0
            while x > self.datax[count]:
                count+=1
            c_p=[self.parameters[4 * (count-1)], self.parameters[1 + 4 * (count-1)], 
                                              self.parameters[2 + 4 * (count-1)], self.parameters[3 + 4 * (count-1)]]
            
            return 6*c_p[0]*x + 2*c_p[1]
        
    def show_figure(self):
        x=[]
        y=[]
        f_d=[]
        s_d=[]
        for i in range(100):
            x.append(self.datax[0]+(i+1)*1.0*(self.datax[-1]-self.datax[0])/100)
        for i in range(100):
            y.append(self.get_position(x[i]))
            f_d.append(self.get_first_derivative(x[i]))
            s_d.append(self.get_second_derivative(x[i]))
        
        plt.figure(1)
        plt.plot(x,y)
        length = len(self.datax)
        for i in range(length):
            plt.plot(self.datax[i], self.datay[i], 'bo')
        plt.title('position')
        plt.show()
        
        #print(f_d)
        plt.figure(2)
        plt.plot(x,f_d)
        plt.title('first derivative')
        plt.show()
        
        #print(s_d)
        plt.figure(3)
        plt.plot(x,s_d)
        plt.title('second derivative')
        plt.show()


