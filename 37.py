
#This program fetches live data about a Pokémon from an online API and prints out some of its details. Let's go through it.

#requests is a library used to make HTTP calls — in this case, to talk to a website/API over the internet and get data back
import requests

# (base_url = "https://pokeapi.co/api/v2/") This stores the starting portion of the API's web address, so you don't have to retype the whole thing every time you build a new URL.
base_url = "https://pokeapi.co/api/v2/"

#The function that fetches data
#url = f"{base_url}/pokemon/{name}" builds the full web address by combining base_url with /pokemon/ and whatever Pokémon name was passed in. So for "Typhlosion", this becomes https://pokeapi.co/api/v2//pokemon/Typhlosion (note: there's a small double-slash // here since base_url already ends in / — harmless, most web servers ignore the extra slash, but worth knowing).
#requests.get(url) actually sends a request out to that address and waits for a response, storing the result in response.
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

#response.status_code is a number the server sends back indicating whether the request succeeded. 200 specifically means "OK — success."
    #If successful, response.json() converts the raw response data into a Python dictionary, and that dictionary gets returned from the function (handed back to whatever called it)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "Typhlosion"
#Calls the function with "Typhlosion", and stores whatever it returns (either a dictionary of data, or None if it failed) into pokemon_info.
pokemon_info = get_pokemon_info(pokemon_name)

#if pokemon_info: checks whether pokemon_info is "truthy." A dictionary with content in it is truthy; None is falsy. So this block only runs if the fetch actually succeeded — this protects the code from crashing if the API call failed and pokemon_info ended up being None
#Each print() line pulls one specific piece of data out of the dictionary by its key — "name", "id", "height", "weight" — and displays it, using an f-string to embed each value directly into the printed sentence.
if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

