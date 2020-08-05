import geocoder
import requests

API_BASE_URL = "https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/"


destinations = [
  "Space Needle",
  "Crater Lake",
  "Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspesion Bridge"
]

g = geocoder.arcgis('Redlands, CA')

print(g.latlng[0], g.latlng[1])
print('🔥')

for i in destinations:
  geo = geocoder.arcgis(i)
  print("{} is located at ({:.4f}, {:.4f})".format(i, geo.latlng[0], geo.latlng[1]))

  full_api_url = API_BASE_URL + str(geo.latlng[0]) + "," + str(geo.latlng[1])
  result = requests.request('GET', full_api_url).json()

  print("⛅️At the {} right now, it's {} with a temperature of {}".format(i, result["currently"]["summary"], result["currently"]["temperature"]))