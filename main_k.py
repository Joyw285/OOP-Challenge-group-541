from pet import Pet

def main():
    print("Welcome to Virtual Pet!")
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"\nMeet your new pet, {pet_name}!")
    my_pet.get_status()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Put your pet to sleep")
        print("3. Play with your pet")
        print("4. Train your pet")
        print("5. Check tricks")
        print("6. Check status")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            trick = input("What trick would you like to teach? ").strip()
            my_pet.train(trick)
        elif choice == "5":
            my_pet.show_tricks()
        elif choice == "6":
            my_pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {pet_name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.")
            continue  # Skip the status update for invalid choices
        
        # Show status after each valid action
        my_pet.get_status()

if __name__ == "__main__":
    main()