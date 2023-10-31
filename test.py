import json

with open('info.json', 'r') as f:
    data = json.load(f)

print(data['PREFIXES']['123'])
data['PREFIXES']['123'] = '$'
print(data['PREFIXES']['123'])

with open('info.json', 'w') as f:
    json.dump(data,f)
