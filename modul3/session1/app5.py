objects = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
for obj in objects:
    print("Tipul obiectului", obj, "este", str(type(obj)).split("'")[1])
