from computer import Computer
class ResaleShop:
    
    # What attributes will it need?
   
    inventory= []
    item_id = 0
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self):
        self.inventory = []
        self.item_id = 0

    # What methods will you need?
    # To store computers in the inventory, assign an id number to each of them
    def buy(self, computer: Computer):
        self.item_id += 1
        self.inventory.append({"id": self.item_id, "computer": computer})
        print(self.item_id)
        return self.item_id

    # To sell computers based on their id    
    def sell(self, item_id: int):
        found=False
        for item in self.inventory:
            if item["id"] == item_id:
                found=True
                self.inventory.remove(item)
                print("Item", item_id, "sold!")
                break
        if not found:
            print("Item", item_id, "not found. Please select another item to sell.")

    # to update the price of a computer, with its id, new price as inputs
    def update_price(self,item_id: int, new_price: int):
        found=False
        for item in self.inventory:
            if item["id"] == item_id:
                found=True
                computer= item["computer"]
                computer.price=new_price
        if not found:
            print("Item", item_id, "not found. Cannot update price.")

    # to check all computers' details in the inventory
    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {item["id"]}, Details: {vars(item["computer"])}')
                #print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
    
    # to refurbish computers, set new prices, updating operation systems
    def refurbish(self, item_id: int, new_os: str = None):
        found = False
        for item in self.inventory:
            if item["id"] == item_id:  
                found=True
                computer = item["computer"] 
                if int(computer.year_made) < 2000:
                    computer.price = 0  
                    print("Price set to 0")
                elif int(computer.year_made) < 2012:
                    computer.price = 250  
                    print("Price set to 250")
                elif int(computer.year_made) < 2018:
                    computer.price = 550  
                    print("Price set to 550")
                else:
                    computer.price = 1000  
                    print("Price set to 1000")

                if new_os is not None:
                    computer.operating_system = new_os 
                    print(f"Operating system updated to {new_os}")
                break  
        if not found:
            print("Item", item_id, "not found. Please select another item to refurbish.")

