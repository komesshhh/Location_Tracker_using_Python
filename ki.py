import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)     #Country Name is printed here.

from phonenumbers import carrier
service_pro= phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en")) #Service provider is printed here.

from opencage.geocoder import OpenCageGeocode
key='9399a4b0d64049f598cfce8887b8244e'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)
lat =results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)


mymap=folium.Map(location=[lat,lng],zoom_start=9)


folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("mylocation.html")

