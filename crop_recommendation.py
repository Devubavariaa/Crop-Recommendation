# -*- coding: utf-8 -*-
"""CROP RECOMMENDATION

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-W9NdrrAK44zXL33kUlnTwMW00YfhZd0
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("C:/Users/DEVANSHI BAVARIA/Downloads/CROP RECOMMENDATION/Crop_recommendation.csv")

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=50)

model=RandomForestClassifier()
model.fit(x_train,y_train)
prediction=model.predict(x_test)

accuracy=model.score(x_test,y_test)


new_features=[[34,67,45,23,12.33,34,56]]
crop=model.predict(new_features)


import pickle

pickle.dump(model,open("model.pickle","wb"))