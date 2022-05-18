# 13. Write a program to reverse the number accepted by the user.


i = 0
num = int(input("enter number"))
while i <= num:
    print(num)
    num = num - 1


# 13. Write a program to reverse the number accepted by the user.


i = int(input("enter"))
reverse = 1
while i > 0:
    reverse = (i % 10)
    i = i // 10
    print(reverse, end="")
