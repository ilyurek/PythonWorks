# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:20:50 2021

@author: ilyur
"""
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import data
df = pd.read_csv("linear_regression_dataset.csv")

# plot data
plt.scatter(df.experience,df.sallary)
plt.xlabel("experience")
plt.ylabel("sallary")
plt.show()

# linefit

# sklearn library
from sklearn.linear_model import LinearRegression

#linear regression model
linear_reg = LinearRegression()

x = df.experience.values.reshape(-1,1)
y = df.sallary.values.reshape(-1,1)

linear_reg.fit(x,y)

#prediction

b0 = linear_reg.predict([[0]])

print("b0:",b0)

b0 = linear_reg.intercept_ # intercept

print("b0:",b0)

b1 = linear_reg.coef_

print("b1:",b1) #slope

salllary_new = 1663 + 1138*11
print(salllary_new)

linear_reg.predict([[11]])

# visualize line
array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)

plt.scatter(x,y)
plt.show

y_head = linear_reg.predict(array)

plt.plot(array,y_head,color = "red")

#r2_square

from sklearn.metrics import r2_score

y_pred = linear_reg.predict(x)

print("r_score: ",r2_score(y,y_pred))




