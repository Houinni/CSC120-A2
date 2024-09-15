# Import a few useful containers from the typing module
from computer import Computer

# Import the functions we wrote in procedural_resale_shop.py
from oo_resale_shop import ResaleShop

class main:
    # First, let's make some computer
    new = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
   
    new1 = Computer(
        "Mac Pro (Late 2012)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
   
    
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
   

    # Add it to the resale store's inventory
    resale_shop=ResaleShop()
    resale_shop.buy(new)
    resale_shop.buy(new1)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", 1 , ", updating OS to", new_OS)
    print("Updating inventory...")
    resale_shop.refurbish(1, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Update the price
    new_price=1500
    print("Updating the price of",1, "to", new_price)
    resale_shop.update_price(1,new_price)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling Item ID:", 1)
    resale_shop.sell(1)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Prints appropriate error messages
    resale_shop.refurbish(1, new_OS)
    resale_shop.refurbish(1)
    resale_shop.sell(1)
    resale_shop.update_price(1,1500)

# Calls the main() function when this file is run
if __name__ == "__main__": main()
