import json

items = json.loads('[{"name": "item1", "price": 10}, {"name": "item2", "price": 15}]')

for item in items:
    print(item['name'])
