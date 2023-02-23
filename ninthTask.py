"""
Write a program to call the given api for get the countries data, fetch "capital"and "currency"
and print a dictionary of fetched information (Capitalize the first letter of the country):

url: https://restcountries.com/v3.1/name/peru

list of countries = [germany, 'australia', 'japan']

finally create a keyword (function) for doing this scenario. The function should get the country name as the argument.

"""


import requests


def get_country_info(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    data = response.json()

    capital = data[0]['capital'][0]
    currency_code = list(data[0]['currencies'].keys())[0]
    currency_name = data[0]['currencies'][currency_code]['name']
    info = {country.capitalize(): {"capital": capital, "currency": currency_name}}

    return info


countries = ['germany', 'australia', 'japan']

for country in countries:
    print(get_country_info(country))
