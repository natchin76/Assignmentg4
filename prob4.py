#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:15:09 2020
Exponential random nos using transformation method
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
n=10000
mean=0.5
runi=np.random.rand(n)
rexp=-mean*np.log(runi)
plt.hist(rexp,density=True)
x=np.linspace(0,20,100)
y=np.exp(-x/mean)
plt.plot(x,y)
plt.show()

    
