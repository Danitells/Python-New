# Users/daryasalgalova/Desktop/example_file.py

def count_lines(name):
    with open("/Users/daryasalgalova/Desktop/{file_name}".format(file_name=name), "r") as file:
        length_of_lines = len(file.readlines())
        return length_of_lines


def count_chars(name):
    lines_len = count_lines(name)
    with open("/Users/daryasalgalova/Desktop/{file_name}".format(file_name=name), "r") as file:
        chars = file.read()
        len_chars = len(chars)
        return len_chars


def test(name):
    print(count_chars(name))
    print(count_lines(name))


test('example_file.txt')