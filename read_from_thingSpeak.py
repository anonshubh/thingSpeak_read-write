"""
Created by - 
Shubh Pathak - MSM19B018

ThingSpeak Fields:
1) Field 1: temperature
2) Field 2: humidity
3) Field 3: light
4) Field 4: pressue

Read API Endpoint: https://api.thingspeak.com/channels/1312520/feeds.json?api_key=QE8UJGAHWPYX3QXW&results=5
"""
import requests,sqlite3

response = requests.get(
    "https://api.thingspeak.com/channels/1312520/feeds.json?api_key=QE8UJGAHWPYX3QXW&results=5"
)

if(response.ok):
    response_in_json = response.json()
else:
    exit(1) # Exiting on Invalid Response

data = response_in_json.get("feeds")

connection = connection = sqlite3.connect("response.db")
cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE Response (Id INTEGER,Temperature INTEGER, Humidity INTEGER, Light INTEGER, Pressue INTEGER)"
) # Creating Table with name Response

for i in data:
    id_ = i['entry_id']
    temperature = int(i['field1'])
    humidity = int(i['field2'])
    light = int(i['field3'])
    pressure = int(i['field4'])

    cursor.execute(f"INSERT INTO Response VALUES ({id_}, {temperature}, {humidity}, {light}, {pressure})")


connection.commit() # Writing Changes into db

print("Sucessfully Written Response from thingSpeak in db!!")
