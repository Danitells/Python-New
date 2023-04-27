while True:
    test_string = str(input('Write here your string:'))
    test_string_length = len(test_string)
    if test_string =='STOP':
        break
    if test_string_length < 2:
        print('Empty string')
    elif test_string_length == 2:
        print(test_string*2)
    else:
        print(test_string[0:2]+test_string[test_string_length - 2:test_string_length])

