**PROJECT TITLE - Commercial Sales Prediction Analysis using Regression**

**Dataset Information**

The data scientists at BigMart have collected 2013 sales data for 1559 products across 10 stores in different cities. Also, certain attributes of each product and store have been defined. The aim is to build a predictive model and find out the sales of each product at a particular store.

Using this model, BigMart will try to understand the properties of products and stores which play a key role in increasing sales.

**MODELS USED**

In order to maintain successful business, marketing
enterprises like bigmart engaged in wholesaling,
manufacturing, logistics and retailing should predict their
sales before actual sales. Marketing enterprises account over
10% of the country’s GDP. It is essential for them need to
analyze and predict their sales for avoiding unnecessary
expenditure. A marketing enterprise should have a model that
can predict sales accurately so that customers future demands
can be met and accordingly update their sales record. To
achieve this, dataset of Big Mart Sales is collected and used
for analysis of sales of each product at a particular store. Data
exploration, preprocessing, exploratory data analysis and
model training methodology is followed for building a
predictive model. This paper explores all basic regression
algorithms models like linear regression, decision tree,
random forest, lasso, ridge and extra-trees regressor for
predicting and improving sales with a promising accuracy.

**LIBRARIES NEEDED**

- numpy
- pandas
- matplotlib
- seaborn

**DATASET**

https://www.kaggle.com/devashish0507/big-mart-sales-prediction

**INTRODUCTION**
It is often assumed that more sales means more profit. One
thing marketing enterprises must have thought when
increasing sales and profits is the natural desperation for
avoiding loses and unneeded expenditure. That desperation
without a proper plan can cause downfall of the entire
enterprise. The dataset collected have defined attributes that
has numerous dependent and independent variables. Then, the
data of the dataset is filtered to get accurate predictions and
get some good results that help us to improve knowledge on
the data we collected. This knowledge on dataset can further
be used for predicting future sales of commercial products by
applying machine learning algorithms like random forest and
basic linear regression.

**LITERATURE SURVEY**
The BigMart dataset is a collection sales data of 2013. The
dataset is divided into 11 input attributes and 1 output
attribute. Training on the model is done on 1559 products
across 10 stores in different cities.

**About the Dataset**
The Dataset is collected from Kaggle. It has tabular data that
corresponds to one or more database tables. Every column of
the table represents a particular variable and each row
corresponds to a given record of the dataset gathered by the
reviews of the customers. Then, the data of the dataset is
filtered to get accurate predictions and get some good results
that help us to improve knowledge on the data we collected.
Sample Data and Basic Analysis on the dataset Screenshots:
The dataset has some missing values as other attributes have
close by values, thus attributes needs to be processed
separately. Unique values in the data set are checked by using
the Lambda function. Preprocessing is performed on the
dataset. Firstly null values are checked and then categorical
attributes are checked. Item and outlet identifier are discarded
which increases the accuracy of the model. Further missing
values are filled by the mean values and if the values of some
attributes are less than 100 we combine them to similar
categories and then check the final count.
Fig. 1.1 Contents of Dataset
Fig. 1.2 Display of Dataset Attributes
Fig. 1.3 Dataset Null Values Check
Fig. 1.4 Dataset Statistical Information
New attributes are created using Lambda function. Old values
are mapped to new values. 3 broad categories are the
observed. Futher we create one new attribute it is noticed that
outlet establishment here is reducing the performance of the
model. So new value which is lesser is subtracted from the year
2013 with the following years mentioned in outlet
establishment year column.

**Hypothesis Generation**
Data Exploration
Data Cleaning
Feature Engineering
Model Building
Hypothesis Generation
Understanding the problem better by brainstorming possible
factors that can impact the outcome
Data Exploration
Analysis of the data to uncover the patterns, point of interest
and characteristics.
Data Cleaning
Modification of the data based on missing values identification.
Feature Engineering
Modifying existing variables and creating new ones for analysis.
Model Building
Making predictive models on the data.
Hypothesis about the data was made and data exploration was
performed where some subtle differences in data was found,
which required remediation. Next, data cleaning was
performed. Then, feature engineering was performed where
missing values were imputed and solved the irregularities. New
features where included and this made data model friendly by
one hot encoding. Finally some basic models were imported to
find out which one among them gave the best performance.

**IMPLEMENTATION**

1. Software
   To run the regression model, following packages are
   required.
    NumPy
    Seaborn
    Matplotlib
    Pandas
    Warnings
2. Exploratory Analysis And Observations with flow chart
   To understand the correspondence between the target
   variable and output variable the following graphs are
   plotted and observed. So quick exploration and
   visualization is performed on the data using sns.displot
   function as shown.
   Fig.3.1 Correspondence between target variable and
   Item_Weight
   As it can be seen that in Fig.3.1, there is a dominant
   peak obtained due to inclusion of mean values that was
   used to fill the missing values in the particular columns
   of the dataset. Also, it can be observed that most of the
   items have values as zero because they don’t have data.
   Fig.3.2 Correspondence between target variable and
   Item_Visibility
   As it can be seen that in Fig.3.2, the inclusion of mean
   values that was used to fill the missing values in the
   particular columns of the dataset is also the reason for
   obtaining dominant peak.
   Fig.3.3 Correspondence between target variable and
   Item_MRP
   As it can be seen that in Fig.3.3, there are four dominant
   peaks obtained in some intervals due to inclusion of
   mean values that was used to fill the missing values in
   the particular columns of the dataset.
   Fig.3.4 Correspondence between target variable and
   Item_Outlet_Sales
   As it can be seen that in Fig.3.4, values are high ranging
   from 0 to 14000. So normalization by using logarithm
   transformation is done over the graph and a uniform
   distribution is obtained as can be seen in Fig.3.5.
   Fig.3.5 Correspondence between target variable and
   Item_Outlet Sales Uniform Distribution
   As a result from Fig.3.5, values are some what minimal,
   so that the model can predict with less error.
   Further exploration is done over categorical
   distributions using countplot function.
   Fig.3.6 Correspondence between target variable and
   Item_Fat_Content
   As it can be seen that in Fig.3.6, most of the products
   are low fat content type and very less products are non
   edible type. For this matplotlib.pyplot is imported.
   Further similar approach is performed on the other
   attributes as shown.
   Fig.3.7 Correspondence between target variable and
   Item_Type
   Fig.3.8 Correspondence between target variable and
   Outlet_Establishment_Year
   Fig.3.9 Correspondence between target variable and
   Outlet_Size
   Fig.3.10 Correspondence between target variable and
   Outlet_Location_Type
   Fig.3.11 Correspondence between target variable and
   Outlet_Type

**Pseudocode**
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
def train(model, X, y):

model.fit(X, y)

pred = model.predict(X)

cv_score = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5)
cv_score = np.abs(np.mean(cv_score))

print("Model Report")
print("MSE:",mean*squared_error(y,pred))
print("CV Score:", cv_score)
from sklearn.linear_model import LinearRegression, Ridge, Lasso
model = LinearRegression(normalize=True)
train(model, X, y)
coef = pd.Series(model.coef*, X.columns).sort*values()
coef.plot(kind='bar', title="Model Coefficients")
model = Ridge(normalize=True)
train(model, X, y)
coef = pd.Series(model.coef*, X.columns).sort*values()
coef.plot(kind='bar', title="Model Coefficients") model = Lasso()
train(model, X, y)
coef = pd.Series(model.coef*, X.columns).sort*values()
coef.plot(kind='bar', title="Model Coefficients")
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
train(model, X, y)
coef = pd.Series(model.feature_importances*, X.columns).sort*values(ascending=False)
coef.plot(kind='bar', title="Feature Importance")
from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
train(model, X, y)
coef = pd.Series(model.feature_importances*, X.columns).sort_values(ascending=False)
coef.plot(kind='bar', title="Feature Importance")
RESULTS AND DISCUSSION

1. Correlation Matrix
   Fig.4 Correlation Matrix
   As it can be seen that in Fig.4, a correlation matrix is
   created that is displayed in a heat map. A particular
   color map can be chosen to display it.
   Following Observations are made:
    Item_Weight and Outlet_Establishment_Year are
   having good correlation.
    However, there is a clear difference between
   Outlet_Establishment_Year and Outlet_Years.
   They are having negative correlation.
    Form Item_Outlet_Sales we get to know which is
   highly impacting the prediction model.
    Therefore, Item_MRP gives the major impact to the
   outlet sales.
   Label encoding and One-hot encoding are performed. Initially,
   for label encoding, label encoder is imported. Firstly, the outlet
   identifier is converted into numerical values, based on the
   specific stores the prediction may be affected. For model
   improvement we converted categorical attribute into label
   encoder. We convert these categorical attributes into
   numerical values.
   For getting, more prediction in the model one hot encoding can
   be performed it will create new column and thus will increase
   accuracy of the model. It performs better for categorical
   attributes. Here, dummies keyword is used to represent one
   hot encoding. As a result, 26 features are obtained.
   Train test split process is performed on input variable output
   variable and a separate variable. For this, some attributes are
   dropped in input and output attributes columns. Cross
   validation can also be used to automatically split the dataset
   accordingly.
   Model training is performed and the following matrix, cross
   validation score and mean squared error is used. Here, the
   function having model, input which is denoted by x and output
   which is denoted by y is used. The training set is then predicted
   and cross validation is performed. The cross validation score is
   often by using negative mean squared error function. With this
   the model is defined.
2. Graphs from Model Training
   Some basic models are imported to analyze the
   performance of the training model. Based on the cross
   validation score, best model is picked.
   A. Linear Regression Model
   Fig.5.1 Linear Regression Model
   Model Report
   MSE: 0.2880838937683423
   CV Score: 0.28921756014145145
   B. Ridge Model
   Fig.5.2 Ridge Model
   Model Report
   MSE: 0.42802985605683475
   CV Score: 0.4289289251562643
   C. Lasso Model
   Fig.5.3 Lasso Model
   Model Report
   MSE: 0.7628688679102087
   CV Score: 0.7630789166281843
   D.Decision Tree Regressor Model
   Fig.5.4 Decision Tree Regressor Model
   Model Report
   MSE: 5.5534030638578795e-34
   CV Score: 0.5787926637055503
   E. Random Forest Regressor Model
   Fig.5.5 Random Forest Regressor Model
   Model Report
   MSE: 0.042468217567918444
   CV Score: 0.3098775587950489
   F. Extra Trees Regressor Model
   Fig.5.7 Extra Trees Regressor Model
   Model Report
   MSE: 1.0418489584965893e-28
   CV Score: 0.33222859882716604

**CONCLUSION**
Based on the reports obtained and analyzed on the
training model and dataset, linear regression has the top
performance. The study was focused on the 11 input
attributes and one output attribute thus, obtaining a
promising accuracy with the corresponding cv score.
Machine learning techniques have wide range of
applications. Many types of research and works are being
done on it.
