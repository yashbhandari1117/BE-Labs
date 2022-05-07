import numpy as np
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
data = {
    'age': ['<21', '<21', '21-35', '>35', '>35', '>35', '21-35', '<21', '<21', '>35', '<21', '21-35', '21-35', '>35'], 
    'income':['high','high','high','medium','low','low','low','medium','low','medium','medium','medium','high','medium'],
    'gender':['male','male','male','male','female','female','female','male','female','female','female','male','female','male'],
    'marital_status':['single', 'married', 'single', 'single', 'single', 'married', 'married', 'single', 'married','single','married','married','single','married'],
    'buys':['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
} 
df = pd.DataFrame.from_dict(data) 

X=df.iloc[:,[0,1,2,3]].values
y=df.iloc[:,-1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
encoder=LabelEncoder()
X_train[:,0]=encoder.fit_transform(X_train[:,0])
X_train[:,1]=encoder.fit_transform(X_train[:,1])
X_train[:,2]=encoder.fit_transform(X_train[:,2])
X_train[:,3]=encoder.fit_transform(X_train[:,3])
X_test[:,0]=encoder.fit_transform(X_test[:,0])
X_test[:,1]=encoder.fit_transform(X_test[:,1])
X_test[:,2]=encoder.fit_transform(X_test[:,2])
X_test[:,3]=encoder.fit_transform(X_test[:,3])
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier = classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
op=classifier.predict([[1,1,0,0]])
print("Prediction for given input: ",op)
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print("Confusion Matrix: ")
print(cm)
acc=accuracy_score(y_test,y_pred)
print("Accuracy Score: ",acc)
