
from datetime import datetime
import geojson
import json

geoJson = {}

with open('data.json') as json_data:
    geoJson = json.load(json_data)

features = geoJson['features']

for point in features:
    point['geometry']['coordinates'][0] = float(point['geometry']['coordinates'][0])
    point['geometry']['coordinates'][1] = float(point['geometry']['coordinates'][1])
    

point = features[0]



sortedGeo = sorted(features, key = lambda x: x['properties']['timestamp'])


print(datetime.fromtimestamp(sortedGeo[0]['properties']['timestamp']))
print(datetime.fromtimestamp(sortedGeo[-1]['properties']['timestamp']))
