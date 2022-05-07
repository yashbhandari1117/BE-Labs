import pandas as pd
import numpy as np

dataset = pd.read_csv("dataset.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,2].values

print("X: ",X)
print("Y: ",y)

# Import KNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X,y)

# Predict the class of point (6,6)

x_test = np.array([6,6])
y_pred = classifier.predict([x_test])
ans  = ""

if y_pred[0] =='negative':
    ans = "orange"
else:
    ans = "blue"

print('\nGeneral KNN : ', y_pred[0],'(', ans, ')')

# Distance Weighted KNN

classifier = KNeighborsClassifier(n_neighbors=3, weights='distance')
classifier.fit(X,y)

# Predict the class of point (6,6)

x_test = np.array([6,6])
y_pred = classifier.predict([x_test])
ans  = ""

if y_pred[0] =='negative':
    ans = "orange"
else:
    ans = "blue"

print('\nDistance Weighted KNN : ', y_pred[0],'(', ans, ')')

# Using Iris Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['Species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print("\nIris Dataset:-\n",df)

df['Species'].value_counts()

df.isnull().sum()

X = df.iloc[:,:4]
X = preprocessing.StandardScaler().fit_transform(X)
y = df['Species']

X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=1)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print("Accuracy:- ", acc)

conf_matrix = confusion_matrix(y_test,y_pred)

sns.heatmap(conf_matrix,annot=True,fmt="d")
plt.ylabel = "Actual"
plt.xlabel = "Predicted"
plt.title("Confusion Matrix")
print("\nConfusion Matrix:- \n",conf_matrix)
plt.show()
