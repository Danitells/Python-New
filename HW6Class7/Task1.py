#Make a program that has some sentence
#(a string) on input and returns a dict containing
#all unique words as keys and the number of occurrences as values.


some_sentence = input('Give me some sentence:').lower()

li = list(some_sentence.split(" "))
length_of_list = len(li)
new_dict = dict()
print(li)
for item in li:
    occurrences = some_sentence.count(item)
    if occurrences == 1:
        new_dict.update({item: occurrences})
print(new_dict)





