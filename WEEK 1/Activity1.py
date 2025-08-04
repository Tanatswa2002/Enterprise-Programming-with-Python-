import random
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        flag = 0
        while flag < 4:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username == self.username and password == self.password:
                print("Login successful!")
                return True
            
            else:
                print("Invalid username or password. Please try again.")
                flag += 1

        print("Too many failed attempts. Please try again later.")
        return False
    

    def logout(self):
        print("You have been logged out successfully.")
        return True


class Restraunt:

    def __init__(self, name,location,menu):
        self.name = name
        self.location = location
        self.menu = None

    def add_menu_item(self,menu):
        self.menu = menu
        print(f"Menu item {self.menu} has been added to the restraunt {self.name}.")

    def View_Menu(self):
       self.item_no = 1
       if self.menu is not None:
         print(f"Menu for {self.name} located at {self.location}:")
         for item in self.menu:
            print(f"{self.item_no} : {self.menu}")

class Menu:
    #note: use .append to add items to menu as oppossed to 'meu += item' this
    #could create probems because if it is an iterable like say the string 'Pizza'
    #it would add each character of the string as an item in the menu
    def __init__(self):
        self.menu = [] #create menu list, this will be used to add 
                        #items to the menu
        self.item = None #individual items that will be added to the menu

    def add_item(self,item):
        self.menu.append(item) # item passed into the method in main function
        print(f'Item {self.item} added to menu.')

class Order(User):

    def __init__(self,order_id,user):
        self.order_id = None
        self.user = user

    def place_order(self):
        #generate random order_id
        self.order_id  = random.randint(0,9999)
       
    def track_order(self):
        pass

