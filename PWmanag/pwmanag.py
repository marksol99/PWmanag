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
            menu_instance()


        else:
            print("ACCESS DENIED")
            quit()

    def first_start(self):      #Bygger filsystem - ikke ferdig
        try:
            f = open(self.master_path)
            self.auth(self.master_path)

        except FileNotFoundError:
            os.makedirs("PWmanag/data")
            set_pw = input("Set a secure password: ")
            with open(master_path, "a") as f:
                f.write(set_pw)
            self.auth(self.master_path)

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
        length = int(input("Password length(12 char.): "))
        if length <= 12:
            random_pw = "".join(random.choice(string.printable))
            print(random_pw)
        else: 
            print("Password not long enough! Try again.")
            gen_pw()


        


class Menu:
    def __init__(self, master_path):
        self.master_path = master_path

    def show_menu(self):
        print("""
1. Add Password
2. View Passwords
3. Edit Passwords
4. Change Master Password
5. Exit              
              """)
        self.select()
        
    def select(self): ##
        selection = {
            "1": PWManag(self.master_path).add_pw,
            "2": PWManag(self.master_path).view_pw,
            "3": PWManag(self.master_path).edit_pw,
            "4": PWManag(self.master_path).change_mpw,
            "5": PWManag(self.master_path).end
        }

        selected = int(input("Select one(1-5): "))
        print(selected)
        
        if selected in selection:
            selection[selected]()
        else:
            print("ERROR! RETRY!")
            menu_inst = Menu(self.master_path)
            menu_inst.show_menu()


def menu_instance():
    Menu(master_path).show_menu()


def start(master_path):
    PWManag(master_path).first_start()

master_path = "PWmanag/data/master.txt"


start(master_path)