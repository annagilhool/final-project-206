import sqlite3
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def get_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def db_join(cur, conn):
    cur.execute('SELECT Establishments.cities, `Establishment Count`, `Cuisine Count` FROM Establishments INNER JOIN Cuisines WHERE Establishments.cities = Cuisines.cities')
    cusine_estab_counts = cur.fetchall()
    conn.commit()
    return cusine_estab_counts

def chart_1(tup_list):
    labels = []
    estab_count = []
    cusine_count = []
    for item in tup_list[:50]:
        labels.append(item[0])
        estab_count.append(item[1])
        cusine_count.append(item[2])

    
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.bar(x - width/2, estab_count, width, label='Establishment Count')
    ax.bar(x + width/2, cusine_count, width, label='Cuisine Count')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set(ylabel='Count', xlabel='Cities', xticklabels=labels, xticks=(x + width / 4), title='Establishment and Cuisine Count by City')
    ax.legend()
    fig.tight_layout()
    fig.savefig('estab-cuisine-count.png')
    plt.show()

def db_yelp_pricing(cur, conn):
    cur.execute('SELECT avg_price FROM `Restaurants and Pricing`')
    pricing = cur.fetchall()
    conn.commit()
    return pricing


def chart_2(tuplist):
    moderate_count = 0
    pricey_count = 0
    for item in tuplist:
        if item[0] == 'Moderate':
            moderate_count += 1
        elif item[0] == "Pricey":
            pricey_count += 1
    percentage_moderate = (moderate_count / 100) * 100
    percentage_pricey = (pricey_count / 100) * 100

    labels = ['Moderate', 'Pricey']
    sizes = [percentage_moderate, percentage_pricey]
    explode = (0, 0.1)

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=350)
    ax.set(title='Average Restaurant Pricing in Top 3 Restaurants in the 100 Most Popular US Cities')
    ax.axis('equal')

    fig.savefig('average-pricing.png')

    plt.show()

def db_yelp_rating(cur, conn):
    cur.execute('SELECT cities, avg_rating FROM `Restaurants and Ratings`')
    rating = cur.fetchall()
    conn.commit()
    return rating

def chart_3(tuplelist):
    labels = []
    values = []
    for item in tuplelist[:50]:
        labels.append(item[0])
        values.append(item[1])

    x = np.arange(len(labels))  # the label locations
    width = 0.5  # the width of the bars
    
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.bar(x - width/2, values, width, color='#db91b2', align='center')
    ax.set(title='Average Restaurant Ratings by City', xlabel='Cities', ylabel='Average Rating', xticklabels=labels, xticks=(x - width / 2))
    plt.gcf().subplots_adjust(bottom=0.45)

    fig.savefig('average-rating.png')

    plt.show()


cur, conn = get_database('final.db')
tuples = db_join(cur, conn)
chart_1(tuples)
tuples2 = db_yelp_pricing(cur, conn)
chart_2(tuples2)
tuple3 = db_yelp_rating(cur, conn)
chart_3(tuple3)
