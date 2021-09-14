#!/usr/bin/env python3

#NAME: APIScraper
#Author: Joseph M

from bs4 import BeautifulSoup
import requests 

html = requests.get('http://[machine_ip]:8000/') 
soup = BeautifulSoup(html.text, "lxml")

links = soup.find_all('a')
for link in links:
    if "href" in link.attrs:          
        print(link["href"])
