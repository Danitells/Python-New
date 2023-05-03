# T ask 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital
# as parameters. Then create a dictionary from those two, with ‘name’
# as a key and ‘capital’ as a parameter. Make the function print out the values of
# the dictionary to make sure that it works as intended.

from countryinfo import CountryInfo

countries_list = []

# Hope u don't mind, I've modified solution a little....too


def get_countries():
    for i in range(1, 6):
        print('Please 5 valid names of country:')
        name_from_user = input()
        countries_list.append(name_from_user)
    return countries_list


def get_countries_capitals(some_list_of_country):
    dict_country = dict()
    for country_nam in some_list_of_country:
        name_of_country: CountryInfo = CountryInfo(country_nam)
        country_capital = name_of_country.capital()
        dict_country_up = {country_nam: country_capital}
        dict_country.update(dict_country_up)
    return print(dict_country)


get_countries()
get_countries_capitals(countries_list)

