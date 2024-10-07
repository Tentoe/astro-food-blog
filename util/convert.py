
from datetime import datetime, date
import geojson
from geojson import LineString
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

days = [
    date(2024, 9, 8),
    date(2024, 9, 9),
    date(2024, 9, 10),
    date(2024, 9, 11),
    date(2024, 9, 12),
    date(2024, 9, 13),
    date(2024, 9, 14),
    date(2024, 9, 15),
]

split = map(lambda y: filter(lambda x: datetime.fromtimestamp(x['properties']['timestamp']).date() == y, sortedGeo), days)


# print(datetime.fromtimestamp(sortedGeo[0]['properties']['timestamp']))
# print(datetime.fromtimestamp(sortedGeo[-1]['properties']['timestamp']))

lines = [LineString([(point['geometry']['coordinates'][0], point['geometry']['coordinates'][1]) for point in day]) for day in split]

# for day in split:
    
    # line = [(point['geometry']['coordinates'][0], point['geometry']['coordinates'][1]) for point in day] 
  
# out = LineString(line)  



with open('out.json', 'w') as json_data:
    geojson.dump(lines[0] ,json_data)

