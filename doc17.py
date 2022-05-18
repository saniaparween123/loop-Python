# 17. Write a program to check whether a number is Armstrong or not.
# (Armstrong number is a number that is equal to the sum of cubes of its digits,
# for example : 153 = 1^3 + 5^3 + 3^3.)


i = int(input("enter:"))
a = i
sum = 0
while i > 0:
    sum = sum+(i % 10)**3
    i = i//10
if sum == a:
    print(sum, "armstrong")
else:
    print(sum, "not an armstrong")
