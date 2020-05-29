#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:21:12 2020
xi squared test
@author: chintan
"""
from scipy.stats import chi2
import numpy as np
ps=np.array([1/36,1/18,1/12,1/9,5/36,1/6,5/36,1/9,1/12,1/18,1/36])
O1=np.array([4,10,10,13,20,18,18,11,13,14,13])
O2=np.array([3,7,11,15,19,24,21,17,13,9,5])
n1=sum(O1)
n2=sum(O2)
exp1=ps*n1
exp2=ps*n2
Var1=(O1-exp1)**2/exp1
V1=sum(Var1)
Var2=(O2-exp2)**2/exp2
V2=sum(Var2)
k=10
p1=1.0-chi2.cdf(V1,k)
p2=1.0-chi2.cdf(V2,k)
print('1st set:',100*p1)
print('2nd set:',100*p2)
print('both sets are not sufficiently random')

