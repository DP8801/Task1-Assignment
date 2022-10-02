#1 Write a program to print “Bright IT Career” ten times using for loop
print("1.3.1 Write a program to print “Bright IT Career” ten times using for loop")
for i in range(10):
    print("Bright IT Career")
print()

#2 Write a program to print 1 to 20 numbers using the while loop
print("1.3.2 Write a program to print 1 to 20 numbers using the while loop")
counter = 1
while counter <= 20:
    print(counter)
    counter+=1
print()

#3 Program to equal operator and not equal operators
print("1.3.3 Program to equal operator and not equal operators")
even_counter = 0
odd_counter = 0
for i in range(100):
    if(i % 2 != 0):
        odd_counter+=1
    elif(i % 2 == 0):
        even_counter+=1
        
print(f"Number of Odd numbers is {odd_counter} and Number of Even Number is {even_counter}")
print()

#4 Write a program to print the odd and even numbers.
print("1.3.4 Write a program to print the odd and even numbers.")
number = int(input("Enter your number: "))
for i in range(number):
    if(i % 2 != 0):
        print(f"{i} is Odd")
    elif(i % 2 == 0):
        print(f"{i} is Even")

print()
#5 Write a program to print largest number among three numbers.
print("1.3.5 Write a program to print largest number among three numbers.") 
max = 0
counter = int(input("How many numbers do you have want to compare : "))
for i in range(counter):
    number = int(input(f"Enter {i+1}th number: "))
    if max < number:
        max = number

print(f"Largest number of the {counter} number is {max}")

print()
#6 Write a program to print even number between 10 and 20 using while
print("1.3.6 Write a program to print even number between 10 and 20 using while")
counter = 10
while counter <= 20:
    if((counter % 2) == 0):
        print(f"{counter} is even")
    counter += 1
print()

#7 Write a program to print 1 to 10 using the do-while loop statement

# NOTE : Python doesn't have do-while loop. But we can create a program by while loop. The do while loop is used to check condition after executing the statement. It is like while loop but it is executed at least once.

print("1.3.7 Write a program to print 1 to 10 using the do-while loop statement")

counter = 10

while True:
    print(counter)
    counter += 1
    if(counter > 20):
        break
    else:
        continue
    
print()

#8 Write a program to find Armstrong number or not
print("1.3.8 Write a program to find Armstrong number or not")

number = input("Enter the number to be checked as armstrong number : ") 
total = 0
for i in number:
    total += (int(i) ** 3)

if total == int(number):
    print(f"Given number {number} is an armstrong number")
else:
    print(f"Given number {number} is NOT an armstrong number")

print()

#9 Write a program to find the prime or not
print("1.3.9 Write a program to find the prime or not")
number = int(input("Enter the number: "))

if number == 1:
    print("1 is neither prime nor composite...")
else:
    isPrime = True
    for i in range(2,number//2):
        if number % i == 0:
            isPrime = False
            break
    if(isPrime):
        print(f"{number} is prime...")
    else:
        print(f"{number} is divisible by {i} hence it is not a prime")
    
print()

#10 Write a program to palindrome or not
print("1.3.10 Write a program to palindrome or not")
def isPalindrome(arg):
    txt = ""
    for i in arg[::-1]:
        txt += i
    
    if txt == arg:
        return True
    else:
        return False

Userin = input("Enter number or string(👉All UpperCase👈) to sheck palindrome : ")
if isPalindrome(Userin):
    print(f"{Userin} is palindrome")
else:
    print(f"{Userin} is not palindrome")

print()

#11 Program to check whether a number is EVEN or ODD using switch
print("1.3.11 Program to check whether a number is EVEN or ODD using switch")

# NOTE : Python don't have switch case

number = int(input("Enter number : "))
rem = number % 2

if rem==0: print("EVEN")
else: print("ODD")

print()

#12 Print gender (Male/Female) program according to given M/F using switch
print("1.3.12 Print gender (Male/Female) program according to given M/F using switch")

print()
# NOTE : No switch case in python

gender = input("Enter you gender (m/f) : ")
if (gender == 'm'):
    print("MALE")
else:
    print("FEMALE")