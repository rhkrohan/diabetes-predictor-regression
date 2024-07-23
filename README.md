# Diabetes Prediction Analysis

## Introduction
This project aims to predict the likelihood of diabetes in patients using various regression techniques. The dataset includes 16 symptoms as features and is sourced from a reliable dataset on Kaggle. The data preprocessing is performed using modules from the sklearn library.

The dataset is split into training and testing sets with a ratio of 80:20. Multiple regression models are trained on the training data, and their performance is evaluated using the R² score and a custom accuracy function, which calculates the percentage of correctly predicted results.

The models applied in this project are:

1. Multiple Linear Regression
2. Polynomial Regression
3. Support Vector Regression (SVR)
4. Decision Tree Regression
5. Random Forest Regression

The performance of each model is thoroughly analyzed to determine the most effective technique for predicting diabetes based on the given symptoms.

## Data Preprocessing
The dataset used in this project is comprehensive and well-prepared, containing a total of 521 observations with no missing values. Each observation represents a patient, and the dataset includes various symptoms and demographic information.

### Dataset Overview
- **Number of Observations:** 521
- **Symptom Categories:** The dataset includes 16 symptoms, which are used as features to train the models. The symptoms are primarily categorical, with responses like "Yes" or "No".
- **Age Group:** The dataset includes patients from various age groups, although specific age ranges are not explicitly detailed in the dataset.

### Data Encoding
The dataset's symptoms are labeled with categorical values, typically "Yes" or "No". To prepare the dataset for machine learning models, we used the `OrdinalEncoder` from `sklearn.preprocessing` to convert these categorical values into numerical values (1 for "Yes" and 0 for "No"). This transformation is crucial for enabling the regression models to process and learn from the dataset effectively.

### Dataset Details
- **Symptom Names:** The labels for the symptoms are used to identify each feature in the dataset.
- **Categorical Nature:** Most of the dataset features are categorical, necessitating the use of encoding techniques to convert them into a numerical format suitable for model training.

This preprocessing step ensures that the data is in the correct format for training the machine learning models, allowing for accurate predictions and analysis.

## Visualization

The project includes various visualizations to help understand model performance and feature importance:

### Scatter Plot of Actual vs. Predicted Values

- Helps visualize how well the model's predictions match the actual values.
- Useful for identifying any patterns or biases in the predictions.

### Histogram of Residuals

- Shows the distribution of prediction errors to identify any patterns or biases.
- A normal distribution of residuals indicates a well-fitted model.

### Decision Tree Structure

- Visualizes the structure of the decision tree to understand the decision-making process.
- Helps in understanding the model's logic and identifying key decision points.

### Feature Importance

- Displays the importance of each feature in the Random Forest model.
- Useful for understanding which symptoms are most influential in predicting diabetes.

## Cross-Validation

The project implements cross-validation to ensure the models generalize well to unseen data. This technique splits the dataset into multiple folds and evaluates the model on each fold. The results provide insights into the model's consistency and performance across different subsets of the data.

### Analysis

- **Cross-Validation Scores**: Provide insight into the performance of the model on different subsets of the data.
- **Mean R² Score**: Gives an overall estimate of the model's performance.
- **Standard Deviation**: Indicates the consistency of the model's performance across different folds. Lower standard deviation suggests more consistent performance.

## Results and Analysis

In this section, we present the performance metrics of each regression model applied to predict the likelihood of diabetes in patients based on 16 symptoms. The models were evaluated using the R² score and the percentage accuracy of the predictions on the test set.

### Model Performance

| Model                       | R² Score | Accuracy (%) |
|-----------------------------|----------|--------------|
| Multiple Linear Regression  | 0.705    | 93.269       |
| Polynomial Regression       | 0.808    | 93.269       |
| Support Vector Regression   | 0.9461   | 100          |
| Decision Tree Regression    | 0.878    | 97.115       |

### Analysis

From the results, it is clear that the Support Vector Regression (SVR) model performed the best, achieving the highest R² score of 0.9461 and an accuracy of 100%. This indicates that SVR was able to capture the underlying patterns in the data most effectively among all the models tested.

The Decision Tree Regression also performed well, with an R² score of 0.878 and an accuracy of 97.115%, showing its ability to model non-linear relationships in the dataset.

Polynomial Regression, with a degree of 2, showed an improvement over Multiple Linear Regression, indicating that adding polynomial terms helps in capturing non-linear relationships in the data. However, it did not perform as well as SVR or Decision Tree Regression.

Multiple Linear Regression had the lowest performance, with an R² score of 0.705 and an accuracy of 93.269%. This is expected as linear models often struggle to capture non-linear relationships in the data.

### Detailed Analysis

#### Multiple Linear Regression

- **Why it Worked**: Multiple Linear Regression provides a simple model that is easy to interpret and can perform well on datasets with linear relationships.
- **Why it Didn't Work**: The dataset likely contains non-linear relationships between symptoms and the likelihood of diabetes, which a linear model cannot capture effectively. This is evident from its relatively lower R² score and accuracy.

#### Polynomial Regression

- **Why it Worked**: By introducing polynomial terms, the model can capture some non-linear relationships, leading to improved performance over Multiple Linear Regression.
- **Why it Didn't Work**: Although it captures more complexity than a linear model, it might still be insufficient to fully model the intricate relationships in the dataset compared to more advanced models like SVR and Decision Tree Regression.

#### Support Vector Regression (SVR)

- **Why it Worked**: SVR, especially with an RBF kernel, is effective at capturing complex non-linear relationships in the data. It projects data into higher dimensions where a linear separation is possible, leading to superior performance.
- **Why it Didn't Work**: Given its high performance, there are minimal drawbacks in this context, but SVR can be computationally intensive and sensitive to parameter settings.

#### Decision Tree Regression

- **Why it Worked**: Decision Tree Regression can model non-linear relationships and interactions between features effectively. It partitions the data into subsets based on feature values, capturing complex patterns.
- **Why it Didn't Work**: Decision Trees can overfit the training data, but this is mitigated here as the model performed well on the test set. However, it may still be less robust compared to ensemble methods like Random Forest.

### Conclusion

Based on the analysis, Support Vector Regression (SVR) emerged as the best-performing model for predicting diabetes in this dataset, followed by Decision Tree Regression. Polynomial Regression and Multiple Linear Regression, while useful, did not capture the complexity of the data as effectively. Future work could explore ensemble methods like Random Forest or Gradient Boosting for potentially even better performance.

[Link to the dataset](#) for further analysis and replication of results.



