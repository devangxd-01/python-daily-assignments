# 1. Product Stock Management
#
# Question:
# A dictionary contains products and their available stock.
# Use a loop and nested conditions to display the stock status.
#
# Conditions:
# Stock = 0 -> Out of Stock
# Stock <= 5 -> Low Stock
# Stock > 5 -> Available

products = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 0,
    "Monitor": 7,
    "Printer": 2
}

for product, stock in products.items():
    if stock == 0:
        print(product, "-> Out of Stock")
    else:
        if stock <= 5:
            print(product, "-> Low Stock")
        else:
            print(product, "-> Available")


# 2. Student Eligibility
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


# 3. Bank Account Classification
#
# Question:
# A dictionary contains customer names and account balances.
#
# Conditions:
# Balance > 0:
# Balance >= 10,000 -> Premium Account
# Otherwise -> Regular Account
# Balance = 0 -> No Balance
# Balance < 0 -> Overdraft

accounts = {
    "Rahul": 25000,
    "Amit": 5000,
    "Priya": 0,
    "Neha": -2000
}

for name, balance in accounts.items():
    if balance > 0:
        if balance >= 10000:
            print(name, "-> Premium Account")
        else:
            print(name, "-> Regular Account")
    elif balance == 0:
        print(name, "-> No Balance")
    else:
        print(name, "-> Overdraft")
