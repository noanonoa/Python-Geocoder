import geocoder

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