# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:53:03 2021

@author: ilyur
"""

#%% import data

import pandas as pd
import numpy as np

#%% read the data

data = pd.read_csv("data.csv")

#%% data drop

data.drop(["id","Unnamed: 32"],axis=1,inplace=True)

#%% 1-0

data["diagnosis"] = [1 if each == "M" else 0 for each in data["diagnosis"]]

#%% y,x_data

y = data["diagnosis"].values
x_data = data.drop(["diagnosis"],axis=1)

#%% normalization

x = (x_data - np.min(x_data)) / (np.max(x_data)-np.min(x_data))

#%% train test split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.15, random_state = 42)

#%% random forest

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100,random_state=1)
rf.fit(x_train,y_train)
print("accuracy:",rf.score(x_test,y_test))

#%% confusion matrix

y_pred = rf.predict(x_test)
y_true = y_test

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true,y_pred)
#%% visualization

import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cm,annot=True,linewidth=0.5,linecolor = "red",fmt=".0f",ax =ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()
#
