# Starbucks Portfolio Exercise

## Project Description

This portfolio exercise was originally used as a take-home assignment provided by Starbucks for their job candidates. This exercise involves an advertising promotion that was tested to see if it would bring more customers to purchase a specific product priced at $10. It costs the company 0.15 to send out each promotion. Ideally, we want to limit that promotion only to those that are most receptive to the promotion.

Our promotion strategy will be evaluated on 2 key metrics

Incremental Response Rate (IRR)
Net Incremental Revenue (NIR)
There are numerous approaches to tackle this problem. I have chosen to implement uplift models to optimize the promotional strategy. 3 different types of uplift models were implemented:

-  Two Models Approach
- Treatment Dummy Approach
- Four Quadrant Approach


## File Description
training.csv: Contains training data
Test.csv: Contains test data
Starbucks.ipynb: Contains code for the promotional strategy based on uplift models
test_results.py: Contains functions to evaluate the IRR and NIR values. File is provided by Starbucks.

## Instructions
Run Starbucks.ipynb

## Installations
Anaconda, XGBoost, Imblearn, Statsmodels, Seaborn
