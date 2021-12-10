import random

print()

print("Enter names into the raffle, or press enter to randomly choose a winner.\n")

names = []

while True:
  name = input("Enter a name: ")

  if name != "":
    names.append(name)
  elif len(names) == 0:
    print("\nEnter a name before choosing a winner.\n")
  else:
    print(f"\nThe winner is {random.choice(names)}.\n")
