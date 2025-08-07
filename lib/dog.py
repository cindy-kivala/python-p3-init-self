#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

nana = Dog("Nana")
nana.breed = "Golden Retriever"
nana.name = "Nana the Golden Retriever"
