your_name_input = input('Please write your name:')
your_age_input = int(input('Please write your age:'))+1
greeting = 'Hello {name}, on your next birthday you’ll be {age} years'.format(name=your_name_input, age=your_age_input)
print(greeting)
