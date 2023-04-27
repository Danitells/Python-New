from datetime import datetime

today = datetime.today().strftime('%A')
name_surname = 'Daria Salhalova'

print('Good day {name}! {today} is a perfect day to learn some python.'.format(name=name_surname, today=today))