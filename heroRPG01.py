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

    def attack (self,other):
        other.health -= self.power
        print (f"{self.name} does {self.power} damage to the {other.name}.")
        return other.health


Hero = Character(10,5,"Hero")
Goblin = Character(8,2,"Goblin")



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
        Hero.attack(Goblin)
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
        Goblin.attack(Hero)
        if Hero.health <= 0:
            print("You are dead.")

#main()