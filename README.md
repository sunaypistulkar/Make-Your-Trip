# Make Your Trip...

## ==Table of content==
[Demo]
[Overview]
[Motivation]
[Technical Aspect]
[Installation]
[Technology Used]
[Team]

## Demo
Link: https://yourtrippss.herokuapp.com
![20220206_154152](https://user-images.githubusercontent.com/98392987/152691171-43984394-59e8-4b8e-9ee1-b58a76bf397e.jpg)

## Overview
This application is multiclass classification model in machine learning. It takes inputs from user (like departure, flight-budget, hotel-rating, accomodation-budget and COVID risk) and tries to suggest destinations based on their preferences.

## Motivation
Service-sector's working environment has changed drastically, employees are working from their homes for last 2 years. Everyone wants some change in their routine, thats why I came up with this application, which would suggest places according to persons need so they can work and enjoy the change simultaneously, the suggested places has the greate internet connectivity so their work commitments won't suffer.


## Technical Aspect
Project consists of two parts

A) Training a Machine Learning Model using random forest classification.
1. To train the mdoel with highest accuracy, I have used hyperparameter tuning with GridSearchCV to get optimize parameters. 
2. Eventually I comemnt it down as it was slowing down the runtime.
3. While splitting the data into train and test, used 'stratify' parameter to increase the accuracy.

B) Building & hosting the application on Heroku!
1. Used streamlit to build an interface.
2. Used git version control to make it visible on all the platforms
3. Used git to push files at Heroku master.

## Installation
The code for the application is written in Python 3.8. If your system doesn't have Python installed, you can use following link to install! To install required packages and libraries use the following command.
Installation: https://www.python.org/downloads/
Libraries: pip install -r requirements.txt

## Technology Used
[Python](https://python.org/), [Scikit-Learn](https://scikit-learn.org/stable/), [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Streamlit](https://streamlit.io/), [Heroku](https://dashboard.heroku.com/)

## Team
[Sunay Pistulkar](https://github.com/sunaypistulkar)
