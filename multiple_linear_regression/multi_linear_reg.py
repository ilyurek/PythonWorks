# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:21:59 2021

@author: ilyur
"""
#import library
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression

#import data

df = pd.read_csv("multi_linear_regression_dataset.csv")

x = df.iloc[:,[0,2]].values
y = df.sallary.values.reshape(-1,1)

multiple_linear_regression = LinearRegression()
multiple_linear_regression.fit(x,y)

print("b0:",multiple_linear_regression.intercept_)
print("b1,b2:",multiple_linear_regression.coef_)

#predict

multiple_linear_regression.predict(np.array([[10,35],[5,35]]))