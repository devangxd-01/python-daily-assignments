print("By Devang Bhardwaj")

# Exercise 1: Movie Ticket Booking
# Create a ticket booking system.
# Conditions:
# Check whether seats are available.
# If available:
# Check customer age.
# If age < 5 -> Free
# If age 5-12 -> 50% discount
# If age > 60 -> 30% discount
# Otherwise -> Full price.
# If no seats -> "House Full".

seats = int(input("Enter number of available seats: "))

if seats > 0:
    age = int(input("Enter customer age: "))
    ticket_price = 200

    if age < 5:
        final_price = 0
        print("Free ticket")
    elif age >= 5 and age <= 12:
        final_price = ticket_price * 0.50
        print("50% discount")
    elif age > 60:
        final_price = ticket_price * 0.70
        print("30% discount")
    else:
        final_price = ticket_price
        print("Full price")

    print("Final ticket price =", final_price)
else:
    print("House Full")



# Exercise 2: Student Result System
# Write a program that takes marks of 3 subjects.
# Conditions:
# If every subject has marks >= 40:
# Calculate percentage.
# If percentage >= 75 -> Distinction
# If percentage >= 60 -> First Division
# If percentage >= 50 -> Second Division
# Otherwise -> Pass
# If any subject is below 40 -> Fail.

marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))

if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
    percentage = (marks1 + marks2 + marks3) / 3

    print("Percentage =", percentage)

    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    else:
        print("Pass")
else:
    print("Fail")



# Exercise 3: E-Commerce Discount
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

