cities = {}
while True:
    city = input().split(" ")
    if "Waterloo" in city:
        break
    else:
        cities[city[0]] = int(city[1])
sortedcity = sorted(cities.items(), key=lambda x: x[1])
print(sortedcity[0][0])