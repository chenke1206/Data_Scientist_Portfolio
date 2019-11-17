# Disaster Response Pipeline

## Overview

### Background:
Following a disaster, there are a number of different problems that could arise. Different types of disaster response organizations take care of different parts of the disasters and observe messages to better understand the needs of the situation. 

They have the least capacity to filter out messages during a large disaster, so predictive modeling can help classify different messages more efficiently.


This project used a data set from [Figure Eight](https://www.figure-eight.com/) that contained labeled disaster messages received by an aid organization. I built an ETL pipeline that cleaned messages using regex and NLTK. A multi-output Random Forrest classifier was trained using supervised learning with a natural language processing (NLP). 


An ETL pipeline was created, extracting data from csv files, cleaning and loading into an SQL database. A machine learning pipeline was created to extract the NLP features and then optimize the algorithm using grid search. A web app was then developed that extracts the initial data from the database and provides some interactive visual summaries. Users are also able to enter their own message to be classified by the algorithm.


## Technologies Used
- Python
  - Libraries: pandas, sklearn, sqlite3, sqlalchemy, nltk, plotly, flask, regex
- HTML
  - Bootstrap

## Project Details
### Web App
Users have the ability to enter their own message to be classified and see the classification results.

!['Example Classification'](https://github.com/chenke1206/Data_Scientist_Portfolio/blob/master/Project-2-disaster-response-pipeline/example.png)

They can also see a summary of the original dataset.
!['Summary'](https://github.com/chenke1206/Data_Scientist_Portfolio/blob/master/Project-2-disaster-response-pipeline/homepage.png)

### Machine Learning Considerations
One of the primary considerations for this dataset is that the majority of the categories are very imbalanced. In some cases, out of 20k messages, only a few hundred messages exist under a specific classification. Because of this imbalance, I used f-score as the performance metric for evaluating the model with 'micro' averaging.

Further work could be done to develop the algorithm by using anomaly detection machine learning techniques. 


### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python train_classifier.py ../data/DisasterResponse.db classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
