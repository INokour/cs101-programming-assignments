def add(a, b):
    return a + b
# Call add with 5 and 3
result = add(5, 3)
print(result) # Should print 8

def multiply(a=1, b=1, c=1):
    return a * (b or 1) * (c or 1)
# Test it
print(multiply(2, 3, 4)) # Should print 24

def format_date(month, date, year):
    return f"{month:02}/{date:02}/{year}"

print(format_date(5, 3, 2024)) # Should print "03/05/2024"
print(format_date(15, 12, 2024)) # Should print "12/15/2024"


def welcome(name="Student"):
    print(f"Welcome, {name}!")
# Call with your name
welcome("Ibrahim")
welcome()
# Call without any argument

def power(base, exp=2): # Add default here
    return base ** exp
print(power(5)) # Should print 25 (5²)
print(power(5, 3)) # Should print 125 (5³)

def calculate_discount(discount=10, price=1, tax=8):
# Calculate discounted price with tax
    discounted = price * (1 - discount/100)
    final = discounted * (1 + tax/100)
    return final
print(calculate_discount())

def divide(dividend, divisor):
    return dividend / divisor
# Call with dividend=20, divisor=4 using keywords
result = divide(20, 4)
print(result) # Should print 5.0

def register(first_name, last_name, age, email=""):
    print(f"{first_name} {last_name}, age {age}")
    if email:
        print(f"Email: {email}")
register("John", "Doe", 25, email="jdoe@email.com")

def process(a, b, c):
    return a + b + c
# Why does this fail?
# result = process(a=1, 2, c=3) # SyntaxError!
# 2 isn't assigned to a parameter


def greet(first, last="User", title=""):
    print(f"{title} {first} {last}")
# Mark each as VALID or INVALID:
# A. greet("John") #Valid
# B. greet(first="John") #Valid
# C. greet("John", "Doe", "Mr.") #Valid
# D. greet(title="Ms.", "Jane") #Invalid

def configure_game(width, height, fullscreen=False, volume=50, difficulty="normal"):
    pass
# Rewrite this confusing call using keywords:
configure_game(width=800, height=600, fullscreen=True, volume=75, difficulty="hard")

# Hint: Use **kwargs
def print_info(name, **extras):
    age = f"{extras["age"]}" or ""
    city = extras["city"] or ""
    job = extras["job"] or ""
    print(f"Name: {name} | Age: {age} | City: {city} | Job: {job}")
# Print any extra keyword arguments
# Should work with:
print_info("Alice", age=25, city="Boston", job="Engineer")

def get_coordinates():
    return 10, 20
# Unpack into x and y variables
x, y = get_coordinates()
print(f"x = {x}, y = {y}") # Should print: x = 10, y = 20

def divide_remainder(a, b):
    return ( a // b ), ( a % b )
    # Return both integer division and remainder
    # Test it
result, leftover = divide_remainder(17, 5)
print(f"17 ÷ 5 = {result} remainder {leftover}") # Should print: 3 remainder 2

def get_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average
# Return minimum, maximum, and average
# Handle empty list case
values = [15, 3, 27, 9, 41]
minimum, maximum, average = get_statistics(values)
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")