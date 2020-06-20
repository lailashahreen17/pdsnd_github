### Date created
June 20th, 2020

### Project Title
Bikeshare Data Analysis for cities

### Description
In this project, I explored three different datasets on bike share information provided by Motivate at three large cities such as Chicago, New York City and Washington.To identify what kind of data are shared and also to better understand the descriptive statistics, trip information, user type etc., I wrote the Python script to extract respective column/s and then analyzed the info.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

 1.Start Time (e.g., 2017-01-01 00:07:57)
 2.End Time (e.g., 2017-01-01 00:20:53)
 3.Trip Duration (in seconds - e.g., 776)
 4.Start Station (e.g., Broadway & Barry Ave)
 5.End Station (e.g., Sedgwick St & North Ave)
 6.User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

 1.Gender
 2.Birth Year

# Question Answered
1. What is the most frequent times of travel ( Month, day, hour)?
2. What is the the most popular stations and trip( start-station, end station, popular route)?
3. What are the total travel time and average travel time by users?
4. Who are the most frequent traveler (Gender type, age information, customer type)?

Raw input is solicited and handled correctly to guide the interactive question-answering experience so that no errors are thrown when unexpected input is entered.Descriptive statistics are correctly computed and used to answer the questions posed about the data. Raw data is displayed upon request by the user in this manner: Script should prompt the user if they want to see 5 lines of raw data, display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.

### Files used
Three files containing less amount of data are downloaded and then used for the exploration.
 1.chicago.csv
 2.new_york_city.csv
 3.washington.csv

### Credits
# Software Used for Analysis
1.Jupyter Notebook
2.Pandas library and Numpy
3.https://www.geeksforgeeks.org/python-pandas-series-str-cat-to-concatenate-string/
4.https://wiki.python.org/moin/WhileLoop
5.Stack Overflow and previous practice quiz have helped to solve the questions if I got stuck somewhere.
