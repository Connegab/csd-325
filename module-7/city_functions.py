# Gabe Conner
# Assignment 7.2

# city_functions.py

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Function calls
print(city_country("santiago", "chile", 5000000, "spanish"))
print(city_country("tokyo", "japan"))
print(city_country("brussels", "belgium", 1200000))
