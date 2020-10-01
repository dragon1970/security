

import requests

ip = "1.2.3.4"
url = "http://ipinfo.io/"+ip
r = requests.get(url)
print("country:", r.json()["country"])
print("city:", r.json()["city"])





