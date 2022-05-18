# 18. Write a program to convert binary to decimal.


num = int(input("enter binary number:-"))
sum = 0
i = 0
while num != 0:
    rem = num % 10
    sum = sum + + rem * pow(2, i)
    num = num//10
    i = i + 1
print("Decimal number", sum)
