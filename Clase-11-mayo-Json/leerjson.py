import json

with open ('ejemploCaminoV2.json') as archivo:
    datos=json.load(archivo)

print datos["height"]
print datos["width"]
print datos ["layers"][1]["data"]
print datos ["layers"][0]["data"]
