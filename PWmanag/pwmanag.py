import random
import string
from pathlib import Path
import os

class PWManag:
    def __init__(self, master_path):
        self.master_path = master_path

    def auth(self, master_path):   
        master_in = str(input("Enter master password: "))
        with open(master_path, "r") as f:
            master = f.readline().strip()

        if master_in == master:
            print("ACCESS GRANTED")
            menu()

        else:
            print("ACCESS DENIED")
            quit()

    def first_start(self):      #Bygger filsystem - ikke ferdig
        try:
            f = open("data/master.txt")
            self.auth(master_path)

        except:
            os.makedirs("PWmanag/data")
            set_pw = input("Set a secure password: ")
            with open(master_path, "a") as f:
                f.write(set_pw)
            self.auth()

        return

        
    def add_pw(self):
        pass
        
    
    def view_pw(self):
        pass
    
    def edit_pw(self):
        pass

    def change_mpw(self):
        pass

    def end(self):
        pass

    def gen_pw(self):
        length = int(input("Password length(12 characters minimum.): "))
        if length <= 12:
            random_pw = "".join(random.choice(string.printable))
        else: 
            print("Password not long enough! Try again.")
            gen_pw()


        


class Menu:
    def __init__(self):
        pass

    def show_menu(self):
        print("""
1. Add Password
2. View Passwords
3. Edit Passwords
4. Change Master Password
5. Exit              
              """)
    def select():
        Menu.show_menu()
        selection = {
            "1": PWManag.add_pw(),
            "2": PWManag.view_pw(),
            "3": PWManag.edit_pw(),
            "4": PWManag.change_mpw(),
            "5": PWManag.end()
        }


def menu():
    Menu().select()


def start():
    PWManag(master_path).first_start()

master_path = "PWmanag/data/master.txt"


start()