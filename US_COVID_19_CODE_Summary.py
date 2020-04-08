# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:56:25 2020

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

#from scipy.stats import linregress
#importing data
dataset = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

#data munging

state_count=dataset.groupby('state')['state'].count().rename('count').reset_index()
state_deaths=dataset.groupby('state')['deaths'].sum().rename('deaths').reset_index()
state_count_deaths=state_count.merge(state_deaths,how='inner')
state_cases=dataset.groupby('state')['cases'].sum().rename('cases').reset_index()
state_count_cases_deaths=state_count.merge(state_cases,how='inner').merge(state_deaths,how='inner')

#statitistics
state_count_cases_deaths.describe()

#filtering state with min and max

CASES=state_cases[['cases']]
CASES.min()
CASES.max()
#find minimum first then find the country
state_cases[state_cases.cases==54]
state_cases[state_cases.cases==1111808]
state_count_cases_deaths.describe()


CASESD=state_deaths[['deaths']]
CASESD.min()
CASESD.max()
state_deaths[state_deaths.deaths==0]
state_deaths[state_deaths.deaths==25089]

#plot data

X=state_count_cases_deaths.state
Y=state_count_cases_deaths.cases
Z=state_count_cases_deaths.deaths

plt.figure(figsize=(10,10))
plt.plot(Y,'k')
plt.xlabel('state rank')
plt.ylabel('number of cases')
plt.legend('cases')

plt.plot(Z,'r')
plt.xlabel('state rank')
plt.ylabel('number of deaths')
plt.legend('deaths')
date_count=dataset.groupby('date')['date'].count().rename('count').reset_index()
date_cases=dataset.groupby('date')['cases'].sum().rename('cases').reset_index()
date_deaths=dataset.groupby('date')['deaths'].sum().rename('deaths').reset_index()
#state_count_cases_deaths=state_count.merge(state_cases,how='inner').merge(state_deaths,how='inner')
date_count_cases_deaths=date_count.merge(date_cases, how='inner').merge(date_deaths, how='inner')
plt.plot(date_count_cases_deaths.date,date_count_cases_deaths.cases)




