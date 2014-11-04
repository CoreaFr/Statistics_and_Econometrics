# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 10:27:55 2014

@author: francescocorea
"""

# Lower Partial Standard Deviation

import pandas as pd
import scipy.stats as stats
import numpy as np
import datetime as dt
from matplotlib.finance import quotes_historical_yahoo as yahoo

ticker='IBM'

begdate=(2008,12,31)
enddate=(2009,11,1)

# For the risk free rate, using Fama-French daily dataset. The data already formatted has been downloaded from Yan's website.

price=yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)

returns=(price.aclose[1:]-price.aclose[:-1])/price.aclose[1:]

x=pd.DataFrame(data=returns,index=price.date[:-1],columns=['returns'])

ff=pd.load('ffDaily.pickle')
final_data=pd.merge(x,ff,left_index=True,right_index=True)

premium=final_data.returns-final_data.Rf

LPSD=np.std(premium[premium > 0])*np.sqrt(252)

print "LPSD is " + str(LPSD)