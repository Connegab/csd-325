import requests

response = requests.get("https://anapioficeandfire.com/api/") 
print(response.json())

import json

# create a formatted string of the Python JSON object
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())
