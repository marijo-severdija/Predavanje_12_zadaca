import json
import random

global select_city

def play():
    global select_city
    country_list = []

    with open("guess_city.json", "r") as file:
        city_list = json.loads(file.read())

    for item in city_list:
        country_list.append(item["country"])

    select_country = random.choice(country_list)
    for item in city_list:
        if item["country"] == select_country:
            select_city = item["city"]

    while True:
        city_guess = input(f"What is capital city of {select_country}?: ")
        if city_guess == select_city:
            print("Wow, you are correct!")
            break
        else:
            print("Hmmm, not correct, try again...")


play()
while True:
    select = input("Do you want to play again? (y/n): ")
    if select.lower() == "y":
        play()
    else:
        break
