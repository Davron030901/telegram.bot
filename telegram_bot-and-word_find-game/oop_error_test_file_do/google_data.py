import json
import googlemaps
from apikey import APIKEY

gmaps=googlemaps.Client(key=APIKEY)

data=gmaps.geocode('Olmozor,Toshkent,Uzbekistan')

g=json.dumps(data[0],indent=4,sort_keys=True)
print(g)

data=data[0]

kenglik=data['geometry']['location']['lat']
uzunlik=data['geometry']['location']['lat']
print(f'{kenglik},{uzunlik}')