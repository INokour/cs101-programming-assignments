# TODO: Create a store system with these features:
# 1. Display a menu of 5 items with prices
# 2. Let user select one item
# 3. Ask for quantity
# 4. Apply discounts:
# - 10+ items: 10% off
# - Member: additional 5% off
# 5. Calculate tax (8%)
# 6. Show final receipt
print("=== CORNER STORE ===")
# Your code here

menu = {"Item 1":{"Name": "1lb Flour", "Price": 4.00, "Quantity":100}, "Item 2":{"Name": "25lb Rice", "Price": 30.00, "Quantity":10}, "Item 3":{"Name": "1 Gal Milk", "Price": 2.50, "Quantity":43}}
itemChoice = None;

itemSelection = input("What item would you like? [1-5] ")
itemChoice = menu[f"Item {itemSelection}"]

print(f"Chose {itemChoice["Name"]}, it costs ${itemChoice["Price"]}, and there are {itemChoice["Quantity"]} left.")

quantitySelection = input("How many would you like to buy? ")

itemChoiceTotal = itemChoice["Price"] * float(quantitySelection)

print(f"Great your total is ${itemChoiceTotal}")

totalPrice = itemChoice["Price"]

isMember = input("Are you a member?")

if isMember == "yes" or isMember == "y":
    totalPrice = totalPrice - (totalPrice * 0.05)
    print(f"We've applied a 5% discount for you, your new total is {totalPrice}")

if float(quantitySelection) >= 10:
    totalPrice = totalPrice - (totalPrice * 0.1)
    print(f"For buying more than 10 items, we are giving you an additional 10% off. Your new total is {totalPrice}")




print("======Reciept======")
print("Thank you for shopping here.")
print("Items Purchased:")
print(f"{itemChoice["Name"]}, Unit Price: ${itemChoice["Price"]}        x{int(quantitySelection)}    ${itemChoice["Price"] * float(quantitySelection)}")

itemChoice["Quantity"] = itemChoice["Quantity"] - float(quantitySelection)

print(menu)
