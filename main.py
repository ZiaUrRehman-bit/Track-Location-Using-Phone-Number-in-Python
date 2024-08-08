import phonenumbers
import opencage
import folium
from myNumber import number

from phonenumbers import geocoder

pepNumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepNumber, "en")

print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key='d8b0a13134074f2bbc87dad6f5777e44'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation4.html")