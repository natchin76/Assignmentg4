#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:57:04 2020
Rejection method
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
n=10000
x=10*np.random.random(n)
y=np.random.random(n)
def f(x):
    return(np.sqrt(2/np.pi)*np.exp(-x**2/2))
y_acc=y[y<f(x)]
x_acc=x[y<f(x)]
plt.hist(x_acc,density=True)
x1=np.linspace(0,10,50)
y1=np.sqrt(2/np.pi)*np.exp(-x1**2/2)
plt.plot(x1,y1)
plt.show()