# age = 18

# if age >= 18:
#     print("You are an adult.")



# age = 20
# has_id = True

# if age >= 18:
#     if has_id:
#         print("You are allowed to enter.")
#     else:
#         print("You need to show your ID.")
# else:
#     print("You are not allowed to enter.")


   #if else statement
# i = 20
# if i < 15:
# 	print("i is smaller than 15")
#     print("i'm in if Block")
# else:
# 	print("i is greater than 15")
# 	print("i'm in else Block")
# print("i'm not in if and not in 	else Block")


#nested if
# i = 10
# if i == 10:
#     if i < 15:
#         print("i is smaller than 15")
#     if i < 12:
#         print("i is smaller than 12 too")
#     else:
#          print("i is greater than 15")


# i=20
# if i==10:
#    print("i is 10")
# elif(i==15):
#    print("i is 15")
# elif(i==20):
#    print("i is 20")
# else:
#     print("i is not present")


i=90
if i<=100 and i>=0:
    if i>=90:
        print("A grade")
    elif i>=80:
        ptint("B grade")
    elif i>=70:
        ptint("C grade")
    elif i>=60:
        print("D grade")
    else:
        print("Fail")
else:
        print("invalid mark")


# Program to check whether a number is positive

# Input from user
num = float(input("Enter a number: "))

# Check if the number is positive
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# Program to check if a number is divisible by 5

# Input from user
num = int(input("Enter a number: "))

# Check divisibility
if num % 5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 5.")


# Program to check if a given character is a vowel

# Input from user
char = input("Enter a character: ")

# Check if it's a single alphabetic character
if len(char) == 1 and char.isalpha():
    # Convert to lowercase to handle both uppercase and lowercase inputs
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")
else:
    print("Please enter a single alphabet letter.")


# Program to check if the entered string is "Python"

# Input from user
user_input = input("Enter a string: ")

# Check if it matches "Python" exactly
if user_input == "Python":
    print("The entered string is 'Python'.")
else:
    print("The entered string is not 'Python'.")


# Program to check whether a number is even or odd

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# Program to check voting eligibility

# Input from the user
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Program to find the greater number between two numbers

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers
if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")


# Program to check whether a year is a leap year

# Input from the user
year = int(input("Enter a year: "))

# Check leap year conditions
if (year % 4 == 0):
    if (year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")
