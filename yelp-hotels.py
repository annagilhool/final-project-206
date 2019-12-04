import requests
import json

api_key='rW11rA7zdWapU9FiLWzVDCMWzGIVoaZ3zH-owUmUwpPd_ot9NAMVLRn50AWmwWbAsiBu9vxEk_9u-aLuHQA_gxf7ZEXhFAMkaTJsusOZAIsGAJ8C3vr1AAzGGM7lXXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

dict = {}
yelp_data = []
dict['yelp_data'] = yelp_data
# print(dict)

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Indianapolis', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville', 'Baltimore', 'Oklahoma City', 'Louisville', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St Louis', 'Riverside', 'Corpus Christi', 'Lexington','Pittsburgh','Anchorage','Stockton','Cincinnati','Saint Paul','Toledo','Greensboro','Newark','Plano','Henderson','Lincoln','Buffalo','Jersey City','Chula Vista','Fort Wayne','Orlando','St Petersburg','Chandler','Laredo','Norfolk','Durham','Madison','Lubbock','Irvine','Winston–Salem','Glendale','Garland','Hialeah','Reno','Chesapeake','Gilbert','Baton Rouge','Irving','Scottsdale','North Las Vegas','Fremont','Boise','Richmond','San Bernardino']

for i in city_list:

    # User input
    # location = input("What city do you want to travel to: ")


    params = {'term':'hotels','location': i}

    #making dict
    data_dict = {}
    data_dict['city'] = i
    data_dict['results'] = {}
    
    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)
    
    # proceed only if the status code is 200
    # print('The status code is {}'.format(req.status_code))

    data = json.loads(req.text)

    #writing to a json file
    with open('yelp-restaurant-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # list of hotels
    hotels = data['businesses']

    #restaurants with rating >= 4.5
    # top_rest = []
    # for rest in restaurants: 
    #     if str(rest['rating']) == '4.5' or str(rest['rating']) == '5.0':
    #         print(type(str(rest['rating'])))
    #         top_rest.append([rest['name'], rest['rating']])

    # print(top_rest)

    #top 5 hotel results
    top_hotel = []
    names = []
    count = 0
    for hotel in hotels:
        if count < 5:
            top_hotel.append(hotel)
            names.append(hotel['name'])
            count += 1
        else:
            break
    # print(top_hotel)

    data_dict['results']['Top 5'] = names

    #gathering top 5 results ratings
    top_hotel_ratings = []
    for hotel in top_hotel:
        top_hotel_ratings.append([hotel['name'], hotel['rating']])
    # print(top_hotel_ratings)

    #average rating of top five results
    ratings = []
    for hotel in top_hotel_ratings:
        ratings.append(hotel[1])
    average_rating = sum(ratings)/len(ratings)
    # print(average_rating)

    data_dict['results']['Average Rating'] = average_rating

    #gathering top 5 results prices
    top_hotel_price = []
    for hotel in top_hotel:
        try:
            top_hotel_price.append([hotel['name'],hotel['price']])
        except:
            continue
    # print(top_rest_price)

    #converting price to int
    for hotel in top_hotel_price:
        if hotel[1] == "$":
            hotel[1] = 1
        elif hotel[1] == "$$":
            hotel[1] = 2
        elif hotel[1] == "$$$":
            hotel[1] = 3
        elif hotel[1] == "$$$$":
            hotel[1] = 4
        
    # print(top_rest_price)

    #averaging the price
    prices = []
    for hotel in top_hotel_price:
        prices.append(hotel[1])
    average_price = sum(prices)/len(prices)
    # print(average_price)

    final_price = average_price

    if average_price <= float(1):
        final_price = 'Inexpensive'
    elif average_price <= float(2):
        final_price = "Moderate"
    elif average_price <= float(3):
        final_price = "Pricey"
    elif average_price <= float(4):
        final_price = "Ultra High-End"

    # print(final_price)

    data_dict['results']['Average Price'] = final_price

    #making dictionary
    yelp_data.append(data_dict)

dict['yelp_data'] = yelp_data
print(dict)

# with open('yelp-hotel-data.json', 'w', encoding='utf-8') as f:
#         json.dump(dict, f, ensure_ascii=False, indent=4)



