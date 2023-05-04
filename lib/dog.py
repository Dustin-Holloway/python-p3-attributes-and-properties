#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, breed="Pug", name="Dog"):
        self.name = name
        self.breed = breed


    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25 and not None:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Dog"

    def get_name(self):
            return (self._name)

    def set_breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    def get_breed(self):
            return (self._breed)
    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)









    # @property
    # def name(self):
    #     return self._name
    
    

    # @name.setter
    # def name(self, value):
    #     if isinstance(value, str) and 1 <= len(value) <= 25:
    #         self._name = value
    #     else:
    #         print("Name must be string between 1 and 25 characters.")
    #         self._name = "Dog"

    # @property
    # def breed(self):
    #     return self._breed


    # @breed.setter
    # def breed(self, value):
    #     if value in APPROVED_BREEDS:
    #         self._breed = value
    #     else:
    #         print("Breed must be in list of approved breeds.")
    #         self._breed = "Mutt"

    
