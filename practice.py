total = 0
name = []
item_price = []
while True:
    item_name = input("Enter the name of item or to quit press q: ")
    if item_name != "q":
        price = input("Enter a price:")
        total += int(price)
        # if item_name != "q":
        name.append(item_name)
        item_price.append(price)
    else:
        print(name)
        print(item_price)
        print(f"Total: {total}\nThanks for shopping!!")
        break
