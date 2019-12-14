class Hero():
    def __init__(self, name, hitpoints, strength):
        self.name = name
        self.hitpoints = hitpoints
        self.strength = strength
        self.food = 100

    def __str__(self):
        return ("Name: "+ str(self.name)+
                "\nHitpoints: "+ str(self.hitpoints)
                +"\nStrength: " + str(self.strength)
                +"\nFood:" + str(self.food))


    def hero_creator():
        name = input("Enter hero's name>>> ")
        hero = Hero(name, 10, 10)
        return hero


