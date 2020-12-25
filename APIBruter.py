#!/usr/bin/env python3

#NAME: APIBRUTER
#Author: Joseph Martinez

import requests 

for api_key in range(1,100,2):
    print(f"api_key {api_key}")
    html = requests.get(f'http://10.10.84.152:8000/api/{api_key}')
    print(html.text) 
