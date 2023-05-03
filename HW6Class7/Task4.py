week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

numbers_first = {week.index(day)+1: day for day in week}
print(numbers_first)
numbers_second = {day: week.index(day)+1 for day in week}
print(numbers_second)
