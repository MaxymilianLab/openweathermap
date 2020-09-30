#!/usr/bin/env python3

import os
import requests
import sys
from argparse import ArgumentParser


parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('city', help='City to get the weather for')


args = parser.parse_args()

api_key = os.getenv('OWM_API_KEY')


if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

url = f"http://api.openweathermap.org/data/2.5/weather?q={args.city}&appid={api_key}"
# print(url)
res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

print(res.json())




