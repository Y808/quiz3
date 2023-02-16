"""
Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum
"""

x = int(input('first number is '))
y = int(input('second number is '))
z = int(input('third number is '))


def sum_thrice(a, b, c):
    sum = a + b + c

    if a == b == c:
        sum = sum * 3
    return sum


print(sum_thrice(x, y, z))
print(sum_thrice(1, 2, 3))
print(sum_thrice(5, 5, 5))
