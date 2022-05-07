from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import cross_val_score

diabetes = load_diabetes()

lr = LinearRegression(normalize = True)

lr_scores = cross_val_score(lr, diabetes.data, diabetes.target,cv=10)
print("Scores obtained by Linear Regression: ",lr_scores)
print("\nMean: ",lr_scores.mean())

## Ridge
rg = Ridge(0.005, normalize=True)
rg_scores = cross_val_score(rg, diabetes.data, diabetes.target, cv=10)
print("Scores obtained by Ridge Regression: ",rg_scores)
print("\nMean: ",rg_scores.mean())

## RidgeCV for set of alpha values, alpha_ to extract alpha value
from sklearn.linear_model import RidgeCV
rg = RidgeCV(alphas=(1.0, 0.1, 0.01, 0.005, 0.0025, 0.001, 0.00025),normalize=True)
rg.fit(diabetes.data, diabetes.target)
print(rg.alpha_)

rg_cv_scores = cross_val_score(rg, diabetes.data, diabetes.target, cv=10)
print("Scores obtained by RidgeCV Regression: ",rg_cv_scores)
print("\nMean: ",rg_scores.mean())

## Lasso, LassoCV
from sklearn.linear_model import Lasso, LassoCV
ls = Lasso(alpha=0.005, normalize=True)
ls_scores = cross_val_score(ls, diabetes.data, diabetes.target, cv=10)
print("Scores obtained by Lasso Regression: ",ls_scores)
print("\nMean: ",ls_scores.mean())

from sklearn.linear_model import LassoCV
ls_cv = LassoCV(alphas=(1.0,0.1,0.01,0.005,0.0025,0.001,0.00025),normalize=True)
ls_cv.fit(diabetes.data, diabetes.target)
ls_cv.alpha_

ls_cv_scores = cross_val_score(ls_cv, diabetes.data, diabetes.target,cv=10)
print("Scores obtained by LassoCV Regression: ",ls_cv_scores)
print("\nMean: ",ls_cv_scores.mean())

## ElasticNet, ElasticNetCV
from sklearn.linear_model import ElasticNet, ElasticNetCV
en = ElasticNet(alpha=0.001,l1_ratio=0.8, normalize=True)
en_scores = cross_val_score(en, diabetes.data, diabetes.target, cv=10)
print("Scores obtained by ElasticNet Regression: ",en_scores)
print("\nMean: ",en_scores.mean())

encv = ElasticNetCV(alphas=(0.1, 0.01,0.005, 0.0025, 0.001),l1_ratio=(0.1,0.25,0.5,0.75,
0.8), normalize=True)
encv.fit(diabetes.data, diabetes.target)

print(encv.alpha_)
print(encv.l1_ratio_)

encv_scores = cross_val_score(encv, diabetes.data, diabetes.target,cv=10)
print("Scores obtained by ElasticNetCV Regression: ",encv_scores)
print("\nMean: ",encv_scores.mean())

## Comparative analysis
#Linear Regression Score
print(lr_scores.mean())
#Ridge Score
print(rg_scores.mean())
#Lasso Score
print(ls_scores.mean())
#ElasticNet Score
print(en_scores.mean())

import matplotlib.pyplot as plt
import numpy as np
objects = ('Linear','Ridge','Lasso','ElasticNet')
y_pos = np.arange(len(objects))
p = [0.4619623619583371,0.4627580697072979,0.4628257255366856,0.46358858847836454]
plt.bar(y_pos, p, align='center',alpha=0.5, color=['hotpink', 'yellow', 'lime','cyan'])
plt.xticks(y_pos, objects)
plt.ylabel('Accuracy')
plt.title('Linear Models')

ElasticNetCV(alphas=(0.1, 0.01, 0.005, 0.0025, 0.001),

l1_ratio=(0.1, 0.25, 0.5, 0.75, 0.8), normalize=True)

plt.show()
