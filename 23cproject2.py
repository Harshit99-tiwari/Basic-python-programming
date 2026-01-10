#creating a mad libs game
print(" Welcome to the Mad Libs Game ")
print("Fill in the words below:\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
animal = input("Enter an animal: ")

print("\n Your Mad Libs Story:\n")

story = f"""
One day {name} went to {place}.
It was a very {adjective} day.
Suddenly, a {noun} appeared and started to {verb}.
Everyone was shocked when a {animal} joined the fun!
"""

print(story)
