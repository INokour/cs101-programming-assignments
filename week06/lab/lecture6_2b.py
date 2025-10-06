errors = []
card = int(input("Enter your card number: "))

cardType = "Visa"
if str(card)[0] == "4":
    cardType = "Visa"
elif str(card)[0] == "5":
    cardType = "Mastercard"
else:
    errors.append("Invalid card number, not Visa or Mastercard")

expInput = input("Enter the expiration date: ")
if expInput.split("/"):
    print(expInput.split("/")[0:2])