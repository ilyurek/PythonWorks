# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:59:36 2021

@author: ilyur
"""

#import library

import pandas as pd 
import numpy as np

#reaad data

data = pd.read_csv("data.csv")

#drop data

data.drop(["id","Unnamed: 32"],axis=1,inplace = True)

#%% 0-1

data["diagnosis"] = [1 if each == "M" else 0 for each in data["diagnosis"]]


#%% y,x-data

y = data["diagnosis"].values
x_data = data.drop(["diagnosis"],axis=1)

#%% normalization

x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data))

#%% train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.15,random_state=42)

#%% decision_tree

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()

dt.fit(x_train,y_train)
print(dt.score(x_test,y_test))

#%% random forest

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 100,random_state = 1) # 100 tane decision tree kullandık
rf.fit(x_train,y_train)
print("random_forest_algo_result:",rf.score(x_test,y_test))