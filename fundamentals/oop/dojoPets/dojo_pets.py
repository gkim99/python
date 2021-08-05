class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


class Pet:
    def __init__(name, type, tricks):
        name = name
        type = type
        tricks = tricks
        health = 0
        energy = 0

    def sleep(energy):
        energy += 25

    def eat(energy, health):
        energy += 5
        health += 10

    def play(health):
        health += 5

    def noise(noise):
        print(noise)
