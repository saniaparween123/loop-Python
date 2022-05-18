# 24. Write a program to display sum of odd numbers and even numbers
# separately that fall between two numbers accepted from the user.
# (including both numbers) 100 and 500.


num = int(input("enter start number"))
num1 = int(input("enter ending number"))
while num <= num1:
    if num % 2 == 0:
        print(num, "even number")
    if num % 2 != 0:
        print(num, "odd number")
    num = num + 1
