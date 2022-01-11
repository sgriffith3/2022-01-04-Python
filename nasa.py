import requests

r = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

print(r.json())
print(r.headers)