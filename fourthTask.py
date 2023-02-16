"""
Write a Python program to sort a given dictionary by key.
"""

dict1 = {
    "Armenia": "Yerevan",
    "Ukraine": "Kyiv",
    "Japan": "Tokyo",
    "Iran": "Tehran",
    "Austria": "Vienna",
    "Germany": "Berlin",
    "United States": "Washington DC"}

sorted_dictionary = {}
for i in sorted(dict1.keys()):
    sorted_dictionary[i] = dict1[i]

print(sorted_dictionary)
