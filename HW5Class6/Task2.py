import random
list_of_numbers1 = []
list_of_numbers2 = []
while len(list_of_numbers1) != 10:
    rand_num1 = random.randint(1, 10)
    list_of_numbers1.append(rand_num1)

while len(list_of_numbers2) != 10:
    rand_num2 = random.randint(1, 10)
    list_of_numbers2.append(rand_num2)

print(list_of_numbers1)
print(list_of_numbers2)

set_from_list1 = set(list_of_numbers1)
set_from_list2 = set(list_of_numbers2)

print(set_from_list1)
print(set_from_list2)

list_of_intersection = list(set_from_list1.intersection(set_from_list2))
print(list_of_intersection)




