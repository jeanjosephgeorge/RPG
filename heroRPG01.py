#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self,health,power,name):
        self.health = health
        self.power = power
        self.name = name

Hero = Character(10,5,"Hero")
Goblin = Character(6,2,"Goblin")


# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

while Goblin.health > 0 and Hero.health > 0:
    print(f"You have {Hero.health} health and {Hero.power} power.")
    print(f"The goblin has {Goblin.health} health and {Goblin.power} power.")
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        # Hero attacks goblin
        Goblin.health -= Hero.power
        print(f"You do {Hero.power} damage to the goblin.")
        if Goblin.health <= 0:
            print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print(f"Invalid input {raw_input}")

    if Goblin.health > 0:
        # Goblin attacks hero
        Hero.health -= Goblin.power
        print(f"The goblin does {Goblin.power} damage to you.")
        if Hero.health <= 0:
            print("You are dead.")

#main()