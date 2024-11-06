import time

# all items avaliable and corosponding price 
items = {
    'jacket': 119.99,
    'gloves': 29.99,
    'shirt': 54.99,
    'shoes': 99.99,
    'glasses': 59.99,
    'hoodie': 74.99,
    'joggers': 64.99,
    'hat': 19.99,
    'watch': 149.99,
    'bracelet': 89.99
}
#listing items avalible and price 
def start_shop():
    print("Jacket: £119.99\nGloves: £29.99\nShirt: £54.99\nShoes: £99.99\nGlasses: £59.99\nHoodie: £74.99\nJoggers: £64.99\nHat: £19.99\nWatch: £149.99\nBracelet: £89.99\n")
    total = 0
    itemList = []
#asking user to inputs items they want
    print("Current Basket: ")
    print("Current total: £0.00")
    while True:
        choice = input("Enter the item that you would like to purchase (leave blank to stop): ").lower()
        print("\033[1A\033[K\033[1A\033[K\033[1A\033[K\033[1A\033[K")
        if choice in items:
            total += items[choice]
            itemList.append(choice)
        elif choice == "":
            print(f"Your item total is £{"{:.2f}".format(round(total,2))}")
            break
        else:
            print("\033[1A\033[K")
            print("Item not available")
            time.sleep(1)
            print("\033[1A\033[K\033[1A\033[K")
        print(f"Current Basket: {str(itemList).replace("'","").replace("[","").replace("]","")}")
        print(f"Current total: £{round(total,2)}")

    return {
        'items': itemList,
        'total_cost': round(total,2)
    }
        