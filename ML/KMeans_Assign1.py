import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

X=[[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]

centroids=np.array([[0.1,0.6],[0.25,0.5]])

kmeans=KMeans(n_clusters=2,init=centroids)
kmeans.fit(X)
print("Labels after trainig:",kmeans.labels_)

#Q1
print("P6 belongs to ",kmeans.labels_[5],"cluster")

#Q2
print("Population around centroid 2(P6) is ",np.count_nonzero(kmeans.labels_==1))

#Q3
print("New values of centroids are:",kmeans.cluster_centers_)


from sklearn import datasets
iris=datasets.load_iris()
iris_x=iris.data

wcss=list()
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++')
    kmeans.fit(iris_x)
    wcss.append(kmeans.inertia_)

#plt.plot(range(1,11),wcss)
#plt.xlabel('No. of clusters')
#plt.ylabel('WCSS')
#plt.show()

kmeans=KMeans(n_clusters=3,init='k-means++')
kmeans.fit(iris_x)
y_means=kmeans.predict(iris_x)

plt.scatter(iris_x[y_means==0,0],iris_x[y_means==0,1],c='blue',s=100,label='iris_sertosa')
plt.scatter(iris_x[y_means==1,0],iris_x[y_means==1,1],c='yellow',s=100,label='iris_versicolour')
plt.scatter(iris_x[y_means==2,0],iris_x[y_means==2,1],c='green',s=100,label='iris_versginica')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c='red',s=100,label='centroids')
plt.legend()
plt.show()
    

