# -*- coding: utf-8 -*-
"""diabetes_pred(Polynomial_Regression).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vcqnj2AtjpvMFkT7zRv8bJHaEpEV5Gl8

##Importing the Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""##Importing the Dataset"""

dataset = pd.read_csv('diabetes_data_upload.csv')
dataset.head()

"""##Seperation of Dependent and Independent variables"""

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

print(X)

print(y)

"""#Data Preprocessing"""

from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder()
X.iloc[:, 1:] = encoder.fit_transform(X.iloc[:, 1:])

y = encoder.fit_transform(y.array.reshape(len(y), 1))

print(X)

print(y)

"""##Splitting the data into Training and Test sets

"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""##Building the Polynmial Regression Model"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

polyX_regressor = PolynomialFeatures(degree = 2)
poly_Xtrain = polyX_regressor.fit_transform(X_train)

lin_regressor = LinearRegression()
lin_regressor.fit(poly_Xtrain, y_train)

"""##Predicting Results and Evaluating Model Perfromance"""

poly_Xtest = polyX_regressor.transform(X_test)
y_pred = lin_regressor.predict(poly_Xtest)

print(y_pred)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

"""##Determining Percentage Acuracy on Test Results"""

def accuracy(x_test, y_test, y_pred):
    correct = 0
    for i in range(len(y_pred)):
        if np.round(y_pred[i]) == y_test[i]:
            correct += 1
    accuracy = (correct / len(y_pred)) * 100
    return accuracy

accuracy_score = accuracy(X_test, y_test, y_pred)
print(f"Accuracy: {accuracy_score}%")

"""##Visualising the results"""

# Scatter plot of actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Values (Polynomial Regression, Degree 2)')
plt.show()

# Histogram of residuals
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=20, edgecolor='k')
plt.xlabel('Residual')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals (Polynomial Regression, Degree 2)')
plt.show()