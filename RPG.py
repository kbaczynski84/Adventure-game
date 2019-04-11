from random import random
from sys import exit

name = input("Hello what is your name?")



class Hero(object):
    def __init__(self, hit_points, strength, money):
            self.hit_poitns = hit_points
            self.strength = strength
            self.money = money


    name = Hero(0, 0, 0)
    food = 0
    axe = False
    pickaxe = False
    bow = False
    fishingrod = False

    def hp_test():
        if Hero.hitpoints <= 0:
            Death.enter()
        else:
            pass

    def hunger_test():
        if Hero.food <= 0:
            Death.enter()
        else:
            pass

    def equip():
        if Hero.axe == True:
            Hero.strength += 10
        elif Hero.pickaxe == True:
            Hero.strength += 5
        elif Hero.bow == True:
            Hero.strength += 2
        else:
            pass

# this method i think it will be easier to assign to creature to only fight hero
    def fight():
        hp1 == Hero.hit_points
        hp2 == Creature.hit_points
        damage1 = Hero.strength.equip
        damage2 = Creature.strength
        while hp1  > 0 or hp2 > 0:
            hp1 -= damage2,
            hp2 -= damage1
        else:
            Print(f"You lost {hp1}HP, your opponent lost {hp2}HP")

class Creature(object):
    def __init__(self, hit_points, strength, money):
            self.hit_poitns = hit_points
            self.strength = strength
            self.money = money


#class monster(creature)
    goblin = Creature(0, 0, 0)


#class Animall(Creature):
    deer = Creature(0, 0, 0)


#class Fish(Person):
    herring = Creture(0, 0, 0)



class NPC(object):
    def __init__(self, hit_points, strength, money):
            self.hit_points = hit_points
            self.strength = strength
            self.money = money

    Sigfrid = NPC(0, 0, 0)
    alive = True

    def shop_greating(self):
        print("""
        Greeting traveller. What do you wish to have?
        1.FishingRod          - 10 gp
        2.Bow                 - 20 gp
        2 Pickaxe             - 50 gp
        4.Axe                 - 100 gp
        5. or maybe some food?-  2 gp
        """)

    def buy(self):
        self.buy = input("<")

    if self.buy == "1" and Hero.money > 10:
        Hero.fishingrod = True,
        Hero.money -= 10
    elif self.buy == "2" and Hero.money > 20:
        Hero.bow = True,
        Hero.money -= 20
    elif self.buy == "3" and Hero.money > 50:
        Hero.pickaxe = True,
        Hero.money -= 50
    elif self.buy == "4" and Hero.money > 100:
        Hero.axe = True,
        Hero.money -= 100
    elif self.buy == "5" and Hero.money > 2:
        Hero.food += 5
        Hero.money -= 2
    elif  self.buy == "steal":
        pass
    elif buy == "attack" or "kill":
        pass
    elif buy == "run" or "leave":
        pass
    else:
        print("I dont understand")



class Location(object):
    pass
#here i will poss init method which when executed will take food from the hero

class Death(Location):

     motivation = [
        "You died. You kinda suck at this.",
        "Such a luser",
        "You're worse than your Dad's jokes."
        "Dont quit your day job"
        "I feel sorry for you... Not really"
        "Your lucky that's only a game.Though you probably also suck in life"
        ]

def enter(self):
    print(Death.motivation[randint(0, len(self.motivation)-1)])
    exit(1)

class Forest(Location):

    def enter(self):
        print("""
        You enter a forest. You know that it is quite peacefull.
        But lately when you traveled to the forest you seem to notice an
        increased number of goblins in here. Forest is good hunting grounds
        but could also have an encounter with some type of monster if you
        wont be carefull.
        """)

class Dungeon(Location):

    def enter(self):
        print("""
        As you traveled throgh well known forest. You noticed something which
        you didnt see before. There is a cave entrence in a place where was
        a solid rock before. Do you decide to come in?(Y/N)
        """)

class Lake(Location):

    def enter(self):
        print("You went for a stroll besiede the lakeshore.")

class Shop(Location):

    def enter(self):
        if Sigfrid.alive == True:
            shop_greating()
        else:
            print("""
            The shop is demolished. You dont want to spend here to
            much time. You throw a glimpse on dead shopkeeper corpse and regret
            actions which lead to slaying this poor fellow.
            """)
            enter(Start)


class Start(Location):



    def enter(self):
        print("""
        You stand before your little house. What do you want to do?
        1. Go to the shop?
        2. Go to the lake?
        3. Go to the forest?
        Or You just need help?
        """)

    direction = input("<")
        if direction == "1":
            pass
        elif direction == "2":
            pass
        elif direction == "3":
            pass
        else:
            print("""
You probaly are wondering how to quit this stupid game. If you do just remember
that you can ask for help on any of the screens when you are asked for input.
(procrastinating instead of coding). So sure if you will be courius enough
to read what was going through my mind than sure just type help and i will
lend you a helping hand. Although you probably you just want to quit -
press Ctrl-Q.                       
                    """)


class Map(object):
    passs

class Engine(object):
    pass