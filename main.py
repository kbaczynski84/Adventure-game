from hero import Hero
from menu import Menu
from locations import Start
from engine import engine

if __name__ == "__main__":

    menu_object = Menu()
    menu_object.welcome_screen()
    hero = menu_object.menu_screen()
    print(hero)
