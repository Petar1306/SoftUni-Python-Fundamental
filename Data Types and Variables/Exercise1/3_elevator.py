# from math import ceil
#
# number_of_people = int(input())
# capacity = int(input())
# courses_needed = ceil(number_of_people / capacity)
# print(courses_needed)
number_of_people = int(input())
capacity = int(input())
courses_needed = number_of_people // capacity
if number_of_people % capacity != 0:
    courses_needed += 1
print(courses_needed)
