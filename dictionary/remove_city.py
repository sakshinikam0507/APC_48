cities = {
    "Pune": 7000000,
    "Mumbai": 21000000,
    "Nashik": 1800000,
    "Nagpur": 2500000
}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
print(cities)
