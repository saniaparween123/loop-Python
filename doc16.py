# 16. Write a program to print the factorial of a number accepted by the user.


i = int(input("enter"))
f = 1
while i >= 1:
    f = f * i
    i = i - 1
print(f)
