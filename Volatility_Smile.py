# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 11:53:34 2014

@author: francescocorea
"""

# Volatility Smile

import scipy as sp
import numpy as np
import datetime
from pandas.io.data import Options
from matplotlib.finance import quotes_historical_yahoo as yahoo
import bs_option as bs


def Vol_Smile(ticker,expiration,S,K,T,r,call_price):
    implied=1.
    minimum_value=1000
    for i in range(10000):
        sigma=0.0001*(1+i)
        d1=(sp.log(S/K)+(r+sigma*sigma/2.)*T)/(sigma*sp.sqrt(T))
        d2=d1-sigma*sp.sqrt(T)
        call_iv=S*sp.stats.norm.cdf(d1)-K*sp.exp(-r*T)*sp.stats.norm.cdf(d2)
        if call_iv-call_price < minimum_value:
            minimum_value=call_iv-call_price
            implied=sigma
            i=k
        return implied
    
    begdate=datetime.date(2011,1,1)
    enddate=datetime.date.today()
    
    option_data=Options(ticker,'yahoo').get_call_data(expiry=expiration)
    price_data=yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)
    
        