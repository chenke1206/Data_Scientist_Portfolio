# Using Spark to Predict Churn
A binary classification problem solved with Spark and Spark's ML.
[Medium Post](https://medium.com/@corrinechen6/predict-customer-churn-with-pyspark-and-machine-learning-981d1eedb00b)

## Project Motivation
This project serves as an exploration of how to make a churn-prediction model using Spark, with the following steps included:

- explore and manipulate our dataset
- engineer relevant features for our problem
- split data into train and test sets by sampling churn
- build binary classifier models with Spark’s DataFrame-based ML

## Dependencies
- python==3.7.3
- pyspark==2.4.4
- spark-stratifier==0.1.5
- numpy
- pandas
- matplotlib
- seaborn
- jupyterlab

## Files Explanation
- Sparkify (local).ipynb
  - A notebook contains all the analysis codes that could be run on local machine.
- Sparkify (AWS).ipynb
  - A notebook contains all the analysis codes that could be run on AWS.


## Analysis Results
- Best model: Random Forest Classifier with PCA
- Best f1-score: 0.9992479970393414
