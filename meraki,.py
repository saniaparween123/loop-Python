# Take input of weights of 11 people and then print their average and
# then check whether the average weight is a multiple of 5 or not?
# This means that when you will divide the average weight by 5,
# the remainder should be 0.

i = 1
sum = 0
while i <= 11:
    people = int(input("enter"))
    sum = sum + people
    i = i + 1
print(sum)
average = sum / 11
if average % 5 == 0:
    print(average, "average is divisible by 5 reminder is 0")
else:
    print(average, "average is not divisible by 5 ")
