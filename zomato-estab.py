import requests
import json

cuisines = "https://developers.zomato.com/api/v2.1/establishments?city_id={}"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ec8d07cd9f4ba5a10333320eb29ebf2d"}

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Indianapolis', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville', 'Baltimore', 'Oklahoma City', 'Louisville', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St Louis', 'Riverside', 'Corpus Christi', 'Lexington','Pittsburgh','Anchorage','Stockton','Cincinnati','Saint Paul','Toledo','Greensboro','Newark','Plano','Henderson','Lincoln','Buffalo','Jersey City','Chula Vista','Fort Wayne','Orlando','St Petersburg','Chandler','Laredo','Norfolk','Durham','Madison','Lubbock','Irvine','Winston–Salem','Glendale','Garland','Hialeah','Reno','Chesapeake','Gilbert','Baton Rouge','Irving','Scottsdale','North Las Vegas','Fremont','Boise','Richmond','San Bernardino']
city_ids = [280, 281, 292, 277, 287, 301, 304, 302, 276, 10883, 278, 718, 574, 306, 1021, 303, 10978, 285, 1168, 1144, 216, 305, 283, 289, 1138, 787, 1051, 745, 286, 282, 1267, 964, 466, 514, 499, 10924, 856, 11187, 1228, 288, 529, 946, 6890, 291, 10773, 5570, 1045, 1033, 730, 11175, 290, 496, 604, 640, 10611, 10924, 484, 844, 4772, 1174, 742, 1081, 415, 508, 1030, 10646, 1042, 4148, 3976, 11003, 5852, 943, 1012, 3959, 11250, 703, 601, 577, 11188, 1177, 10500, 907, 1264, 1189, 5863, 1060, 10959, 10992, 291, 976, 8111, 11193, 757, 10995, 11190, 282, 10796, 664, 1219, 10811]

dict = {}
zomato_data = []
dict['zomato_data'] = zomato_data

for city_id, city in zip(city_ids, city_list):
    response = requests.get(cuisines.format(city_id), headers=header)
    data_dict = {}
    data_dict['city'] = city
    data_dict['results'] = response.json()
    zomato_data.append(data_dict)

print(zomato_data)

#sorting data

list_cuisines = []
for item in zomato_data:
    cuisines = item['results']['establishments']
    c = []
    for cuisine in cuisines:
        c_type = cuisine['establishment']['name']
        c.append(c_type)
    list_cuisines.append(c)

# print(list_cuisines)

# with open('list-cuisines.json', 'w', encoding='utf-8') as f:
#     json.dump(list_cuisines, f, ensure_ascii=False, indent=2)

# counts = []

# for item in list_cuisines:
#     print(item)
#     counts.append(len(item))
# print(counts)


sorted_data = {}
cuisines_by_city = []
sub_dict = {}

for city, cuisine in zip(city_list, list_cuisines):
    sub_dict = {}
    sub_dict['city'] = city
    sub_dict['cuisines'] = cuisine
    cuisines_by_city.append(sub_dict)



sorted_data['data'] = cuisines_by_city

with open('zomato-establishments.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=4)



