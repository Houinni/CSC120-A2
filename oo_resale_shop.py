from computer import Computer
class ResaleShop:
    
    # What attributes will it need?
   
    inventory = {}
    item_id = 0
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self):
        self.inventory = {}
        self.item_id = 0

    # What methods will you need?
    # To store computers in the inventory, assign an id number to each of them
    def buy(self, computer: Computer):
        self.item_id += 1
        self.inventory[self.item_id] = computer
        print(self.item_id)
        return self.item_id

    # To sell computers based on their id    
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")

    # to update the price of a computer, with its id, new price as inputs
    def update_price(self,item_id: int, new_price: int):
        if item_id in self.inventory:
            computer= self.inventory[item_id]
            computer.price=new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    # to check all computers' details in the inventory
    def print_inventory(self):
        if self.inventory:
            for item_id in self.inventory:
                print(f'Item ID: {item_id} : {vars(self.inventory[item_id])}')
                #print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
    
    # to refurbish computers, set new prices, updating operation systems
    def refurbish(self, item_id: int, new_os: str = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
                print( "price set to 0")
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
                print( "price set to 250")
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
                print( "price set to 550")
            else:
                computer.price = 1000 # recent stuff
                print( "price set to 1000")

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
                print(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

