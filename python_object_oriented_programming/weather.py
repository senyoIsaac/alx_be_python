# -*- coding: utf-8 -*-

import requests
import json

apiKey = "f8d0a854e21170737d1620c19a61c0f5"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

completeURL = baseURL + "Kumasi" + "&appid=" + apiKey
response = requests.get(completeURL)
 
data = response.json()

print(data)