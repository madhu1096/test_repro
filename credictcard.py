import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('ds_full.csv')
 
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
 



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.25,random_state=0)
#######################################################
from sklearn.preprocessing import RobustScaler
sc_x = RobustScaler()
X_train = sc_x.fit_transform(x_train)
X_test = sc_x.transform(x_test)

 
########################################################

from sklearn.preprocessing import MinMaxScaler
sc_x = MinMaxScaler()
X_train = sc_x.fit_transform(x_train)
X_test = sc_x.transform(x_test)

##################################################
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

#######################################################
from sklearn.linear_model import LogisticRegression
model =  LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test) 

###########################################################
from sklearn.neighbors import KNeighborsClassifier
model =  KNeighborsClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

###########################################################
from sklearn.svm import SVC
model =  SVC(kernel = 'rbf')
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

###########################################################
from sklearn.naive_bayes import GaussianNB
model =  GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

###########################################################
from sklearn.tree import DecisionTreeClassifier
model =  DecisionTreeClassifier(criterion = 'entropy')
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

###########################################################
from sklearn.ensemble import RandomForestClassifier
model =  RandomForestClassifier(n_estimators = 500,criterion = 'entropy')
model.fit(x_train,y_train)
y_pred = model.predict(x_test)



###########################################################
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred,y_test)
from sklearn.metrics import accuracy_score
per = accuracy_score(y_pred,y_test)






from sklearn.model_selection import cross_val_score
test = cross_val_score(estimator = model,X=x_train,y=y_train,cv=10, scoring=None)

print(test.mean())
print(test.std())

model.summary()



y_pred = model.predict(X_test)
y_pred = (y_pred>.50)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)


