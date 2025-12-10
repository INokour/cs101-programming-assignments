# # Scenario 1: Print all months of the year
# # Your answer: for or while? Why?
# # For, because you want to print "for" every month in the year

# # Scenario 2: Keep rolling dice until you get a 6
# # Your answer: for or while? Why
# # While, as you want to roll conditionally

# #Exercise 2

# # Original for loop:
# for i in range(5):
#     print(i)

# # while loop
# i = 0;

# while i < 5:
#     i+= 1
#     print(i)

# # Basic While Loop
# count = 0
# print("Counting with while")
# while count <= 5:
#     print(f" Count is: {count}")
#     count += 1 # CRUCIAL: Update the condition variable
# print("Loop ended!\n")

# # User input example
# print("Password checker:")
# password = "python123"
# attempts = 2

# while password != "python123" and attempts < 3:
#     password = input("Enter password: ")
#     attempts += 1
#     if password != "python123":
#         print(f" Wrong! {3-attempts} attempts left")
#     if password == "python123":
#         print("Access granted!")
#     else:
#         print("Too many attempts!")

# # Exercise 1
# # Print numbers 1 to 5 using while
# num = 1
# while num < 5: # Fill in condition
#     print(num)
#     num += 1 # Update num

# value = 1
# # Your while loop here
# # Should print: 1, 2, 4, 8, 16, 32, 64
# while value < 100:
#     print(value)
#     value *= 2


# # Keep showing menu until user chooses to exit
# # Menu options: 1. Say Hello, 2. Say Goodbye, 3. Exit
# choice = 0
# choice = int(input("Select a choice [1-3]: "))
# # Your code here
# while choice > 0:

#     if choice == 1:
#         print('Hello')
#         choice = int(input("Select a choice [1-3]: "))
#     elif choice == 2:
#         print("Goodbye")
#         choice = int(input("Select a choice [1-3]: "))
#     else:
#         print("Exit.")
#         exit()

# # 1. Loop while score is less than 100
# score = 0
# while score < 100: # Your condition
#     score += 10
# # 2. Loop while answer is not "yes"
# answer = "no"
# while answer != "yes": # Your condition
#     answer = input("Continue? ")

# # This should print even numbers from 2 to 10
# num = 0
# while (num < 10) and (num % 2 == 0) : # Fix this condition
#     print(num)
#     num += 2
    
# # Loop while: health > 0 AND (has_ammo OR has_shield)
# health = 100
# ammo = 50
# shield = True

# while health > 0 and (ammo > 0 or shield) :
#     print(f"You are still alive and have ammo. Health: {health} Ammo: {ammo}")
#     if ammo > 0:
#         ammo -= 1
#     health -= 1
#     print("took 1 damage")
    

# # Fix this code:
# count = 10
# while count > 0:
#     print(count)
# # What's missing? the iteration
#     count -= 1

# user_input = ""
# # Add a maximum attempts limit (5) to this loop
# maximum_attempts = 0
# while user_input != "quit" and maximum_attempts <= 5:
#     user_input = input("Enter command: ")
#     maximum_attempts += 1
# # Your safety code here
# print("Command failed, maximum attempts reached [5].")


# # This should find the first number divisible by both 3 and 5
# num = 0
# while (num < 100) and (num % 2 == 0): # Bug here!
#     num += 1
#     print(f"Found: {num}")
# # What's wrong? How to fix?



# # Stop counting when you reach 5
# for i in range(10):
#     print(i)
#     if i == 5:
#         break
#     # Add break here

# numbers = [3, 7, 9, 2, 11, 4, 13]
# # Write loop with break to find and print first even number
# for number in numbers:
#     if number % 2 == 0:
#         print(number)
#         break

# # Allow 3 password attempts
# # Use break when correct password entered
# # Password is "secure123"
# correct_password = "secure123"
# max_attempts = 3
# attempts = 0

# while True:
#     if attempts == max_attempts:
#         print("Max attempts reached.")
#         break
#     passInput = input("Enter password: ")
#     attempts += 1
#     if str(passInput) == correct_password:
#         break

# Print 0-5 but skip 3
for i in range(6):
# Add continue to skip 3
    if i == 3: continue
    print(i)

scores = [85, -5, 92, 150, 78, 45, 200]
# Use continue to skip invalid scores (must be 0-100)
# Calculate average of valid scores only
for score in scores:
    if score < 0 or score > 100: continue
    print(score)

# Process words that are:
# - Not empty
# - More than 2 characters
# - Don't start with 'x'
words = ["hi", "xerox", "", "python", "xy", "code", "x"]
for word in words:
    if len(word) < 2:
        continue
    if word[0] == "x":
        continue
    print(word)

# Add else to confirm all numbers are positive
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num < 0:
        print("Found negative!")
        break
    else:
        print(num)

# Search for a vowel in a word
word = "fruits"
vowels_found = []
# Write loop with else to report if no vowels found

for letter in word:
    for vowel in "aeio":
        if letter == vowel:
            print(f"Vowel found: {letter}")
            vowels_found.append(letter)
            continue
if len(vowels_found) < 1:
    print("No vowels found.")

scores = [75, 82, 91, 68, 73]
passing_scores = []
for score in scores:
    if score < 60:
        print(f"A student did not pass. Score: {score}")
        break
else:
    print(f"All students passed.")