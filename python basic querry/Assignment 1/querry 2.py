print("By Devang Bhardwaj")
# Exercise 6: Count even and odd numbers between 1 and 50.
even_count = 0
odd_count = 0

for i in range(1, 51):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)


# Exercise 7: Print the multiplication table of 7.
for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)


# Exercise 8: Print all odd numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 != 0:
        print(i)



# Exercise 9: Find the sum of even numbers from 1 to 100.
sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i

print("Sum of even numbers =", sum)
