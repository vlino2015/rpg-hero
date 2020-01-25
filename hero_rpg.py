#!/usr/bin/env python

# Step 5
# Take the code for printing the health status of the hero and move 
# it into a method called print_status of Hero. Do the same for the goblin.


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
        
    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")

        
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
        
    def print_status(self):
        print(f"The goblin has {self.health} health and {self.power} power.")

def main():
    
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    
    while goblin.alive() > 0 and hero.alive():
        
        hero.print_status()
        goblin.print_status()
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
            if not goblin.alive():
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            
            print("The goblin does {} damage to you.".format(goblin.power))
            
            if not hero.alive():
                print("You are dead.")

main()