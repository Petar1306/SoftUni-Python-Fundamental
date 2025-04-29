number_of_lines = int(input())
result = 0
for _ in range(1, number_of_lines+1):
    string = input()
    for i in string:
        result += ord(i)
print(f"The sum equals: {result}")
