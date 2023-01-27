# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:45:28 2021

@author: ilyur
"""
#import library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# read 

df = pd.read_csv("poly_reg.csv")

#visualize

y = df.car_speed.values.reshape(-1,1)
x = df.car_price.values.reshape(-1,1)

plt.scatter(x,y,color = "red")
plt.ylabel("car_speed")
plt.xlabel("car_price")


#linear regression

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x,y)

#predict

y_head = lr.predict(x)

plt.plot(x,y_head,color="green",label="linear")
plt.legend()
plt.scatter(x,y,color = "red")


prediction = np.array(10000).reshape(-1,1)
lr.predict(prediction)

#polynomial linear regression

from sklearn.preprocessing import PolynomialFeatures

polynomial_reg = PolynomialFeatures(degree = 4)

x_poly = polynomial_reg.fit_transform(x)

linear_regression2 = LinearRegression()
linear_regression2.fit(x_poly,y)

y_head2 =linear_regression2.predict(x_poly)

plt.plot(x,y_head2,color="purple",label="poly")
plt.legend()
plt.scatter(x,y,color = "red")
plt.show()
