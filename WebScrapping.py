# IMPORT REQUIRED LIBRARIES

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# WEBSITE URL

URL = "https://www.scrapethissite.com/pages/simple/"

# LOAD WEB PAGE

page = requests.get(URL)

# CHECK STATUS CODE

print("Status Code :", page.status_code)

# CREATE BEAUTIFULSOUP OBJECT

soup = BeautifulSoup(page.text, "html.parser")

# EXTRACT ALL COUNTRIES

countries = soup.find_all("div", class_="country")

# EMPTY LISTS

country_names = []
capitals = []
populations = []

# LOOP THROUGH EACH COUNTRY

for country in countries:

    name = country.find("h3", class_="country-name").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()
    population = country.find("span", class_="country-population").text.strip()

    country_names.append(name)
    capitals.append(capital)
    populations.append(int(population))

# CREATE DATAFRAME

df = pd.DataFrame({
    "Country": country_names,
    "Capital": capitals,
    "Population": populations
})

# DISPLAY DATAFRAME

print("\nDataFrame:\n")
print(df.head())

# SAVE TO CSV

df.to_csv("countries_data.csv", index=False)

print("\nCSV File Saved Successfully!")

# VISUALIZATION

plt.figure(figsize=(10,5))
plt.bar(country_names[:10], populations[:10])
plt.xticks(rotation=90)
plt.xlabel("Country")
plt.ylabel("Population")
plt.title("Population of First 10 Countries")
plt.tight_layout()
plt.show()
