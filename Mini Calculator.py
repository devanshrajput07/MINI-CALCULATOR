#-------------------------------------------------------------------------------
# Name: MINI CALCULATOR
# Purpose:
#
# Author:      Devansh Rajput
#
# Created:     19-09-2022
# Copyright:   (c) Devansh Rajput 2022
# Licence:     <Devansh Rajput licence>
#-------------------------------------------------------------------------------

#Our Calculator

first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----Press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")

