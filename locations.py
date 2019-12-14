

class Locations():

    @staticmethod
    def enter_location(hero):
        hero.food -= 1
        return hero.food


class Start(Locations):
    pass

class Lake(Locations):
    pass

class Dungeon(Locations):
    pass

class Shop(Locations):
    pass