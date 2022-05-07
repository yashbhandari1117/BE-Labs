import numpy as np
import pandas as pd

from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

dataset=pd.read_csv("D:\Yash\BE Lab Assignments\ML")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier=NearestCentroid()
classifier=classifier.fit(X,y)

neigh = KNeighborsClassifier(n_neighbors=3, weights='distance')
neigh.fit(X, y)

n = KNeighborsClassifier(n_neighbors=3)
n.fit(X, y)

y_pred=classifier.predict(X)
y_p=neigh.predict(X)
y_pn=n.predict(X)

print(str(accuracy_score(y,y_pred)))

print(str(accuracy_score(y,y_p)))

print(str(accuracy_score(y,y_pn)))



