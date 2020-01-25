#!/usr/bin/env python

# Step 4
# Refactor the while condition:

# while goblin.health > 0 and hero.health > 0:

# to

# while goblin.alive() and hero.alive():

# The health checks should be moved to within the alive methods of
#  Hero and Goblin respectively.


class Hero:
    def __init__(self, health, power):
        self.health = health 
        self.power = power
        
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        
    def alive(self):
        
        if self.health > 0:
            return True
        else:
            return False
        
        
        
class Goblin:
    def __init__(self, health, power):
        self.health = health 
        self.power = power
        
    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        
    def alive(self):
        if self.health > 0 :
            return True 
        else: 
            return False

def main():
    
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    
    while goblin.alive() > 0 and hero.alive():
        
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
            goblin.attack(hero)
            
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

main()