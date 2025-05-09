budget = float(input())
kg_flour_price = float(input())
pack_eggs_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price * 1.25
milk_per_bread = liter_milk_price * 0.250

bread_cost = kg_flour_price + pack_eggs_price + milk_per_bread
bread = 0
colored_eggs = 0
while budget >= bread_cost:
    bread += 1
    colored_eggs += 3
    if bread % 3 == 0:
        colored_eggs -= (bread - 2)
    budget -= bread_cost
print(f"You made {bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
