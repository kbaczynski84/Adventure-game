class Hero():
    def __init__(self, name, hitpoints, strength):
        self.name = name
        self.hitpoints = hitpoints
        self.strength = strength

    def __str__(self):
        return ("Name: "+ str(self.name)+
                "\nHitpoints: "+ str(self.hitpoints)
                +"\nStrength: " + str(self.strength))

    @staticmethod
    def hero_creator():
        name = input("Enter hero's name>>> ")
        hero = Hero(name, 10, 10)
        print(hero)

