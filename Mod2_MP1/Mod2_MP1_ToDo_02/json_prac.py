import json

with open('Mod2_MP1\Mod2_MP1_ToDo_02\weather.json','r') as read_file:
    data = json.load(read_file)

print(data)