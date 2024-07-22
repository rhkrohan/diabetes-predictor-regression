# Diabetes Prediction Analysis 
## Introduction
This project aims to predict the likelihood of diabetes in patients using various regression techniques. The dataset includes 16 symptoms as features and is sourced from a reliable dataset on Kaggle. The data preprocessing is performed using modules from the sklearn library.

The dataset is split into training and testing sets with a ratio of 80:20. Multiple regression models are trained on the training data and their performance is evaluated using the R² score and a custom accuracy function, which calculates the percentage of correctly predicted results.

The models applied in this project are:

1. Multiple Linear Regression
2. Polynomial Regression
3. Support Vector Regression (SVR)
4. Decision Tree Regression
5. Random Forest Regression

The performance of each model is thoroughly analyzed to determine the most effective technique for predicting diabetes based on the given symptoms.
## Data Preprocessing
The dataset used in this project is comprehensive and well-prepared, containing a total of 521 observations with no missing values. Each observation represents a patient, and the dataset includes various symptoms and demographic information.

*Dataset Overview* \
**Number of Observations:** 521 \
**Symptom Categories:** The dataset includes 16 symptoms, which are used as features to train the models. The symptoms are primarily categorical, with responses like "Yes" or "No". \
**Age Group:** The dataset includes patients from various age groups, although specific age ranges are not explicitly detailed in the dataset. \

## Data Encoding
The dataset's symptoms are labeled with categorical values, typically "Yes" or "No". To prepare the dataset for machine learning models, we used the OrdinalEncoder from sklearn.preprocessing to convert these categorical values into numerical values (1 for "Yes" and 0 for "No"). This transformation is crucial for enabling the regression models to process and learn from the dataset effectively.

### Dataset Details
**Symptom Names:** The labels for the symptoms are used to identify each feature in the dataset.
**Categorical Nature:** Most of the dataset features are categorical, necessitating the use of encoding techniques to convert them into a numerical format suitable for model training.
This preprocessing step ensures that the data is in the correct format for training the machine learning models, allowing for accurate predictions and analysis.



