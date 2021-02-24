"""
Created by - 
Shubh Pathak - MSM19B018

ThingSpeak Fields:
1) Field 1: temperature
2) Field 2: humidity
3) Field 3: light
4) Field 4: pressure

Write API Endpoint: https://api.thingspeak.com/update?api_key=2UU5ZBPMF0Y3PE1C&field1=0
"""

import requests,random,time

try:
    while True:
        temperature = random.randint(1,50)
        humidity = random.randint(10,30)
        light = random.randint(1,10)
        pressure = random.randint(1,100)

        response = requests.get(
            "https://api.thingspeak.com/update?api_key=2UU5ZBPMF0Y3PE1C",
            params={'field1':temperature,'field2':humidity,'field3':light,'field4':pressure}
        )

        print(f"Status {response.status_code}")
        time.sleep(1)
except:
    print("\nExiting due to Error...")




