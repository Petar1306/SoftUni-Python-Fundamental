num_messages = int(input())
for num in range(1, num_messages +1):
    new_code = int(input())
    if new_code == 88:
        print("Hello")
    elif new_code == 86:
        print("How are you?")
    elif new_code < 88:
        print("GREAT!")
    elif new_code > 88:
        print("Bye.")
