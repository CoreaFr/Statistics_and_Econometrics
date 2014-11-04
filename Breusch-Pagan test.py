# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 11:23:51 2014

@author: francescocorea
"""

# This is a test for heteroskedasticity

import scipy as sp
import statsmodels.api as api

def bp_test(y,x):
    results=api.OLS(y,x).fit()
    residual=results.resid
    
    F=residual**2/(sum(residual**2)/len(residual)) -1
    
    results2=api.OLS(F,x).fit()
    
    fv=results2.fittedvalues
    
    bp=0.5*sum(fv**2)
    
    degree_of_freedom=results2.df_model
    
    p_value=1-sp.stats.chi.cdf(bp,degree_of_freedom)
    
    return bp, degree_of_freedom, p_value
    
