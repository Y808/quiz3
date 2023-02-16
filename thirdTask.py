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
