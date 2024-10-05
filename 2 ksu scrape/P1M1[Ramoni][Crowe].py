menu = "salad, pasta, sandwich, pizza, drinks, dessert, ravioli, oreos, gummies, wine, water"
print(menu)
add_item = input("what is your item: ")
new_menu = menu + ", " + add_item
print(new_menu)

print(new_menu)
ask = input("What item are you looking for? ")
print(ask,"is in the new menu = ", ask.lower() in new_menu.lower())