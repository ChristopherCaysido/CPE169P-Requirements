import json

# f = open('weather.json',)
f = open('manila_weather_2021-04-16.json',)
data = json.load(f)

# #part 1: display main
# for k in data['main']:
#     print(k, ':', data['main'][k])

# part 2: display the coordinates
# print(f"{data['name']} {data['sys']['country']}")
# values = map(lambda key: key[0] + str(key[1]), data['coord'].items())
# values = filter(lambda key: key[0] + str(key[1]), data['coord'].items())

# for i,j in values:
#     print(i,':', j)

# # part 3: display weather
# for i,j in data['weather'][0].items():
#     print(i,':', j)


f.close()

