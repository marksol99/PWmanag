
master_path = "C:/Users/marku/Desktop/PWmanag/master.txt"
pw_manager = PWManag(file_path)

class PWManag:
    def __init__(self, master_path):
        self.master_path = master_path

    def auth(self):   
        master_in = str(input("Enter master password: "))
        with open(master_path, "r") as f:
            master = f.readline().strip()

        if master_in == master:
            print("ACCESS GRANTED")
            menu()

        else:
            print("ACCESS DENIED")
            quit()

    def add_pw():
        pass
    
    def view_pw():
        pass
    
    def edit_pw():
        pass

    def change_mpw():
        pass
    def end():
        pass


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




pw_manager.authenticate_master()