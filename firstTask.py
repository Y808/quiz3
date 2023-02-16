x = int(input('first number is '))
y = int(input('second number is '))
z = int(input('third number is '))


def sum_thrice(a, b, c):
    sum = a + b + c

    if a == b == c:
        sum = sum * 3
    return sum


print(sum_thrice(x, y, z))
