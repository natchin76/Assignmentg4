#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:43:11 2020
Prob1: Linear congruential random number generator
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
import time


def Lrand(n):
    x=1
    a=1236117
    c=1123624237
    m=7123625533
    rand=np.zeros(n)
    rand[0]=x
    for i in range(1,n):
        rand[i]=(a*rand[i-1]+c)%m
    return(rand/m)    

n=10000
x=np.linspace(0,1,n)
y=np.ones(n)
t1=time.time()
rand=Lrand(n)
t2=time.time()

plt.hist(rand,density=True)
plt.plot(x,y)
plt.title('using linear congruential method')
plt.show()
print('time taken:',t2-t1)