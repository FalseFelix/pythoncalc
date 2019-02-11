"""
Homework 7.3: Calculator

Write a program that does the basic arithmetic operations:

addition (+),
subtraction (-),
multiplication (*),
and division (/).
Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
"""

Number1 = int(input("Zahl1: "))

operation=input("+, -, *, /")

Number2 = int(input("Zahl2: "))



if operation=="+":
    print(Number1+Number2)
elif operation=="-":
    print(Number1-Number2)
elif operation=="*":
    print(Number1*Number2)
else:
    print(Number1/Number2)