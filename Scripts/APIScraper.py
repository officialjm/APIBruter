#!/usr/bin/env python3

#   ___  ______ _____ _____ _____ ______  ___  ______ ___________ 
#  / _ \ | ___ \_   _/  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \
# / /_\ \| |_/ / | | \ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /
# |  _  ||  __/  | |  `--. \ |    |    /|  _  ||  __/|  __||    / 
# | | | || |    _| |_/\__/ / \__/\| |\ \| | | || |   | |___| |\ \ 
# \_| |_/\_|    \___/\____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|
#                                                                                                                              
# Author: github.com/officialjm
# This is a simple web domain scraper used to find a link to where API calls can be made within 
# the webserver.

from bs4 import BeautifulSoup
import requests 

html = requests.get('http://[machine_ip]:80/') # Insert machine ip here.
soup = BeautifulSoup(html.text, "lxml")

links = soup.find_all('a')
for link in links:
    if "href" in link.attrs:          
        print(link["href"])
