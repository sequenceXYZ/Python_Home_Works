"""
Task 1
 Write a Python function to find the Max of three numbers.
"""
from asyncio import __main__


def max_mum(a, b, c):
    list = [a, b, c]
    return max(list)
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

print(max_mum(a, b, c))



"""
Task 2
Write a Python program to reverse a string
"""
def reverse(string):
    string=string[::-1]
    return string

print(reverse("1234abcd"))



"""
Task 3
"""
def sum_numbers(*value: int) -> float:
    """sum the numbers"""
    return sum(value)


if __name__ == "__main__":
    print(sum_numbers(1.1, 2.2, 5.5))



"""
Task 4
Write a Python program to subtract five days from the current date
"""

from datetime import datetime, timedelta
today = datetime.now()
timedelta = datetime.now() - timedelta(days=5)
print(today)
print(timedelta)


