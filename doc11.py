# 11. Write a program to find the sum of the digits of a number accepted from
# the user.


i = 1
sum = 0
user = int(input("enter"))
while i <= user:
    sum = sum + i
    print(sum)
    i = i + 1
