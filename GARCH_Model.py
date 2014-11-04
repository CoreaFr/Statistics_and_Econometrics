# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 11:54:40 2014

@author: francescocorea
"""

# GARCH Model (General Autoregressive Conditional Heteroskedasticity Model) - Simulation

import scipy as sp
from matplotlib.pyplot import plot, title,show

"Parameters"

observations=1000
obs_to_drop=100
total=observations + obs_to_drop
alphas=(0.1,0.3)
beta=0.2

"ARCH (1) - Autoregressive Conditional Heteroskedasticity Model of order 1"

sp.random.seed(1)

errors=sp.random.normal(0,1,total)

error_t=sp.zeros(total)
error_t[0]=sp.random.normal(0,sp.sqrt(alphas[0]/(1-alphas[1])),1)

for i in range(0,total-1):
    error_t[i]=errors[i]*sp.sqrt(alphas[0]+alphas[1]*error_t[i-1]**2)
    
plot(range(observations),error_t[obs_to_drop-1:-1])
title("ARCH (1) simulation")

show()

"GARCH (1,1) - General Autoregressive Conditional Heteroskedasticity Model of order (1,1)"

sp.random.seed(2)

errors=sp.random.normal(0,1,total)

error_t=sp.zeros(total)

error_t[0]=sp.random.normal(0,sp.sqrt(alphas[0]/(1-alphas[1])),1)

for i in range (1,total-1):
    error_t[i]=errors[i]*sp.sqrt(alphas[0] + alphas[1]*errors[i-1]**2 + beta*error_t[i-1]**2)
    
plot(range(observations),error_t[obs_to_drop-1:-1])
title("GARCH (1,1) simulation")

show()
