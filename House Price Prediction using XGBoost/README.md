# House Price Prediction 

This is a project on House Price Prediction is based on *Python 3.8*. The data has been extracted from a CSV file.

## Packages Used:
1. pandas
2. sklearn
3. xgboost

## XGBoost

XGBoost, which stands for e**X**treme **G**radient **B**oosting, is a model used to work on standard tabular data (like DataFrames). It is an implementation of the **Gradient 
Boosted Decision Trees** algorithm.  XGBoost is preferred over other models because of its accuracy and speed. So, how does it work?

The process is cyclical. Models are built over and over and added to an "emsemble" model. The cycle is started by caculating the errors for each observation in the dataset. Then,
a model is built to predict those, this is added to the ensemble and then another model is built to predict the next errors. To make a prediction, we add the predictions from 
all previous models. We can use these predictions to calculate new errors, build the next model, and add it to the ensemble.

Before we start the cycle, we need a base prediction. This prediction could be pretty naive. Subsequent additions to the ensemble will reduce the errors.

Here are some links I referred to,

[Documentation of XGBoost](https://xgboost.readthedocs.io/en/latest/)

[Tutorial and explanation of XGBoost](https://www.kaggle.com/dansbecker/xgboost)

[Introduction to XGBoost for Machine Learning](https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/)

This project was made by [Deepesha Burse](https://github.com/deepeshaburse).
