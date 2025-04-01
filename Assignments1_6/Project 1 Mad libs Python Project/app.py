# Sci-Fi Adventure Mad Libs Game

# Welcome message for the user
print("\n🌍 Welcome to the Ultimate Sci-Fi Adventure Mad Libs Game! 🚀\n")

# Taking user inputs for the Mad Libs game
name = input("Enter your name: ")  # User se unka naam liya jaata hai
planet = input("Name a mysterious planet: ")  # User se ek mysterious planet ka naam liya jaata hai
spaceship = input("Your spaceship's name: ")  # User se spaceship ka naam liya jaata hai
robot = input("A robot's name: ")  # User se ek robot ka naam liya jaata hai
weapon = input("A futuristic weapon: ")  # User se futuristic weapon ka naam liya jaata hai
alien_species = input("A strange alien species: ")  # User se alien species ka naam liya jaata hai
super_ability = input("A super ability you wish to have: ")  # User se ek super ability li jaati hai
technology = input("An advanced technology: ")  # User se ek advanced technology ka naam liya jaata hai
color = input("Your favorite color: ")  # User se unka favorite color liya jaata hai
space_food = input("A space food you'd love to try: ")  # User se ek space food ka naam liya jaata hai

# Story template with the user's input inserted into the story
story = f"""
🛸 Captain {name} set out on a daring space mission to the mysterious planet {planet} aboard the {spaceship}.
With {robot} by their side, they navigated through asteroid fields and cosmic storms.

Upon landing on {planet}, they encountered the {alien_species}, a highly intelligent species with glowing {color} eyes.
The aliens challenged {name} to prove their worth by mastering the {technology} and showcasing their ability of {super_ability}.

As the final challenge, {name} wielded the legendary {weapon} and bravely faced the cosmic trials.
After a victorious adventure, the {alien_species} rewarded {name} with a feast of {space_food}, marking the beginning of a new intergalactic friendship! 🌌✨
"""

# Printing the story to the user
print(story)  # Yeh line story ko print karti hai jo ab user ke inputs se customize ho chuki hoti hai.
