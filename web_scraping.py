# Web Scraping com Python usando requests e bs4 BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = 'https://astronaut-landing-page.netlify.app' 
response = requests.get(url)

raw_html = response.text 
parsed_html = BeautifulSoup(raw_html, 'html.parser') 

# print(parsed_html.title) 

selector_copiado = parsed_html.select_one('#top3 > div > div > article:nth-child(3) > h3') 

if selector_copiado is not None:
    tudo_da_tag_article = selector_copiado.parent 
    print(tudo_da_tag_article)

for p in tudo_da_tag_article.select('p'): 
    print(p) 
    print(p.text) 
