ponds = [
    {"pk": 1, "volume": 10000, "fish": "тунец"},
    {"pk": 192, "volume": 20000, "fish": "морская камбала"},
    {"pk": 206, "volume": 10000, "fish": "треска"},
    {"pk": 322, "volume": 25000, "fish": "тунец"},
    {"pk": 420, "volume": 20000, "fish": "морская камбала"},
    {"pk": 704, "volume": 10000, "fish": "треска"},
    {"pk": 920, "volume": 25000, "fish": "тунец"},
]

for pond in ponds:
    if pond['fish'] == "тунец":
        ponds.remove(pond)

print(ponds)

ponds_converted = {}
ponds_to_delete = []
for i in range(len(ponds)):
    ponds_converted[i] = {"pk": ponds[i]['pk'], "volume": ponds[i]['volume'], "fish": ponds[i]['fish']}
    if ponds[i]['fish'] == 'тунец':
        ponds_to_delete.append(i)

for i in ponds_to_delete:
    del ponds_converted[i]

ponds.clear()

for i in ponds_converted:
    ponds.append(ponds_converted.get(i))
