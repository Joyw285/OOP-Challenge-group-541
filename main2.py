from nel import Pet
# Creating a pet instance
pet_name = "Bingo"
my_pet = Pet(pet_name)
print(f"creating pet: {my_pet.name}")
my_pet.rest()
my_pet.play()
my_pet.sleep()
my_pet.show_status()

# Teaching the pet some new tricks
my_pet.learn_trick("backflip")
my_pet.learn_trick("sit")
my_pet.learn_trick("roll over")
my_pet.show_status()

# Trying to teach an existing trick
my_pet.learn_trick("jumping")