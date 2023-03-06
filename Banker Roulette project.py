# 14. Banker Roulette project:

print("Welcome to Banker Roulette!")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
from random import randrange
random_name = randrange(len(names))
print(f"{names[random_name]} is going to buy a meal today!")
