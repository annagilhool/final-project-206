import requests
import json
import time

cuisines = "https://developers.zomato.com/api/v2.1/establishments?city_id={}"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ec8d07cd9f4ba5a10333320eb29ebf2d"}

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Indianapolis', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville', 'Baltimore', 'Oklahoma City', 'Louisville', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St Louis', 'Riverside', 'Corpus Christi', 'Lexington','Pittsburgh','Anchorage','Stockton','Cincinnati','Saint Paul','Toledo','Greensboro','Newark','Plano','Henderson','Lincoln','Buffalo','Jersey City','Chula Vista','Fort Wayne','Orlando','St Petersburg','Chandler','Laredo','Norfolk','Durham','Madison','Lubbock','Irvine','Winston–Salem','Glendale','Garland','Hialeah','Reno','Chesapeake','Gilbert','Baton Rouge','Irving','Scottsdale','North Las Vegas','Fremont','Boise','Richmond','San Bernardino']
# needed city ids for API request
city_ids = [280, 281, 292, 277, 287, 301, 304, 302, 276, 10883, 278, 718, 574, 306, 1021, 303, 10978, 285, 1168, 1144, 216, 305, 283, 289, 1138, 787, 1051, 745, 286, 282, 1267, 964, 466, 514, 499, 10924, 856, 11187, 1228, 288, 529, 946, 6890, 291, 10773, 5570, 1045, 1033, 730, 11175, 290, 496, 604, 640, 10611, 10924, 484, 844, 4772, 1174, 742, 1081, 415, 508, 1030, 10646, 1042, 4148, 3976, 11003, 5852, 943, 1012, 3959, 11250, 703, 601, 577, 11188, 1177, 10500, 907, 1264, 1189, 5863, 1060, 10959, 10992, 291, 976, 8111, 11193, 757, 10995, 11190, 282, 10796, 664, 1219, 10811]


#creates dictionary that will be written to json file
dict = {}
zomato_data = []
dict['zomato_data'] = zomato_data

#looping through cities and city ids to making a call to api to retrieve data
#appending this data to zomato_data list

for city_id, city in zip(city_ids, city_list): # loops through both city list of names and city ids 
    response = requests.get(cuisines.format(city_id), headers=header)
    data_dict = {}
    data_dict['city'] = city
    data_dict['results'] = response.json()
    zomato_data.append(data_dict)

#sorting data
#looping through zomato_data and getting only the establishments' names for each city
#appending the establishemnts to a new list (c)
#then appending that list (c) to new list so we have a list of lists

count = 0

list_cuisines = []

for item in zomato_data:
    try:
        cuisines = item['results']['establishments']
        c = []
        for cuisine in cuisines:
            c_type = cuisine['establishment']['name']
            c.append(c_type)
        list_cuisines.append(c)
        count += 1
        if count % 10 == 0:
            print('pausing for a bit...')
            time.sleep(5)
    except:
        continue

last_entry = zomato_data[-1]
names = []
l = last_entry['results']['establishments']
for item in l:
    name = item['establishment']['name']
    names.append(name)
list_cuisines.append(names)


#making a dictionary of a list of dictionaries to append to json file

sorted_data = {}
cuisines_by_city = []
sub_dict = {}

#looping through cities and list of establishments creating a sub_dict
#appending this sub_dict to a list

for city, cuisine in zip(city_list, list_cuisines):
    sub_dict = {}
    sub_dict['city'] = city
    sub_dict['establishments'] = cuisine
    cuisines_by_city.append(sub_dict)

#making dictionary equal to a list of dictionaries

sorted_data['data'] = cuisines_by_city

#writing dictionary to json file zomato-establishment.json

with open('zomato-establishments.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=4)





