# Customer purchase prediction _ Online Shopping Mall

### Overview

Data driven approach in Machine Learning requires deep understanding of data itself. From Naver Boostcamp Ai Tech, students participate bootcamp to understand ongoing problems and tasks in the industry and apply up-to-date methodology based on corresponding prerequisite theories. 

'Online Shopping Mall Customer Purchase Prediction' is to design algorithm to predict whether each customer's total purchase in specific month will be greater than $3 million, which is not given as train data. Regard of in-class competition, students were provided with baseline code, which requires the minimum pipeline of machine learning.



### Dataset

Online mall transaction data is provided with CSV tabular data. train and test data are given in that order_date from 2009.12 to 2011.11. We predict each customer's purchase a month later on 2011.12. Its probability can be filled across user_id column, which is index of test dataset.

Under given period in dataset, goal is to estimate probability. This is binary classification problem in that prediction on total data based on previous contiguous months' activities. Probability describes whether each customer purchase total amount exceeds $200. Metric is AUC(Area Under Curve).

![image-20210529211105843](C:\Users\JUNGHYUN LEE\AppData\Roaming\Typora\typora-user-images\image-20210529211105843.png)

#### train.csv

* order_id
* product_id
* description
* quantity
* order_date
* price
* cutomer_id
* country
* total



### Machine Learning Pipeline

![image-20210530115350142](C:\Users\JUNGHYUN LEE\AppData\Roaming\Typora\typora-user-images\image-20210530115350142.png)

* EDA : Statistic features, reasoning data, feature correlation
* Data Preprocessing: Missing value, Continuous feature to categorical feature, vice versa.
* Feature Engineering: Candidate features and its combination
* Model Selection: Validating model combination(LightGBM, XGBoost)
* CV Strategy: random split stratefied k-fold
* Ensemble: Average ensemble