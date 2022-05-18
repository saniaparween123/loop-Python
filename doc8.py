# 8. Write a program to print a table of a number entered from the user.


i = 1
user = int(input("enter:"))
while i <= 10:
    print(i*user)
    i = i + 1


# 8. Write a program to print a table of a number entered from the user.

# without using multiply

i = 1
sum = 0
user = int(input("enter:"))
while i <= 10:
    sum = sum + user
    i = i + 1
    print(sum)
