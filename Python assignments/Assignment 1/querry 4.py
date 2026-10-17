print("By Devang Bhardwaj")
# Exercise 4: ATM Withdrawal
# Write a Python program for ATM withdrawal.
# Conditions:
# Check whether PIN is correct.
# If PIN is correct:
# Check whether withdrawal amount is a multiple of 100.
# If yes, check whether balance is sufficient.
# If sufficient, withdraw the amount.
# Otherwise print "Insufficient Balance".
# If PIN is incorrect, print "Invalid PIN".
correct_pin = 1234
balance = 10000

pin = int(input("Enter PIN: "))

if pin == correct_pin:
    amount = int(input("Enter withdrawal amount: "))

    if amount % 100 == 0:
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Remaining balance =", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be a multiple of 100")
else:
    print("Invalid PIN")




# Exercise 5: E-Commerce Discount
# An online shopping website provides discount based on:
# If cart amount >= ₹5000:
# If customer is a premium member:
# Discount = 20%
# Otherwise:
# Discount = 10%
# If cart amount < ₹5000:
# If premium member:
# Discount = 5%
# Otherwise:
# No discount.
# Print final amount.

cart_amount = float(input("Enter cart amount: "))
premium = input("Are you a premium member? (yes/no): ")

if cart_amount >= 5000:
    if premium == "yes":
        discount = 20
    else:
        discount = 10
else:
    if premium == "yes":
        discount = 5
    else:
        discount = 0

discount_amount = cart_amount * discount / 100
final_amount = cart_amount - discount_amount

print("Discount =", discount, "%")
print("Final amount =", final_amount)



