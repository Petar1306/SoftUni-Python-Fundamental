budget = int(input())
price_count = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    price_product = int(command)

    if price_count + price_product > budget:
        print("You went in overdraft!")
        break
    price_count += price_product
