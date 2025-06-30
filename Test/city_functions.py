# city_functions.py

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# Function calls
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
print(city_country("brussels", "belgium"))
