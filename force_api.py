#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

# URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader = resp.json()
        pprint(vader)
        # {Darth Vader} was born in the year {41.9BBY}. His eyes are now {yellow} and his hair color is {none}.
        print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are now {vader['eye_color']} and his hair color is {vader['hair_color']}")
    else:
        print("That is not a valid URL.")

    movie = requests.get("https://swapi.dev/api/films/1/").json()
    movie_name = movie['title']
    print(movie_name)

    ship = requests.get("https://swapi.dev/api/starships/13").json()
    ship_name = ship["name"]
    print(ship_name)

    # He first appeared in the movie {A New Hope} and could be found flying around in his {TIE Advanced x1}.
    print(f"He first appeared in the movie {movie_name} and could be found flying around in his {ship_name}.")


if __name__ == "__main__":
    main()
