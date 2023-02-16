"""
Write a program to map the given list to the given dictionary and create a list of the values of the keys
available in the dictionary. list1= [ 'Armenia', 'United States', 'Iran']

dict1 = { "Armenia": "Yerevan", "Russia": "Moscow" , "Japan": "Tokyo", "Iran": "Tehran", "Austria": "Vienna",
"Germany": "Berlin", "United States": "Washington DC"} output: ['Yerevan', 'Washington DC', Tehran]
"""

list1 = ['Armenia', 'United States', 'Iran']

dict1 = {
    "Armenia": "Yerevan",
    "Ukraine": "Kyiv",
    "Japan": "Tokyo",
    "Iran": "Tehran",
    "Austria": "Vienna",
    "Germany": "Berlin",
    "United States": "Washington DC"}

list1 = list(map(dict1.get, list1))

print(list1)
