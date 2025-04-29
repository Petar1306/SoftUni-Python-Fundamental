number_of_lines = int(input())
tank = 255
for line in range(number_of_lines):
    liters_water = int(input())
    if tank - liters_water < 0:
        print("Insufficient capacity!")
        continue
    tank -= liters_water
print(255 - tank)
