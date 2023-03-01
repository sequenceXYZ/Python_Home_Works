"""
Task 1
Write a small program that assigns the name of 2 items to 2 variables.
If the values of the 2 variables are equal,
print the message ”The items are the same”. Otherwise, print ”The items are different”
"""
a = 10
b = 0
if a == b:
    print("The items are the same")
else:
    print("The items are different")



"""
Task 2
Write a program to ask for a name and an age.
When both values have been entered, check if the person is the right age to enter the club. 
A person must be an adult.
If they are, welcome them. 
Otherwise, print a polite refusing them entry.
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age == 18:
    print("Welcome, " + name + "!")
elif age >= 18:
    print("Welcome, " + name + ", you are an adult!")
else:
    print("Entrance is not allowed, " + name + ", you are not an adult!")



"""
Task 3
Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
"""
for i in range(0, 100):
    if i % 7 == 0:
        print(i)



"""
Task 4
Write a program in Python to reverse a word. Words should be provided using input function.
"""

word = input("Enter a word: ")
averse = word[:]
reverse = word[::-1]
print(averse)
print(reverse)



"""
Task 5
WWrite a function called factorial that will return the factorial of the number passed as its argument.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
num = factorial(n)
print('Factorial number of', n, 'is', num)