string1 = 'Hello'
string2 = "World"
string3 = '''This is
a multiline
string'''

print("String 1:", string1)
print("String 2:", string2)
print("String 3:", string3)

# YOUR TURN: Create these strings
# Create a string with an apostrophe in it
my_string1 = "It's a nice day" # Fix this
print("My string 1:", my_string1)
# Create a string with quotes in it
my_string2 = "Hello" # He said "Hello"
print("My string 2:", my_string2)
# Create your name
my_name = "Ibrahim Nokour"
print("My name:", my_name)


# Finding the length of strings
text1 = "Python"
length1 = len(text1)
print("Length of 'Python':", length1)
text2 = "Hello World"
length2 = len(text2)
print("Length of 'Hello World':", length2)
# YOUR TURN: Find lengths
text3 = "Programming"
length3 = len(text3)
print("Length of 'Programming':", length3)
# Empty string
empty = ""
empty_length = len(empty)
print("Length of empty string:", empty_length)
# Single space
space = " "
space_length = len(space)
print("Length of single space:", space_length)
# Your name
name_length = len(my_name)
print("Length of your name:", name_length)

word = "Computer"

# Get first character
first = word[0]
print("First character:", first)
# Get last character (two ways)
last_v1 = word[7]
last_v2 = word[-1]
print("Last character (method 1):", last_v1)
print("Last character (method 2):", last_v2)

# YOUR TURN: Get these characters from "Computer"
second_char = word[1] # Should be 'o'
print("Second character:", second_char)
middle_char = word[4] # Should be 'u' (position 4)
print("Middle character:", middle_char)
third_from_end = word[-3] # Use negative index for 't'
print("Third from end:", third_from_end)

phrase = "Hello World"
# Remember: space is also a character!
# Find specific characters
h_char = phrase[0]
space_char = phrase[5]
w_char = phrase[6]
print("H is at index 0:", h_char)
print("Space is at index 5:", space_char)
print("W is at index 6:", w_char)
# YOUR TURN: Find these characters
o_in_hello = phrase[4] # First 'o' in Hello
print("First 'o':", o_in_hello)
o_in_world = phrase[6] # 'o' in World
print("Second 'o':", o_in_world)
exclamation = "Python!"
last_char = exclamation[-1] # Get the '!'
print("Exclamation:", last_char)
# Calculate middle index
text = "Programming"
text_length = len(text)
middle_index = text_length // 2 # Integer division
middle = text[middle_index]
print("Middle of 'Programming':", middle)

message = "Python Programming"
# Get "Python" (indices 0-5)
first_word = message[0:6]
print("First word:", first_word)
# Get "Programming" (indices 7-end)
second_word = message[7:18]
print("Second word:", second_word)
# YOUR TURN: Extract these substrings
# Get "Prog" from message
prog = message[7:11]
print("Prog:", prog)
# Get "gram" from message
gram = message[10:14]
print("gram:", gram)
# Get "Python Prog" (first 11 characters)
first_part = message[0:11]
print("First part:", first_part)
# Get "ming" (last 4 characters)
last_part = message[14:18]
print("Last part:", last_part)

text = "Hello World"
# Shortcuts for common slices
from_start = text[:5] # First 5 characters
print("First 5:", from_start)
to_end = text[6:] # From index 6 to end
print("From index 6:", to_end)
copy_all = text[:] # Copy entire string
print("Full copy:", copy_all)
# YOUR TURN: Use shortcuts
# Get first 3 characters of text
first_three = text[:3]
print("First three:", first_three)
# Get last 5 characters of text
last_five = text[5:]
print("Last five:", last_five)
# Skip first and last character
middle = text[1:-1]
print("Middle part:", middle)
# Get everything except last 3 characters
except_last = text[:-3]
print("Except last 3:", except_last)

numbers = "0123456789"
# Every second character
every_second = numbers[::2]
print("Every second:", every_second)
# Every third character
every_third = numbers[::3]
print("Every third:", every_third)
# Reverse the string
reversed_nums = numbers[::-1]
print("Reversed:", reversed_nums)
# YOUR TURN: Create these slices
alphabet = "abcdefghijklmnop"
# Get every second letter starting from 'a'
pattern1 = alphabet[::2]
print("Pattern 1:", pattern1) # Should be "acegikmo"
# Get every second letter starting from 'b'
pattern2 = alphabet[1::2]
print("Pattern 2:", pattern2) # Should be "bdfhjlnp"
# Get last 5 characters reversed
last_reversed = alphabet[:-5:-1]
print("Last 5 reversed:", last_reversed) # Should be "ponml"
# Reverse your name
name_reversed = my_name[::-1]
print("Name reversed:", name_reversed)

# Using + to join strings
first = "Python"
second = "Programming"
combined = first + " " + second
print("Combined:", combined)
# Building strings piece by piece
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print("Message:", message)
# YOUR TURN: Create these strings
word1 = "Data"
word2 = "Science"
# Create "Data Science"
phrase1 = word1 + " " + word2
print("Phrase 1:", phrase1)
# Create "DataScience" (no space)
phrase2 = word1 + word2
print("Phrase 2:", phrase2)
# Create a sentence
subject = "I"
verb = "love"
object = "Python"
sentence = subject + " " + verb + " " + object + "!"
print("Sentence:", sentence)
# Create an email address
username = "student"
domain = "university.edu"
email = username + "@" + domain
print("Email:", email)

# Using * to repeat strings
star = "*"
line = star * 20
print("Line of stars:", line)
dash = "-"
separator = dash * 30
print("Separator:", separator)
# YOUR TURN: Create these patterns
# Create 10 equals signs
equals = "=" * 10
print("Equals:", equals)
# Create "HoHoHo"
ho = "Ho" * 3
print("Ho pattern:", ho)
# Create a border: "+--------+"
plus = "+"
minus = "-" * 8
border = plus + minus + plus
print("Border:", border)
# Create "ABABAB"
ab = "AB"
pattern = ab * 3
print("AB pattern:", pattern)
# Create 5 copies of your initials
first_initial = my_name[0]
space = " "
initials_repeated = (first_initial + space) * 5
print("Initials:", initials_repeated)