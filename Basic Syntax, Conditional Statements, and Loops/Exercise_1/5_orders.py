orders = int(input())
caffe_price = 0
total = 0
for _ in range(0, orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_capsule < 0.01 or price_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    caffe_price = days * capsules_per_day * price_capsule
    total += caffe_price
    print(f"The price for the coffee is: ${caffe_price:.2f}")
print(f"Total: ${total:.2f}")
