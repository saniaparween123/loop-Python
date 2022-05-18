# 12. Write a program to find the product of the digits of a number
#  accepted from the user.

i = int(input("enter"))
product = 1
while i > 0:
    product = product*(i % 10)
print(product)
