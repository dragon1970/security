

import requests

ip = "45.77.182.72"
url = "http://ipinfo.io/"+ip
r = requests.get(url)
print("国家:", r.json()["country"])
print("城市:", r.json()["city"])





