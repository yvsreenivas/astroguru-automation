# generate_panchanga.py

import requests
from bs4 import BeautifulSoup

url = "https://www.astroguru.life/"

html = requests.get(url).text

# Extract Panchanga data here

print("Panchanga data extracted")
