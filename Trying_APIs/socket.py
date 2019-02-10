import requests
import json

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

response_pass = requests.get("http://api.open-notify.org/iss-pass.json")

# Print the status code of the response.
#print(response.status_code)
print(response_pass.status_code)

#lat = float(input("Please, enter Latitude: "))
#lon = float(input("Please, enter Longitude: "))
lat = 40.71
lon = -74

# This is the latitude and longitude of New York City.
#parameters = {"lat": 40.71, "lon": -74}

parameters = {"lat": lat, "lon": lon,}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#print the returned values
#print(response.content)

# This gets the same data as the command above
#response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
#print(response.content)

#Converting the API response to a python dictionary

data = response.json()

head = response.headers
headdict = head.json()

for x,y in headdict.items():
    print("Key:{} Value:{}\n".format(x,y))

#print(type(data))
#print(data)
for x,y in data.items():
    print("Key:{} Value:{}\n".format(x,y))
