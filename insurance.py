import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Social_Network_Ads.csv')
 
x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values
y = y.reshape(-1,1)

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
label = LabelEncoder()
x[:,-1] = label.fit_transform(x[:,-1])
x[:,-2] = label.fit_transform(x[:,-2])
x[:,0] = label.fit_transform(x[:,0])
one = OneHotEncoder(categorical_features = [-1])
x = one.fit_transform(x).toarray()
x = x[:,1:]



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=0)
#######################################################
from sklearn.preprocessing import RobustScaler
sc_x = RobustScaler()
X_train = sc_x.fit_transform(x_train)
X_test = sc_x.transform(x_test)

sc_y = RobustScaler()
Y_train = sc_y.fit_transform(y_train)
Y_test  = sc_y.transform(y_test)

########################################################

from sklearn.preprocessing import MinMaxScaler
sc_x = MinMaxScaler()
X_train = sc_x.fit_transform(x_train)
X_test = sc_x.transform(x_test)

sc_y = MinMaxScaler()
Y_train = sc_y.fit_transform(y_train)
Y_test  = sc_y.transform(y_test)
##################################################
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(x_train)
X_test = sc_x.transform(x_test)

sc_y = StandardScaler()
Y_train = sc_y.fit_transform(y_train)
Y_test  = sc_y.transform(y_test)
#######################################################
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,Y_train)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 300,random_state=0)
model.fit(X_train,Y_train)

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(random_state = 0)
model.fit(X_train,Y_train)
 
from sklearn.svm import SVR
model = SVR(kernel = 'rbf')
model.fit(X_train,Y_train)

from xgboost import XGBClassifier
model = XGBClassifier()
model.fit(X_train,Y_train)

from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors = 5,metric = 'manhattan')
model.fit(X_train,Y_train)

from sklearn.linear_model import Lasso
model = Lasso()
model.fit(x_train,y_train)

from sklearn.linear_model import Ridge
model = Ridge()
model.fit(x_train,y_train)

from sklearn.linear_model import ElasticNet
model = ElasticNet()
model.fit(x_train,y_train)

import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras import optimizers

sgd = optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)

model = Sequential()
model.add(Dense(units = 3, activation = 'relu', input_shape=(3,)))
 
model.add(Dense(units = 300, activation = 'relu'))
model.add(Dense(units = 300, activation = 'relu'))
 
model.add(Dense(units = 1, activation = 'sigmoid'))
model.compile(optimizer = 'adam', loss = 'binary_crossentropy',metrics=['accuracy'])

model.fit(X_train,y_train, batch_size = 32, epochs = 1000)

y_pred = model.predict(X_test)
y_pred_D = sc_y.inverse_transform(y_pred)

score = model.evaluate(X_test,Y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

from sklearn.model_selection import cross_val_score
test = cross_val_score(estimator = model,X=X_train,y=Y_train,cv=10, scoring=None)

print(test.mean())
print(test.std())

model.summary()



y_pred = model.predict(X_test)
y_pred = (y_pred>.50)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)


