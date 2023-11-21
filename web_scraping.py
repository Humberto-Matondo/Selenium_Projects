# Web Scraping com Python usando requests e bs4 BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = 'https://astronaut-landing-page.netlify.app' 
response = requests.get(url)

raw_html = response.text 
parsed_html = BeautifulSoup(raw_html, 'html.parser') 

print(parsed_html.title) 