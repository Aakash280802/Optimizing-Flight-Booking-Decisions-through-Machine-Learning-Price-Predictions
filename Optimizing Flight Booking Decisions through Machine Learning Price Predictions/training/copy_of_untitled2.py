# -*- coding: utf-8 -*-
"""Copy of Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/126aVJGvygsNSYQkU7lyM1AUuGscjGSDO
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier,GradientBoostingRegressor,AdaBoostRegressor

from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsClassifier 

from sklearn.metrics import f1_score

from sklearn.metrics import classification_report, confusion_matrix

import warnings

import pickle

from scipy import stats

warnings.filterwarnings('ignore')

plt.style.use('fivethirtyeight')

data=pd.read_csv('/content/sample_data/Data_Train(1).csv')

data.head()

for i in category:
  print(i, data[i].unique())

#we now split the Date column to extract the 'Date','Month',and'Year' values,and store them in new columns in our dataframe.
data.Date_of_Journey=data.Date_of_Journey.str.split('/')

data.Date_of_Journey

data['Date']=data.Date_of_Journey.str[0]
data['Month']=data.Date_of_Journey.str[1]
data['Year']=data.Date_of_Journey.str[2]

data.Total_Stops.unique()

data.Route=data.Route.str.split('->')
data.Route

data['City1']=data.Route.str[0]

data['City2']=data.Route.str[1]

data['City3']=data.Route.str[2]

data['City4']=data.Route.str[3]

data['City']=data.Route.str[4]

data['City6']=data.Route.str[5]

data.Dep_Time=data.Dep_Time.str.split(':')

data['Dep_Time_Hour' ]=data.Dep_Time.str[0] 
data['Dep_Time_Mins' ]=data.Dep_Time.str[1]

data. Arrival_Time=data. Arrival_Time.str.split(' ')

data['Arrival_date']=data. Arrival_Time.str[1]
data['Time_of_Arrival' ]=data. Arrival_Time.str[0]

data['Time_of_Arrival' ]=data. Time_of_Arrival.str.split(':')

data['Arrival_Time_Hour' ]=data. Time_of_Arrival.str[0]

data['Arrival_Time_Mins' ]=data.Time_of_Arrival.str[1]

data.Duration=data.Duration. str.split(' ')

data['Travel_Hours']=data.Duration.str[0]
data['Travel_Hours']=data['Travel_Hours'].str.split('h') 
data['Travel Hours']=data['Travel_Hours'].str[0]
data. Travel_Hours=data. Travel_Hours
data['Travel_Mins ']=data.Duration.str[1]

data.Travel_Mins=data.Travel_Mins.str.split('m')
data.Travel_Mins=data.Travel_Mins.str[0]

data.Total_Stops.replace('non_stop',0, inplace=True) 
data.Total_Stops=data.Total_Stops.str.split(' ')
data.Total_Stops=data.Total_Stops.str[0]

data.Additional_Info.unique()

data.Additional_Info.replace('No Info','No Info',inplace=True)

data.isnull().sum()

data.drop(["City1","City2","City3","City4", "city", "city6"],axis=1,inplace=True
data.drop(["Dte_of_Journey","Route","Total_Stops","Arrival_Time","Travel_Mins"],axis=1,inplace=True)

data['Date_of_Journey']fillna(data['Date']inplace=True)

data['City1'].fillna('None', inplace=True)

data['City2'].fillna('None', inplace=True)

data['City3'].fillna('None', inplace=True)

data['City4'].fillna('None', inplace=True)

data['City'].fillna('None', inplace=True)

data['City6'].fillna('None', inplace=True)

data['Arrival_date'].fillna(data['Date'],inplace=True)

data['Travel Mins'].fillna(0,inplace=True)

data.info()

data.Date=data.Date.astype('int64')
data.Month=data.Month.astype('int64')
data.Year=data.Year.astype('int64')
data.Dep_Time_Hour=data.Dep_Time_Hour.astype('int64')
data.Dep_Time_Hour=data.Dep_Time_Hour.astype('int64') 
data.Dep_Time_Mins=data.Dep_Time_Mins.astype('int64')
data.Arrival_date=data.Arrival_date.astype("int64")
data. Arrival_Time_Hour=data. Arrival_Time_Hour.astype('int64') 
data.Arrival_Time_Mins=data. Arrival_Time_Mins.astype('int64')  
data.Travel_Mins=data.Travel_Mins.astype('int64')

data[data['Travel_Hours']=='5m']

data.drop(index=6474,inplace=True,axis=0)

data.Travel_Hours=data.Travel_Hours.astype('int64')

categorical=['Airline', 'Source','Destination', 'Additional_Info','City']

numerical=['Total_Stops', 'Date', 'Month', 'Year', 'Dep_Time_Hour', 'Dep_Time_ Mins', 'Arrival_date', 'Arrival_Time_Hour', 'Arrival_Time_Mins', 'Travel_Hours', 'Travel_Mins']

from sklearn.preprocessing import LabelEncoder 
le=LabelEncoder()

data.Airline=le.fit_transform(data.Airline)

data.Source=le.fit_transform(data.Source)

data.Destination=le.fit_transform(data. Destination)

data.Total_Stops=le.fit_transform(data. Total_Stops)

data.City1=le.fit_transform(data.City1)

data.City2=le.fit_transform(data.City2) 

data.City3=le.fit_transform(data.City3)

data.Additional_Info=le.fit_transform(data. Additional_Info)

data.head()

data=data(['Airline', 'Source', 'Destination', 'Date', 'Month', 'Year', 'Dep_Time_Hour', 'Dep_Time_Mins', 'Arrival_date', 'Arrival_Time_Hour','Arrival_Time_Mins','Travel_Hours','Travel_Mins'])

data.head()

data.describe()

import seaborn as sns 
C=1 
plt.figure(figsize=(20,45))
for i in categorical:
  plt.subplot(6,3,C)
  sns.countplot(data[i])
  plt.xticks(rotation=90)
  plt.tight_layout(pad=3.0)
  C=C+1
plt.show()

plt.figure(figsize=(15,8))
sns.displot(data.Price)

sns.heatmap(data.corr(),annot=True)

import seaborn as sns
sns.boxplot(data['Price'])

y = data['Price']
X = data.drop(columns=['Price'], axis=1)

from sklearn.preprocessing import StandardScaler 
ss=StandardScaler()

X_scaled = ss.fit_transform(X)

X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
X_scaled.head()

from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)

X_train.head()

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor

rfr=RandomForestRegressor()

gb=GradientBoostingRegressor()

ad=AdaBoostRegressor()

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
for i in [rfr,gb,ad]:
    i.fit(X_train,y_train) 
    y_pred-i.predict(X_test)
    test_score=r2_score (y_test,y_pred)
    train_score=r2_score (y_train, i.predict(X_train))
    if abs(train_score=test_score)<=0.2:
       print(i)
       print("R2 score is", r2_score (y_test,y_pred))
       print("R2 for train data", r2_score (y_train, i.predict(X_train)))
       print("Mean Absolute Error is", mean_absolute_error(y_pred,y_test))
       print("Mean Squared Error is",(mean_squared_error(y_pred, y_test))
       print("Root Mean Sqaured Error is",(mean_squared_error(y_pred,y_test,squared=False)))

from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
knn=KNeighborsRegressor()
svr=SVR()
dt=DecisionTreeRegressor()
for i in [knn, svr,dt]:
  i.fit(X_train,y_train)
  y_pred=i.predict(X_test)
  test_score=r2_score (y_test,y_pred) 
  train_score=r2_score (y_train, i.predict(X_train))
  if abs(train_score=test_score)<=0.1:
     print(i)
     print('R2 Score is', r2_score(y_test,y_pred))
     print('R2 Score for train data', r2_score (y_train,i.predict(X_train)))
     print('Mean Absolute Error is', mean_absolute_error(y_test,y_pred))
     print('Mean Squared Error is',mean_squared_error(y_test,y_pred)) 
     print('Root Mean Squared Error is', (mean_squared_error(y_test,y_pred, squared=False)))

from sklearn.model_selection import cross_val_score 
for i in range(2,5): 
  cv=cross_val_score(rfr,X,y,cv=i) 
  print (rfr,cv.mean())

from sklearn.model_selection import RandomizedSearchCV

param_grid={'n_estimators': [10,38,50,70,100],'max depth': [None,1,2,3],'max_features':['auto', 'sqrt']}

rfr=RandomForestRegressor()

rf_res=RandomizedSearchCV(estimator=rfr,param_distributions=param_grid,cv=3, verbose=2,n_jobs=-1)

rf_res.fit(X_train,y_train)

gb=GradientBoostingRegressor()

gb_res=RandomizedSearchCV(estimator=gb,param_distributions=param_grid, cv=3,verbose=2,n_jobs=-1)

gb_res.fit(X_train,y_train)

rfr=RandomForestRegressor(n_estimators=10, max_features='sqrt',max_depth=None)

rfr.fit(x_train,y_train)

y_train_pred=rfr.predict(x_train)
 
y_test_pred=rfr.predict(x_test)

print("train accuracy", r2_score (y_train_pred,y_train))

print("test accuracy", r2_score (y_test_pred,y_test))

Price_list=pd.DataFrame({'Price':Price})

price_list

import pickle
pickle.dump(rfr,open('model1.pkl','wb'))

from flask import Flask,render_template, request

import numpy as np

import pickle

model = pickle.load(open (r"model1.pkl", 'rb'))

@app.route("/home")

def home():

    return render_template('/home.html')

@app.route("/predict")

def home1():

  return render_template('predict.html')

@app.route("/pred", methods=['POST', 'GET'])

def predict(): 

  x = [[int(x) for x in request.form.values()]]

  print(x)

  x= np.array(x)

  print(x.shape)

  print(x)

  pred = model.predict(x)

  print(pred)

  return render_template('submit.html', prediction_text=pred)

if__name__=="__main__":
app.run(debug=False)