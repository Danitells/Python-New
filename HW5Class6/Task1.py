import random

list_of_numbers = []
while len(list_of_numbers) != 10:
    rand_num = random.randint(-1000, 1000)
    list_of_numbers.append(rand_num)
print('First option')
list_of_numbers.sort()
print(list_of_numbers)
print(list_of_numbers[9])

# OR

print('Another option')
max_num = max(list_of_numbers)
print(max_num)
