"""
Se crean 3 funciones para responder las preguntas planteadas 
en el reto, aqui se ejecutan por medio de la libreria unittest
para realizar una validación unitaria 

Jhonatan Fernandez

"""

from urllib.parse import urlparse
import requests


class PokemonAPI:

    API_URL = "https://pokeapi.co/api/v2"


    def count_pokemon_by_characters(self) -> int:

        pokemon_count = requests.get(
            url=self.API_URL+"/pokemon-species").json()['count']

        pokemon_species_data = requests.get(
            url=f"{self.API_URL}/pokemon/?limit={pokemon_count}").json()

        pokemon_names = [pokemon['name']
                         for pokemon in pokemon_species_data['results'] if ("at" in pokemon['name']) and (pokemon['name'].count('a') == 2)]
        pokemon_number = len(pokemon_names)        
        print(
            f"1- Número de pokemones que poseen en sus nombres \"at\" y dos \"a\" en sus nombres: {pokemon_number}")
        return pokemon_number


    def species_compatibility(self, pokemon_name: str) -> int:
        matches = set()
        pokemon_egg_group_data = requests.get(url=f"{self.API_URL}/pokemon-species/{pokemon_name}")\
            .json()['egg_groups']            
        egg_groups_urls = [egg_group['url']
                           for egg_group in pokemon_egg_group_data]
        for url in egg_groups_urls:
            egg_group_data = requests.get(url=url).json()
            matches = matches.union(set(poke['name']
                                        for poke in egg_group_data['pokemon_species']))
        pokemon_number = len(matches)             
        print(
            f"2- Número de especies compatibles para reproducción con el pokémon raichu es: {pokemon_number}")
        return pokemon_number

    def min_max_weight_by_type(self, type_name: str) -> list():

        weights_list = list()

        pokemon_type_info = requests.get(
            url=f"{self.API_URL}/type/{type_name}").json()
        pokemon_info = [pokemon['pokemon']
                        for pokemon in pokemon_type_info['pokemon']]
        for pokemon in pokemon_info:
            parsed_pokemon_url = urlparse(pokemon['url'])
            if int(parsed_pokemon_url.path.rsplit("/", 2)[1]) <= 151:
                pokemon_data = requests.get(url=pokemon['url']).json()
                weights_list.append(pokemon_data['weight'])
        max_min = [max(weights_list), min(weights_list)]
        print(
            f"3- El Máximo y mínimo de peso de los pokemones tipo fighting es: {max_min}")
        return max_min
