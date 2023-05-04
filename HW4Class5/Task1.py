import random
number_random = str(random.randint(1, 10))
string_for_wrong = 'Ha-ha loooooser!You are wrong, the number was {num}!'.format(num=number_random)
try_to_guess = input("Let's check your luck, which number i chose:")
if number_random != try_to_guess:
    print(string_for_wrong)
else:
    print('You are f**cking cheater!')

