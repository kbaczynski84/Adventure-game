from random import random
from sys import exit

name = input("Hello what is your name?")



class Hero(object):
    def __init__(self, hit_points, strength, money, name, food):
            self.hit_points = hit_points
            self.strength = strength
            self.money = money
            self.name = name
            self.food = food


    axe = False
    pickaxe = False
    bow = False
    fishingrod = False

    def hp_test(self):
        if Hero.hit_points <= 0:
            Death.enter()
        else:
            pass

    def hunger_test(self):
        if Hero.food <= 0:
            Death.enter()
        else:
            pass

    def equip(self):
        if Hero.axe == True:
            Hero.strength += 10
        elif Hero.pickaxe == True:
            Hero.strength += 5
        elif Hero.bow == True:
            Hero.strength += 2
        else:
            pass

# this method i think it will be easier to assign to creature to only fight hero
    def fight(self, hero, creature):
        hp1 = Hero.hit_points
        hp2 = Creature.hit_points
        damage1 = Hero.strength.equip
        damage2 = Creature.strength
        while hp1  > 0 or hp2 > 0:
            hp1 -= damage2,
            hp2 -= damage1
        else:
            print(f"You lost {hp1} HP, your opponent lost {hp2} HP")

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
        elif self.buy == "attack" or "kill":
            pass
        elif self.buy == "run" or "leave":
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
        print(Death.motivation[random.randint(0, len(self.motivation)-1)])
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
        # Spojrzec na mape

        print("""
You probaly are wondering how to quit this stupid game. If you do just remember
that you can ask for help on any of the screens when you are asked for input.
(procrastinating instead of coding). So sure if you will be courius enough
to read what was going through my mind than sure just type help and i will
lend you a helping hand. Although you probably you just want to quit -
press Ctrl-Q""")


class Map(object):
    """Map gonna look like this        5
                                       4
                                   3   1   2
    """

    map = {
        0: "Death",
        1: "Start",
        2: "Shop",
        3: "Lake",
        4: "Forest",
        5: "Dungeon"
    }

    exits = {
        0: {"D": 0},
        1: {"E": 2, "N": 4, "W": 3, "D": 0},
        2: {"W": 1, "D": 0},
        3: {"E": 1, "D": 0},
        4: {"S": 1, "N": 5, "D": 0},
        5: {"S": 4, "D": 0}

    }

    vocabulary = {
        "Death": "D",
        "North": "N",
        "South": "S",
        "East": "E",
        "West": "W"
    }

    loc = 1
    while True:
        availableExits = ""
        for direction in exits[loc].keys():
            availableExits += direction + ","

        print(map[loc])
        if loc == 0:
            break

        direction = input("Available exits are " + availableExits).upper()
        print()

        if len(direction) > 1:
            for word in vocabulary:
                if word in direction:
                    direction = vocabulary[word]

        if direction in exits[loc]:
            loc = exits[loc][direction]
        else:
            print("You cannot go in that direction")


class Engine(object):
    pass