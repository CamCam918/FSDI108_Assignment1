"""
author: Cameron Campbell
System: Simple Python calc
"""

# imports
from display import print_menu, print_header

# global vars


# direct instructions
print_header()
print_menu()


option = input("Select an option:")

num1 = float(input("what is first number? > "))
num2 = float(input("what is second number? > "))

if(option == "1"):
    res = num1 + num2

elif(option == "2"):
    res = num1 - num2

elif(option == "3"):
    res = num1 * num2

elif(option == "4"):
    if(num2 == 0):
        print("Whoa There Killer, dividing by 0 will curse your family")
        res = "Error"
    res = num1 / num2

elif(option == "5"):
    msgInput = input("Type your message here>: ")
    msgNum = input(
        "Enter the number of times you want to display your message: ")
    if(msgNum != 0):
        res = msgInput

print(f"The Result is: {res} "*msgNum)
