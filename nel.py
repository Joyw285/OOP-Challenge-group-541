import random

class Pet:
    def _init_(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
        self.tricks = ['jumping']

    def play(self):
        print(f"{self.name} is playing..")
        self.hunger = min(10, self.hunger + 2)
        self.energy = max(0, self.energy - 3)
        self.happiness = min(10, self.happiness + 3)

    def rest(self):
        print(f"{self.name} is resting ..")
        self.energy = min(10, self.energy + 3)
        self.hunger = min(10, self.hunger + 1)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping..")
        self.energy = 10
        self.hunger = min(10, self.hunger + 1)
        self.happiness = max(0, self.happiness - 1)

    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)
            print(f"{self.name} learned a new trick: {new_trick}!")
        else:
            print(f"{self.name} already knows {new_trick}.")

    def show_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger:{self.hunger}")
        print(f"Energy:{self.energy}")
        print(f"Happiness:{self.happiness}")
        print(f"Tricks: {self.tricks}")
        print()


    



