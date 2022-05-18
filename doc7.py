# 7. Write a program to print the sum of the first 10 Even numbers.


i = 2
sum = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
        sum = sum + i
    i = i + 1
print(sum)
