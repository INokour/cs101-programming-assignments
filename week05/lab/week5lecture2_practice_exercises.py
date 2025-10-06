import sys
# '''
# practice exercise 1-a
# '''
# # TODO: Complete this program
# # Ask for age and print the appropriate category
# # Child: 0-12
# # Teen: 13-17
# # Adult: 18-64
# # Senior: 65+

# age = int(input("Enter your age: "))

# age_group = "Child";

# if age < 12:
#     age_group = "Child"
# elif age < 17:
#     age_group = "Teen"
# elif age < 64:
#     age_group = "Adult"
# else:
#     age_group = "Senior"

# print(f"You are a {age_group}")

# # Write your code here

# # sys.exit(0) -- to test your code, uncomment this and exit 
# #             -- to see the prompt

# '''
# practice exercise 1-b
# '''
# # TODO: Complete this program
# # Ask for temperature in Fahrenheit
# # Give appropriate clothing advice

# temp = float(input("What's the temperature (F)? "))

# if temp < 32:
#     print(f"({temp}º) Wear a heavy coat!")
# elif temp < 51:
#     print(f"({temp}º) Wear a jacket")
# elif temp < 86:
#     print(f"({temp}º) Wear a light sweater!")
# else:
#     print(f"({temp}º) Wear shorst and stay cool!")

# # Write your code here
# # Below 32: "Wear a heavy coat!"
# # 32-50: "Wear a jacket"
# # 51-70: "Wear a light sweater"
# # 71-85: "Wear a t-shirt"
# # Above 85: "Wear shorts and stay cool!"

# # sys.exit(0)
# #

# '''
# practice exercise 1-c
# '''
# # TODO: Complete this program

# # Underweight: BMI < 18.5
# # Normal: 18.5 <= BMI < 25
# # Overweight: 25 <= BMI < 30
# # Obese: BMI >= 30

# weight = float(input("Enter weight in pounds: "))
# height = float(input("Enter height in inches: "))

# # Calculate BMI and provide category with health advice

# BMI = (weight / height ** 2) * 703

# if BMI < 18.5:
#     print("BMI: ({BMI}) You are underweight.")
# elif 18.5 <= BMI < 25:
#     print("BMI: ({BMI}) You are at a normal BMI.")
# elif 25 <= BMI < 30:
#     print("BMI: ({BMI}) You are overweight.")
# else:
#     print("BMI: ({BMI}) You are obese.")

# # sys.exit(0)

# # # '''
# # practice exercise 2-a
# # '''
# # # TODO: Complete this program
# # # Regular price: $12
# # # Child (under 12): $8
# # # Senior (65+): $8
# # # Tuesday discount: All tickets $6

# price = 12.00

# age = int(input("Enter your age: "))
# day = input("What day is it? ").lower()

# if age < 12 or age > 64:
#     price = price - 4.00;
# elif day == "tuesday":
#         price = 6.00
# else:
#     price = 12.00

# print (f"Ticket price for a {age} year old on {day} is ${price}.")


# # Write nested if statements here

# # sys.exit(0)

# '''
# practice exercise 2-b
# '''
# # TODO: Complete this program
# # Must be enrolled (yes/no)
# # If enrolled, check if full-time or part-time
# # Full-time with GPA >= 3.5: 20% discount
# # Full-time with GPA < 3.5: 10% discount
# # Part-time: 5% discount
# # Not enrolled: No discount

# enrolled = input("Are you enrolled? (yes/no): ").lower()

# studentEnrolled = False

# partTime = False

# if enrolled == "yes": 
#     studentEnrolled = True
# else:
#     studentEnrolled = False;

# if studentEnrolled:
#     partTimeInput = input("Full-time? (yes/no): ").lower()
#     if partTimeInput == "yes":
#         partTime = False
#     else:
#         partTime = True
#     gpa = float(input("What is your GPA?"))
# else:
#     partTime = False
#     gpa = 0.0



# if studentEnrolled and gpa >= 3.5 and not partTime:
#     print("You will recieve a 20% discount.")
# elif studentEnrolled and gpa < 3.5 and not partTime:
#     print("You will recieve a 10% discount.")
# elif studentEnrolled and partTime:
#     print("You will recieve a 5% discount.")
# elif not studentEnrolled and not partTime:
#     print("You will not recieve any discount.")

# # Write your nested logic here

# # sys.exit(0)

'''
practice exercise 2-c
'''

# TODO: Complete this program
# Check: Valid PIN (1234)
# Check: Sufficient balance
# Check: Daily limit ($500)
# Check: Bills available (multiples of $20)

balance = 1000  # Starting balance
daily_withdrawn = 0  # Amount already withdrawn today

billsAvailable = (balance - daily_withdrawn) / 20

pin = input("Enter PIN: ")

validPin = False

if pin == ("1234"):
    validPin = True

if validPin:
    print("Pin is valid.")
    if balance > 20:
        print("Sufficient balance. ${balance}")

    withdraw = input(f"How much would you like? [Balance: ${balance - daily_withdrawn}, Max: {billsAvailable}]\n Enter a Number: ")
    withdrawal = int(withdraw) * 20
    print(f"You have withdrawn ${withdrawal}, using {withdraw} $20 Bills")



# Write your nested validation logic here
# Include appropriate error messages for each check


# sys.exit(0)

'''
practice exercise 3-a
'''
# TODO: Complete this program
# Correct username: "student"
# Correct password: "learn123"
# Both must be correct to login

username = input("Username: ")
password = input("Password: ")

# Use 'and' to check both conditions


# sys.exit(0)

'''
practice exercise 3-b
'''
# TODO: Complete this program
# To pass, student needs:
# - Midterm score >= 60
# - Final score >= 60
# - Average of both >= 70

midterm = float(input("Midterm score: "))
final = float(input("Final score: "))
average = (midterm + final) / 2

# Write your logic using 'and'



# sys.exit(0)

# '''
# practice exercise 3-c
# '''
# # TODO: Complete this program
# # Requirements for approval:
# # - Age >= 18 and Age <= 75
# # - Income >= 25000
# # - Credit score >= 650
# # Show specific reasons for denial

# age = int(input("Age: "))
# income = float(input("Annual income: "))
# credit_score = int(input("Credit score: "))

# # sys.exit(0)

# '''
# practice exercise 4-a
# '''
# # TODO: Complete this program
# # Weekend: Saturday or Sunday
# # Holiday: If user says "yes"
# # Either weekend OR holiday = day off

# day = input("What day is it? ").lower()
# is_holiday = input("Is it a holiday? (yes/no): ").lower()

# # Use 'or' to check for day off



# # sys.exit(0)

# '''
# practice exercise 4-b
# '''
# # TODO: Complete this program
# # Password rules:
# # - Must NOT be empty
# # - Must NOT be "password" or "12345"
# # - Must NOT be less than 6 characters

# password = input("Create password: ")

# # Use 'not' to check invalid conditions
# # sys.exit(0)

# '''
# practice exercise 4-c
# '''
# # TODO: Complete this program
# # Can seat if:
# # - (Table available) OR (bar seats available and age >= 21)
# # - NOT during rush hour (12-14 or 18-20)
# # - NOT at capacity (100 people)

# current_hour = int(input("Current hour (0-23): "))
# people_count = int(input("People currently in restaurant: "))
# tables_available = input("Tables available? (yes/no): ").lower()
# bar_seats = input("Bar seats available? (yes/no): ").lower()
# customer_age = int(input("Customer age: "))

# # Write complex logic using or, and, not

# # sys.exit(0)

# '''
# practice exercise 5-a
# '''
# # TODO: Complete this program
# # Check if input is not empty AND starts with 'A'
# # Use short-circuit to prevent error on empty string

# user_input = input("Enter a word: ")

# # Check safely using short-circuit
# # Hint: Check if not empty first, then check first letter


# # sys.exit(0)

# '''
# practice exercise 5-b
# '''
# # TODO: Complete this program
# # Menu options: 1, 2, 3, or 'q' to quit
# # Check if input is digit before converting to int
# # Use short-circuit for efficiency

# choice = input("Enter choice (1-3 or 'q'): ")

# # Validate efficiently
# # If 'q', quit immediately
# # If digit, check if in valid range

# # sys.exit(0)

# '''
# practice exercise 5-c
# '''
# # TODO: Complete this program
# # Input: test scores as strings (might be invalid)
# # Only calculate average if ALL inputs are valid
# # Use short-circuit to stop at first invalid input

# print("Enter 3 test scores")
# test1_str = input("Test 1: ")
# test2_str = input("Test 2: ")
# test3_str = input("Test 3: ")

# # Validate all inputs efficiently
# # Check each is digit AND in range 0-100
# # Calculate average only if all valid
# # Show specific error for first invalid input



# # sys.exit(0)
