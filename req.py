import requests

params = {"who": "Thony", "ik": "Jony"}

r = requests.get("http://192.168.100.90:9000/hi", params=params)
print(r.json())

params = {"who": "Jony", "ik": "Thony ;)"}

r = requests.post("http://192.168.100.90:9000/hi", json=params)
print(r.json())

# Hello? Thony? it's Jony
# Hello? Jony? it's Thony ;)