import unittest
from pokeFunctions import PokemonAPI

class FindElements(unittest.TestCase):
    POKEMON_NAME = "raichu"
    POKEMON_TYPE = "fighting"

    def __init__(self, methodName: str = ...) -> None:
        self.poke_api = PokemonAPI()
        super().__init__(methodName)

    def test_count_pokemon_by_characters(self):
        number_pokemon = self.poke_api.count_pokemon_by_characters()
        self.assertEqual(type(number_pokemon), int)
        self.assertEqual(number_pokemon, 9)

    def test_species_compatibility(self):
        number_matches = self.poke_api.species_compatibility(self.POKEMON_NAME)
        self.assertEqual(type(number_matches), int)

    def test_min_max_weight_by_type(self):
        min_max_weight = self.poke_api.min_max_weight_by_type(
            self.POKEMON_TYPE)
        self.assertEqual(type(min_max_weight), list)
        [max, min] = min_max_weight
        self.assertGreater(max, min)


if __name__ == '__main__':
    unittest.main()
