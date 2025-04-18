# main.py

from pet import Pet

# Create a pet named Coco
coco = Pet()

# Test the pet's methods
coco.get_status()
coco.eat()
coco.play()
coco.sleep()
coco.train("sit")
coco.train("roll over")
coco.train("sit")  # testing duplicate trick
coco.show_tricks()
coco.get_status()

