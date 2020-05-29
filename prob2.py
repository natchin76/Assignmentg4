#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:00:06 2020
Numpy function to generate uniform random nos
@author: chintan
"""

import numpy as np
from matplotlib import pyplot as plt
import time
n=10000
rand2=np.zeros(n)
x=np.linspace(0,1,n)
y=np.ones(n)
t1=time.time()
t2=time.time()
rand2=np.random.rand(n)

plt.hist(rand2,density=True)
plt.title('Using numpy function')
plt.plot(x,y)
plt.show()
print('time taken:',t2-t1)
