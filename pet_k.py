class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats. Hunger decreases, happiness increases!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} sleeps. Energy increases!")
    
    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} plays. Energy decreases, happiness increases, hunger increases!")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)} ({self.happiness}/10)")
        
        # Status messages
        if self.hunger >= 8:
            print(f"Warning: {self.name} is very hungry!")
        if self.energy <= 2:
            print(f"Warning: {self.name} is very tired!")
        if self.happiness <= 2:
            print(f"Warning: {self.name} is very unhappy!")
    
    # Bonus methods
    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)
        print(f"{self.name} learned a new trick: {trick}!")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")