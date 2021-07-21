# **Loan Prediction Problem Dataset **


**GOAL**

#### The main objective for this dataset:

- Using machine learning techniques to predict loan payments.

- **target value**: Loan_Status

**DATASET**

Dataset can be downloaded from [here](https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset).



**WHAT I HAD DONE**

- Importing Libraries
- Preprocessing and Data Analysis 
- Missing values
- Data visalization
- Machine learning models
- 


**MODELS USED**

-  Logistic Regression
-  Random Forest Classifier
-  XGBoostClassifier
-  Decision Tree Classifier



**LIBRARIES NEEDED**

- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn

**Accuracy of different models used**

By using Logistic Regression I got 
 ```python
    test accuracy score of  Logistic Regression =  83%
 ``` 

By using Random Forest Classifier I got 
 ```python
    test accuracy score of Random Forest =  78.38%
 ``` 
 
 By using Decision Tree Classifier I got 
 ```python
    test accuracy score of Decision Tree =  70.27%
 ``` 
 
 By using XGBoost Classifier I got 
 ```python
    test accuracy score of XGBoost =  70.27%
 ``` 
 
 
 **Conclusion**
 
- Credit_History is a very important variable because of its high correlation with Loan_Status therefor showind high Dependancy for the latter.
- The **Logistic Regression algorithm** is the most accurate: **approximately 83%**.