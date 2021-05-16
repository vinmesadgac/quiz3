import requests
import json
import sqlite3


city = 'Tbilisi'
cnt = 16
key = '44ad3b126b3c17e05b920198af4ce15e'
url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={cnt}&appid={key}'
payload = {'q':city, 'appid':key, 'units':'metric'}
r = requests.get(url)
print(r.text)
print(r.headers)
print(r.status_code)
res = r.json()
print(res)
with open('sadgme.json', 'w') as c:
    json.dump(res, c, indent=4)

# ეს ისე. ვერ შემაქ Clinet errors აგდებს
x = res['cod']
print(x)

conn = sqlite3.connect('rame.sqlite')
cursor = conn.cursor()


# ესეც ისე
cursor.execute('''CREATE TABLE IF NOT EXISTS weather
                (city VARCHAR(40),
                date VARCHAR(40),
                windspeed INTEGER,
                temperature INTEGER)''')

cursor.executemany('INSERT INTO weather(city, date, windspeed, temperature) VALUES (?, ?, ?, ?)', (city, 'date', 'speed', 'temp'))