# Question Meraki

# Make a program to print the numbers from 11 to 101.
# The loop counter should start from 156

# Answer :-
# first subtract
# 101 - 11 = 90
# second add
# 90 + 156 = 246
# third substract
# 156 - 11 = 145

i = 156
# 101 - 11 = 90
# 90 + 156 = 246
while i <= 246:
    num = i - 145
# 156 - 11 = 145
    print(num)
    i = i + 1


#     Question Meraki

# answer

i = 1
sum = 0
while i <= 4:
    user = int(input("enter number:- "))
    sum = sum + user
    i = i + 1
print(sum)
