""""
Write a program to get the user info (name, age, gender)
by prompting and print the result like this: 'Your info: {"name": "Jack", "age": 34, "gender": "male" }'
"""
name = input("Enter your name:")
age = int(input("Enter your age:"))
gender = input("Enter your gender:")

print(f'Your info:{{"name": {name}, "age": {age}, "gender": {gender}}}')
