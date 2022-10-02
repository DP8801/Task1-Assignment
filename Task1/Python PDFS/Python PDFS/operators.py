#Task 1.2 (Operators)
#1. Write a function for arithmetic operators(+,-,*,/) 
print("1.2.1 Write a function for arithmetic operators(+,-,*,/) ")
def operations(first_num, second_num):
    print("Addition(+) : "+ str(first_num + second_num))
    print("Subtraction(-) : "+ str(first_num - second_num))
    print("Multiplication(*) : "+ str(first_num * second_num))
    print("Divison(/) : "+ str(first_num / second_num))
    print()


first_num = int(input("Enter your first number: "))

second_num = int(input("Enter your second number: "))

operations(first_num, second_num)


#2. Write a method for increment and decrement operators(++, --)

# NOTE: There is no implicit increment or decrement in Python as in conventional programming language although it have a short hand for icrement and decrement
print("1.2.2 Write a method for increment and decrement operators(++, --)")
num1 = 5  
num1 += 1
print(num1)
num1 -= 3
print(num1)
print()

#3. Write a program to find the two numbers equal or not

# NOTE: Relational operators return boolean (True | False)
print("1.2.3 Write a program to find the two numbers equal or not")
num2 = int(input("Enter First Number: "))
num3 = int(input("Enter Second Number: "))
if(num2 == num3):
    print(f"{num2} = {num3}\n")
else: 
    print("Not Equal!\n")


#4. Program for relational operators (<,<==, >, >==
print("1.2.4 Program for relational operators (<,<==, >, >==)")
num4 = int(input("Enter Your Number: "))
num5 = int(input("Enter Another Number: "))
print(f"{num4} < {num5} "+str(num4 < num5))
print(f"{num4} <= {num5} "+str(num4 <= num5))
print(f"{num4} > {num5} "+str(num4 > num5))
print(f"{num4} >= {num5} "+str(num4 >= num5))
print()


#5. Print the smaller and larger number

print("1.2.5 Print the smaller and larger number")
num6 = int(input("Enter First Number: "))
num7 = int(input("Enter Another Number: "))

if(num6 > num7):
    print(f"{num6} is larger than {num7}")
elif(num6 < num7):
    print(f"{num7} is larger than {num6}")
else:
    print(f"{num6} is equal to {num7}")



