# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:32:20 2021

@author: ilyur
"""

#import library

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

#read data

df = pd.read_csv("random_forest_regression_dataset.csv",header = None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#random forest regression

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators = 100, random_state = 42 ) 
 
rf.fit(x,y)

y_head = rf.predict(x)

#r2_score

from sklearn.metrics import r2_score

print("r_score: ", r2_score(y,y_head))