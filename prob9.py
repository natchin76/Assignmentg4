#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:27:51 2020
MCMC for uniform distribution
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if (x<7 and x>3):
        return(1)
    else: 
        return(1e-10)
n=100000
theta=[0]
for i in range(n):
    theta_prime=theta[i]+np.random.normal()
    r=np.random.rand()
    if f(theta_prime)/f(theta[i])>r:
        theta.append(theta_prime)
    else:
        theta.append(theta[i])        

plt.hist(theta,density='true',range=(3,7))
plt.show()
plt.figure(figsize=(16,3))
plt.plot(theta[0:5000])
plt.ylim(0,7)
plt.title('Markov chain')
plt.show()        