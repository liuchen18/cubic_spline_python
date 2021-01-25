# cubic spline python

this is a python lib to use cubic spline to fit the given points<br>

## about the param
param x: the x position of the given points<br>
param y: the y position of the given points<br>
param option: the bound condition of the cubic spline, this value should be 0 or 1 or 2, default to 0<br>
param l_val: the value of the left bound.used together with param option, default to 0<br>
param r_val: the value of the right bound. used together with param option, default to 0<br>  

if option is 0, it means the default settings, the method will give a fitting results according to the defaults, which is the 3_rd order derivative of the left bound and roght bound are the same

if option is 1, it means it is in the first order mode, and the l_val is the first derivative of the left bound and the r_val is the first derivative of the right bound

if option is 2, it means it is in the second order mode, and the l_val is the second derivative of the left bound and the r_val is the second derivative of the right bound

## how to use

you can simply import cubic_spline and costruct the cubic_spline class,like
```
import cubic_spline as sp
my_cubic_spline=sp.cubic_spline(x,y)
```
and then get data from the cubic spline from my_cubic_spline by calling the functions
```
my_cubic_spline.get_position(given_x)
my_cubic_spline.get_first_derivative(given_x)
my_cubic_spline.get_second_derivative(given_x)
```
and plot the figures by calling
```
my_cubic_spline.show_figure()
```
detiled example is in example.py

the figures in example are as follows:
![alt position](https://github.com/liuchen18/cubic_spline_python/blob/main/position.png,"position")
![alt first](https://github.com/liuchen18/cubic_spline_python/blob/main/first_derivative.png,"first derivative")
![alt second](https://github.com/liuchen18/cubic_spline_python/blob/main/second_derivative.png,"second derivative")