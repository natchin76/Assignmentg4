#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:37:04 2020
Prob 10:Inference
@author: chintan
"""
from scipy.optimize import minimize
import numpy as np
import emcee
import corner


from matplotlib import pyplot as plt
x=np.loadtxt('prob10.txt',usecols=2)
y=np.loadtxt('prob10.txt',usecols=4)
sigma_y=np.loadtxt('prob10.txt',usecols=6)
def log_lik(theta,x,y,sigma_y):
    a,b,c=theta
    y_pred=a*x**2+b*x+c
    sigma2=sigma_y**2
    return 0.5 * np.sum((y - y_pred)**2 / sigma2 + np.log(2 * np.pi * sigma2))
def log_prior(theta):
    a,b,c=theta
    if -1000<a<1000 and -1000<b<1000 and -1000<c<1000:
        return 0
    else:
        return -np.inf
def log_prob(theta,x,y,sigma_y):
    if  np.isinf(log_prior(theta)):
        return -np.inf
    else:
        return log_prior(theta)-log_lik(theta, x,y,sigma_y)

#obtain a,b,c which minimize (-log-likelihood) 
guess=(1,1,1)
soln=minimize(log_lik,guess,args=(x,y,sigma_y))   

#50 markov chains each starting from near the maxima of prob distribution. Each chain is in 3D
nwalk,ndim=50,3
pos=soln.x+1e-4*np.random.randn(nwalk,ndim)
sampler=emcee.EnsembleSampler(nwalk,ndim,log_prob,args=(x,y,sigma_y))
sampler.run_mcmc(pos,4000)
samples=sampler.get_chain()
plt.figure(figsize=(16,3))
plt.subplot(311)
plt.plot(samples[:,:,0])     #a
plt.xlabel('step no') 
plt.ylabel('a')
plt.subplot(312)
plt.plot(samples[:,:,1],)  #b
plt.xlabel('step no') 
plt.ylabel('b')
plt.subplot(313)
plt.plot(samples[:,:,2],)  #c
plt.xlabel('step no') 
plt.ylabel('c')
plt.show()


data=np.zeros([3,4000*50])
for i in range(3):
    data[i,:]=np.hstack(samples[:,:,i])
data=np.transpose(data)
a=np.median(data[:,0])
b=np.median(data[:,1])
c=np.median(data[:,2])    
plt.figure()
corner.corner(data,labels=['a', 'b', 'c'],show_titles=True,truths=[a,b,c])
plt.show()

x_pr=np.linspace(50,300,500)
for i in range(200):
    j=int(4000*50*np.random.uniform())
    a_pr=data[j,0]
    b_pr=data[j,1]
    c_pr=data[j,2]
    plt.plot(x_pr,a_pr*x_pr**2+b_pr*x_pr+c_pr)
    
    
    
plt.errorbar(x, y, yerr=sigma_y,fmt='o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print('mean values of [a,b,c]:',[np.mean(data[:,0]),np.mean(data[:,1]),np.mean(data[:,2])])
print('st. deviations [a,b,c]:',[np.std(data[:,0]),np.std(data[:,1]),np.std(data[:,2])])                      