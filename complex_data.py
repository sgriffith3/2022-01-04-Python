sally = {"make": "ford", "model": "mustang", "year": 2007}
print(sally)
print(sally['make'])
print(sally['model'])
print(sally['year'])

sally['year'] = 1977

print(sally['year'])
sally['color'] = "red"
print(sally)

jose = {"make": "chevy", "model": "el camino", "year": 2001}
print(jose)
print(jose['make'])
print(jose['model'])
print(jose['year'])

paint = {"color": "neon purple"}
jose.update(paint)
print(jose)

jose.update({"color": "metallic gold"})
print(jose)


# cars = [jose, sally]
# index  0      1

# print(cars)
# print(cars[0])
# print(cars[0]['model'])

