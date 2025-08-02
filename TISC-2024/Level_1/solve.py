import h3
ids = ["8c1e806a3ca19ff", "8c1e806a3c125ff", "8c1e806a3ca1bff"]

coordinates = [h3.h3_to_geo(h3_id) for h3_id in ids]
print(coordinates)

lat = sum(c[0] for c in coordinates) / 3
long = sum(c[1] for c in coordinates) / 3
print(f"{lat}, {long}")