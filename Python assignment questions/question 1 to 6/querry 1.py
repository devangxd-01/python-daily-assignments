# 1. Check Even/Odd Values
#
# Question:
# Given a dictionary, check whether each value is even or odd.
#
# If the value is:
# Even and greater than 20 -> Large Even
# Even and <= 20 -> Even
# Odd -> Odd

data = {
    "a": 10,
    "b": 15,
    "c": 25,
    "d": 30,
    "e": 40
}

for key, value in data.items():
    if value % 2 == 0:
        if value > 20:
            print(key, "-> Large Even")
        else:
            print(key, "-> Even")
    else:
        print(key, "-> Odd")


# 2. Shopping Cart Classification
#
# Question:
# A dictionary contains products and their prices.
#
# Conditions:
# Price >= 1000:
# Price >= 5000 -> Premium Product
# Otherwise -> Expensive Product
# Price < 1000 -> Affordable Product

products = {
    "Mobile": 15000,
    "Mouse": 500,
    "Laptop": 60000,
    "Keyboard": 1200
}

for product, price in products.items():
    if price >= 1000:
        if price >= 50000:
            print(product, "-> Premium Product")
        else:
            print(product, "-> Expensive Product")
    else:
        print(product, "-> Affordable Product")


# 3. Student Eligibility
#
# Question:
# The dictionary contains student attendance and marks.
#
# Conditions:
# Attendance >= 75:
# Marks >= 40 -> Eligible
# Marks < 40 -> Failed in Exam
# Attendance < 75 -> Not Eligible

students = {
    "Rahul": {"attendance": 85, "marks": 70},
    "Amit": {"attendance": 60, "marks": 80},
    "Priya": {"attendance": 90, "marks": 35},
    "Neha": {"attendance": 78, "marks": 55}
}

for name, details in students.items():
    attendance = details["attendance"]
    marks = details["marks"]

    if attendance >= 75:
        if marks >= 40:
            print(name, "-> Eligible")
        else:
            print(name, "-> Failed in Exam")
    else:
        print(name, "-> Not Eligible")

