class Inventory:
    def __init__(self):
        self.credits = 0
        self.shards = 0
        self.pokemon_inventory = {}

    def add_credits(self, amount):
        self.credits += amount

    def add_shards(self, amount):
        self.shards += amount

    def add_pokemon(self, pokemon):
        if pokemon.name in self.pokemon_inventory:
            self.pokemon_inventory[pokemon.name] += 1
        else:
            self.pokemon_inventory[pokemon.name] = 1

    def remove_pokemon(self, pokemon):
        if pokemon.name in self.pokemon_inventory:
            if self.pokemon_inventory[pokemon.name] > 1:
                self.pokemon_inventory[pokemon.name] -= 1
            else:
                del self.pokemon_inventory[pokemon.name]