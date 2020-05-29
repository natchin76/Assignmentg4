#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:50:57 2020
Box Muller method
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
n=10000
x1=np.random.random(n)
x2=np.random.random(n)
rnorm= np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
plt.hist(rnorm,density=True)
x=np.linspace(-5,5,50)
y=1/np.sqrt(2*np.pi)*np.exp(-x**2/2)
plt.plot(x,y)
plt.show()
