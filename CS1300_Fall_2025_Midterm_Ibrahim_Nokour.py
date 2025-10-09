## 1. String Manipulation
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"
# Task 1 first name
print(full_name.split(" ")[0])
# Task 2 last name
print(full_name.split(" ")[-1])
# Task 3 initials
initials = ""
initials += f"{full_name.split(" ")[0][0]}."
initials += f"{full_name.split(" ")[1][0]}."
initials += f"{full_name.split(" ")[2][0]}."

print(initials)

## 2. Restaraunt rating calculator
atmosphere = 4.5
food = 3.4
service = 2.5
cleanness = 3.0

average = (atmosphere * 0.1) + (food * 0.45) + (service * 0.20) + (cleanness * 0.25) / 4

print(average)

score = "*" * int(average / 1)
print(score)

## 3. Movie Review
numbers = [3,5,4,3,2,1,3]

numbers.append(4)
print(numbers)

numbers[2] = 3
print(numbers)

del numbers[5]
print(numbers)

numbers.insert(2, 3)
print(numbers)

subnumbers = numbers[0:3]
print(subnumbers)

print(f"Movie Review Numbers: {len(numbers)}")
print(f"First Movie Review Number: {numbers[0]}")
print(f"Last Movie Review Number: {numbers[-1]}")

## 4. Shopping Cart

items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99]
cart = []
cart_total = 0.0

if "milk" in items:
    cart.append("milk")
    price = prices[items.index("milk")]
    cart_total += price
    print(cart_total)

if "eggs" in items:
    cart.append("eggs")
    price = prices[items.index("eggs")]
    cart_total += price
    print(cart_total)

if "cookies" in items:
    cart.append("cookies")
    price = prices[items.index("cookies")]
    cart_total += price
    print(cart_total)
else:
    print("Sorry we do not have any cookies in stock.")

print(f"Original Total: {cart_total}")
if cart_total > 6.00:
    cart_total -= (cart_total * 0.1)
    print("We've applied a special discount for you")
    print(f"New Total: {cart_total}")

print("*" * 8)
print("RECIEPT")
print(cart)
print(f"Number of items: {len(cart)}.")
print(f"Final Total: {cart_total}")