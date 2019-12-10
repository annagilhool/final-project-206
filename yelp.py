import requests
import json
import os

api_key='rW11rA7zdWapU9FiLWzVDCMWzGIVoaZ3zH-owUmUwpPd_ot9NAMVLRn50AWmwWbAsiBu9vxEk_9u-aLuHQA_gxf7ZEXhFAMkaTJsusOZAIsGAJ8C3vr1AAzGGM7lXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

dict = {}
yelp_data = [] 
dict['yelp_data'] = yelp_data

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Indianapolis', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville', 'Baltimore', 'Oklahoma City', 'Louisville', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St Louis', 'Riverside', 'Corpus Christi', 'Lexington','Pittsburgh','Anchorage','Stockton','Cincinnati','Saint Paul','Toledo','Greensboro','Newark','Plano','Henderson','Lincoln','Buffalo','Jersey City','Chula Vista','Fort Wayne','Orlando','St Petersburg','Chandler','Laredo','Norfolk','Durham','Madison','Lubbock','Irvine','Winston–Salem','Glendale','Garland','Hialeah','Reno','Chesapeake','Gilbert','Baton Rouge','Irving','Scottsdale','North Las Vegas','Fremont','Boise','Richmond','San Bernardino']

for i in city_list:

    params = {'term':'restaurants','location': i}

    #making dict
    data_dict = {}
    data_dict['city'] = i
    data_dict['results'] = {}

    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)

    data = json.loads(req.text)

    # list of restaurants
    restaurants = data['businesses']

    #top 5 rest results
    top_rest = []
    names = []
    count = 0
    for rest in restaurants:
        if count < 3:
            top_rest.append(rest)
            names.append(rest['name'])
            count += 1
        else:
            break

    data_dict['results']['Top 3'] = names

    #gathering top 3 results ratings
    top_rest_ratings = []
    for rest in top_rest:
        top_rest_ratings.append(rest['rating'])

    data_dict['results']['Ratings'] = top_rest_ratings

    #gathering top 3 results prices
    top_rest_price = []
    for rest in top_rest:
        try:
            top_rest_price.append(rest['price'])
        except:
            continue

    #converting price to int
    prices = []
    for rest in top_rest_price:
        if rest == "$":
            rest = 1
        elif rest == "$$":
            rest = 2
        elif rest == "$$$":
            rest = 3
        elif rest == "$$$$":
            rest = 4
        prices.append(rest)
        

    data_dict['results']['Prices'] = prices

    #making dictionary
    yelp_data.append(data_dict)

dict['yelp_data'] = yelp_data

# writing to json file

with open('yelp-restaurant-data.json', 'w', encoding='utf-8') as f:
    json.dump(dict, f, ensure_ascii=False, indent=4)

