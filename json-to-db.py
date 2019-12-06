import sqlite3
import os
import json

# reading data from restaurant json file

full_path = os.path.join(os.path.dirname(__file__), "yelp-resaurant-data.json")
f = open(full_path)
rest_data = f.read()
f.close()
json_rest_data = json.loads(rest_data) # now a dictionary


# reading data from hotel json file

full_path = os.path.join(os.path.dirname(__file__), "yelp-hotel-data.json")
f = open(full_path)
hotel_data = f.read()
f.close()
json_hotel_data = json.loads(hotel_data) # now a dictionary


# setting up database

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"final.db")
cur = conn.cursor()

# creating table for cities with top 5 restaurants and average rating and price
cur.execute("DROP TABLE IF EXISTS `Top 5 Restaurant Results by Location`")
cur.execute("CREATE TABLE `Top 5 Restaurant Results by Location` (cities TEXT PRIMARY KEY, #1 TEXT, #2 TEXT, #3 TEXT, #4 TEXT, #5 TEXT, `Average Rating` INTEGER, `Average Price` TEXT)")


# writing json restaurant data to database for ratings 

for data in json_rest_data['yelp_data']:

    sql_query = "INSERT INTO `Top 5 Restaurant Results by Location` (cities, #1, #2, #3, #4, #5, 'Average Rating`, `Average Price`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    data = data['city']
    results = data['results'] # dictionary 
    top5 = results['Top 3']
    ratings = results['Ratings']


# writing json restaurant data to database for prices 


for data in json_rest_data['yelp_data']:

    sql_query = "INSERT INTO `Top 5 Restaurant Results by Location` (cities, #1, #2, #3, #4, #5, 'Average Rating`, `Average Price`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    data = data['city']
    results = data['results'] # dictionary 
    top5 = results['Top 3']
    prices = results['Prices']


    