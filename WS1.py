# IMPORT REQUIRED LIBRARIES

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: WEB SCRAPING

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# EXTRACT QUOTES

quotes = soup.find_all("div", class_="quote")

authors = []
quote_lengths = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    authors.append(author)
    quote_lengths.append(len(text))

# STEP 2: CREATE DATAFRAME

df = pd.DataFrame({
    "Author": authors,
    "Quote_Length": quote_lengths
})

print("\nExtracted Data:\n")
print(df)

# SAVE TO CSV

df.to_csv("quotes_data.csv", index=False)
print("\nCSV File Saved Successfully!")

# STEP 3: DATA VISUALIZATION

plt.figure(figsize=(10,5))
plt.bar(authors, quote_lengths)
plt.xticks(rotation=90)
plt.xlabel("Authors")
plt.ylabel("Quote Length")
plt.title("Quote Length by Author")
plt.tight_layout()
plt.show()
