def get_order_info():
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    return price, quantity

def calculate_order(price, quantity):
    total = price * quantity
    tax = total * 0.08
    final = total + tax
    return final

def process_order():
    # This does too much!
    price, quantity = get_order_info()
    final = calculate_order(price, quantity)
    print(f"Total: ${final:.2f}")

process_order()


def check_length(password):
    if len(password) >= 8:
        return True 
    else:
        return False
def check_case(password):
    uppercase = False
    lowercase = False
    for char in password:
        if char.isupper():
            uppercase = True
    for char in password:
        if char.islower():
            lowercase = True
            
            

    return uppercase, lowercase
def validate_password(password):

    length_good = check_length(password)
    uppercase_good, lowercase_good = check_case(password)
    if length_good and uppercase_good and lowercase_good:
        print("Pass")
        return True

# Currently does everything
# Check length >= 8
# Check has uppercase
# Check has lowercase
# Check has number
# Return True if all pass
# Break into separate functions:
# def check_length(password):
# def check_uppercase(password):
# etc.