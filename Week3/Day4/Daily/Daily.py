# Instructions
# Using this REST Countries API, create the functionality which will write 10 random countries to your json file.
#
# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import json
import requests
import random

response = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()

r_countries = random.sample(countries, 10)

countries_j = []
# print(r_countries[0]['name'])
# print(r_countries[0]['capital'])
# print(r_countries[0]['flag'])
# print(r_countries[0]['subregion'])
# print(r_countries[0]['population'])

for country in r_countries:
    country_info = {
        "name": country.get("name", {}).get("common", "N/A"),
        "capital": country.get("capital", ["N/A"])[0],
        "flag": country.get("flags", {}).get("png", "N/A"),
        "subregion": country.get("subregion", "N/A"),
        "population": country.get("population", "N/A")
    }
    countries_j.append(country_info)
for country in countries_j:
    print(country)
with open("random_countries.json", "w") as json_file:
    json.dump(countries_j, json_file, indent=4)

print("10 random countries data were written to 'random_countries.json'")
