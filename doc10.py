# 10. Write a program to check whether a number is prime or not.


a = int(input("enter number:"))
i = 1
c = 0
while i <= a:
    if a % i == 0:
        c = c+1
    i += 1
if c == 2:
    print(a, "prime number")
else:
    print(a, "not a prime number")
