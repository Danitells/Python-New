phone_number = input('Please enter your mobile number:')
length = len(phone_number)
if not phone_number.isdigit() and length != 10:
    print('Please enter a valid phone number,it should contains only numerical characters '
          'and be only 10 characters long')
elif not phone_number.isdigit() and length == 10:
    print('Please enter a valid phone number,it should contains only numerical characters ')
elif phone_number.isdigit() and length != 10:
    print('Please enter a valid phone number,it should be only 10 characters long ')
else:
    print('Thank you for your answer, our prisoners will call u and ask about your PrivatBank account')
