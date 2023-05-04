first_num = int(0)
last_num = int(101)

counter = first_num
new_list = []
while counter <= last_num:
    if counter % 7 == 0 and counter % 5 != 0:
        new_list.append(counter)
    counter += 1
print(new_list)
