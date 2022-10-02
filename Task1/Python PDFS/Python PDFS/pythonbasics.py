#Task 1.1 (Python Basics)
#1. Write a program to print your name

def greeting(name):
    print(f"Hello🎉 {name}")

greeting(input("Enter Your Name:"))
print()

# ````````````````````````````````````````````````````````````````````
#2. Write a program for a Single line comment and multi-line comments

#Single Line Comment
print("single line comments are written like👉: #Single line comment")
"""Multiline 
    Comments"""
print("Multiline Comments are written like👉: \"\"\" Multilines \"\"\" ")
print()

# ````````````````````````````````````````````````````````````````````
# 3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

salary = 20_000  #int
employed = False #Boolean
aplhabet = 'a'   #char
height = 5.11    #float == double because python don't have specific datatype double

print(f"salary: {salary}\nemployed = {employed}\naplhabet(char) = {aplhabet}\nheight = {height}")

# ````````````````````````````````````````````````````````````````````
#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variable

#Side Note: Global variables are those which are not defined inside any function and have a global scope whereas local variables are those which are defined inside a function and its scope is limited to that function only.

print()
s = "outside function (Global)"

def foo():
    s = "inside function (Local)"
    print(s)

print(s)
foo()