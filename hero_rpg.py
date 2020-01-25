#!/usr/bin/env python

# Step 2
# Take the code for the hero attacking the goblin and extract it into a 
# method (call it attack) of the Hero class. Replace the existing code with 
# a call to the attack method. Hint: attack should take in the goblin (enemy) 
# as a parameter: hero.attack(goblin)

class Hero:
    def __init__(self, health, power):
        self.health = health 
        self.power = power
        
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        
        
class Goblin:
    def __init__(self, health, power):
        self.health = health 
        self.power = power

def main():
    
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    
    while goblin.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

main()