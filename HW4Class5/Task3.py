import random

string_from_user = input('Write here your string:')
len_of_user_string = len(string_from_user)
counter = 0
while counter < len_of_user_string:
    key_list = [random.choice(string_from_user) for i in range(len_of_user_string)]
    print("".join(key_list).lower())
    counter +=1
