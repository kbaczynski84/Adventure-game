import time
from hero import Hero


class Menu:

    def welcome_screen(self):
        print("""                    ____________________________
                    Welcome to my Text based RPG
                    Loading. Please wait.
                 """)
        time.sleep(3)

    def menu_screen(self):
        while True:
            print("""
                RPG!        
        1. Start a new game
        2. Highscores -- Build in progress
        3. Exit
        """)
            choice = input("Go ahead 1, 2 or 3. Then Press Enter> ")
            if choice == "1":
                Hero.hero_creator()
                break
            if choice == "2":
                pass
            if choice == "3":
                exit()
            else:
                pass

