# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:44:06 2021

@author: ilyur
"""
# import library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data

df = pd.read_csv("data1.csv")

#plot data

plt.scatter(df.year,df.milk)
plt.xlabel("year")
plt.ylabel("milk_price")
plt.show()

# sklearn library

from sklearn.linear_model import LinearRegression

#linear regression model

linear_reg = LinearRegression()

x = df.year.values.reshape(-1,1)
y = df.milk.values.reshape(-1,1)

linear_reg.fit(x,y)

#prediction

b0 = linear_reg.predict([[0]])

print("b0:",b0)

b1 = linear_reg.coef_

print("b1:",b1)

#visualize line 

array = np.array([1,2,3,4,5,6,7]).reshape(-1,1)

plt.scatter(x,y)
plt.show

y_head = linear_reg.predict(array)

plt.plot(array, y_head ,color ="red")

plt.savefig("milky.png")