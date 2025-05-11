first_string = input()
second_string = input()
current_string = first_string
for i in range(len(first_string)):
    new_string = second_string[:i] + second_string[i] + first_string[i+1:]
    if new_string != current_string:
        print(new_string)
        current_string = new_string
