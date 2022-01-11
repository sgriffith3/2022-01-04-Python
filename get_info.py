import requests

url = "https://google.com"

r = requests.get(url)

print(r)
# print(r.text)
# print(r.content)

example_data = {"people": [{"craft": "ISS", "name": "Mark Vande Hei"},
                           {"craft": "ISS", "name": "Pyotr Dubrov"},
                           {"craft": "ISS", "name": "Anton Shkaplerov"},
                           {"craft": "Shenzhou 13", "name": "Zhai Zhigang"},
                           {"craft": "Shenzhou 13", "name": "Wang Yaping"},
                           {"craft": "Shenzhou 13", "name": "Ye Guangfu"},
                           {"craft": "ISS", "name": "Raja Chari"},
                           {"craft": "ISS", "name": "Tom Marshburn"},
                           {"craft": "ISS", "name": "Kayla Barron"},
                           {"craft": "ISS", "name": "Matthias Maurer"}], "message": True, "number": 10}

