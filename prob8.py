#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:56:09 2020
Area of circle and volume of 10 dim sphere
@author: chintan
"""
import numpy as np
#a) Area of unit circle
n=10000
x=np.random.random(n)
y=np.random.random(n)
count=0
for i in range(n):
    if x[i]**2+y[i]**2<1:
        count+=1
A=4*count/n
print('area of unit circle:',A)
print('actual area:',np.pi)        
print('error in percentage=',100*abs(A-np.pi)/np.pi)

#b) Volume of 10 dim sphere:
n=100000
x=np.zeros([n,10])
for i in range(10):
    x[:,i]=np.random.random(n)
count=0    
for i in range(n):
    if sum(x[i,:]**2)<1:
        count+=1
V=2**10*count/n
print('volume of 10 dim unit sphere:',V)
V_ext=np.pi**5/120
print('actual area:',V_ext)
print('error in percentage=',100*abs(V_ext-V)/V_ext)       