command = input()

while command != "End":
    if command != "SoftUni":
        current_string = ""
        for character in command:
            current_string += character * 2
        print(current_string)
    command = input()
